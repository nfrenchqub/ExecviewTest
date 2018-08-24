import typing


class CsvReader:
    # States for CSV Parser FSM
    APPEND = 0
    SEPARATOR = 1
    DROP = 2
    DROP_TO_QUOTE = 3
    QUOTED = 4
    QUOTE_OVER = 5
    FAULTED = 6

    @staticmethod
    def _field_lambda(lambdas, field):
        if lambdas is None:
            return None
        if field < len(lambdas):
            return lambdas[field]
        else:
            return None

    def __init__(self, delimiter: str=',', quote_char: str='"', header_row: bool=True, file: typing.TextIO=None,
                 field_lambdas: list=None):
        if file is None:
            raise ValueError('You must provide a file to parse.')

        self._header_line = None
        self._delimiter = delimiter
        self._quote_char = quote_char
        self._state = CsvReader.APPEND

        all_lines = []
        line_number = 1
        line = file.readline()
        while line:
            field = 0
            this_line = []
            this_value = []
            for i, c in enumerate(line):
                if self._is_transition_char(c):
                    self._transition(c)
                    if self._state == CsvReader.FAULTED:
                        raise Exception('CsvReader faulted at line %d position %d' % (line_number, i))

                if self._state in (CsvReader.APPEND, CsvReader.QUOTED):
                    this_value.append(c)
                elif self._state == CsvReader.SEPARATOR:
                    lam = CsvReader._field_lambda(field_lambdas, field)
                    if lam is not None and not (header_row and line_number == 1):
                        this_line.append(lam(''.join(this_value)))
                    else:
                        this_line.append(''.join(this_value))
                    this_value = []
                    field = field + 1
                    self._state = CsvReader.APPEND
                elif self._state == CsvReader.DROP:
                    self._state = CsvReader.APPEND
                elif self._state == CsvReader.DROP_TO_QUOTE:
                    self._state = CsvReader.QUOTED

            if self._state == CsvReader.QUOTED:
                raise Exception('CsvReader faulted at EOL %d (Unmatched quote)' % line_number)

            lam = CsvReader._field_lambda(field_lambdas, field)
            if lam is not None and not (header_row and line_number == 1):
                this_line.append(lam(''.join(this_value)))
            else:
                this_line.append(''.join(this_value))
            all_lines.append(this_line)
            line = file.readline()
            line_number = line_number + 1

        if header_row and len(all_lines) > 0:
            self._header_line = all_lines[0]
            all_lines = all_lines[1:]

        self.all_lines = all_lines
        self._row = -1
        self._rows = len(all_lines)

    def get_rows(self):
        if self._header_line:
            return [{field_name: row[i] for i, field_name in enumerate(self._header_line)} for row in self.all_lines]
        return self.all_lines

    def get_headers(self):
        return {x: i for i, x in enumerate(self._header_line)}

    def get_row(self):
        self._row = self._row + 1
        if self._row >= self._rows:
            return None
        return self.all_lines[self._row]

    def _is_transition_char(self, c):
        if self._state == CsvReader.APPEND:
            return c in (self._delimiter, self._quote_char, '\n')
        elif self._state == CsvReader.QUOTED:
            return c == self._quote_char
        elif self._state == CsvReader.QUOTE_OVER:
            return True

    def _transition(self, c):
        if self._state == CsvReader.APPEND:
            if c == self._delimiter:
                self._state = CsvReader.SEPARATOR
            elif c == '\n':
                self._state = CsvReader.DROP
            elif c == self._quote_char:
                self._state = CsvReader.DROP_TO_QUOTE

        elif self._state == CsvReader.QUOTED:
            if c == self._quote_char:
                # Reached the end-quote
                self._state = CsvReader.QUOTE_OVER

        elif self._state == CsvReader.QUOTE_OVER:
            if c == self._delimiter:
                self._state = CsvReader.SEPARATOR
            elif c == '\n' or c.isspace():
                # Drop whitespace after quotes, or line end
                self._state = CsvReader.DROP
            else:
                # Characters after quote, but before delimiter
                self._state = CsvReader.FAULTED
