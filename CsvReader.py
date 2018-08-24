import typing


class CsvReader:
    def __init__(self, delimiter: str=',', quote_char: str='"', header_row: bool=True, file: typing.TextIO=None):
        if file is None:
            raise ValueError('You must provide a file to parse.')
