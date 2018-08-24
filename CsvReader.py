import typing


class CsvReader:
    # States for CSV Parser FSM
    APPEND = 0
    SEPARATOR = 1
    DROP = 2

    def __init__(self, delimiter: str=',', quote_char: str='"', header_row: bool=True, file: typing.TextIO=None):
        if file is None:
            raise ValueError('You must provide a file to parse.')

        self._delimiter = delimiter
        self._quote_char = quote_char
        self._state = CsvReader.APPEND

        all_lines = []

        line = file.readline()
        while line:
            this_line = []
            this_value = []
            for c in line:
                if self._is_transition_char(c):
                    self._transition(c)
                if self._state == CsvReader.APPEND:
                    this_value.append(c)
                elif self._state == CsvReader.SEPARATOR:
                    this_line.append(''.join(this_value))
                    this_value = []
                    self._state = CsvReader.APPEND
                if self._state == CsvReader.DROP:
                    self._state = CsvReader.APPEND

            this_line.append(''.join(this_value))
            all_lines.append(this_line)
            line = file.readline()

        self.all_lines = all_lines
        self._row = -1
        self._rows = len(all_lines)

    def get_rows(self):
        return self.all_lines

    def get_row(self):
        self._row = self._row + 1
        if self._row >= self._rows:
            return None
        return self.all_lines[self._row]

    def _is_transition_char(self, c):
        return c in (self._delimiter, self._quote_char, '\n')

    def _transition(self, c):
        if self._state == CsvReader.APPEND:
            if c == self._delimiter:
                self._state = CsvReader.SEPARATOR
            elif c == '\n':
                self._state = CsvReader.DROP

