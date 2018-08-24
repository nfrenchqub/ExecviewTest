from unittest import TestCase
from CsvReader import CsvReader


class TestCsvReader(TestCase):
    def setUp(self):
        pass

    def test_missing_file_raises_error(self):
        self.assertRaises(ValueError, lambda: CsvReader())

    def test_reading_easy_csv_file(self):
        with open('noquotes.csv') as csv_file:
            csv_reader = CsvReader(header_row=False, file=csv_file)

        self.assertEqual(csv_reader.get_rows(), [['a', 'b'], ['c', 'd']])

    def test_header_row(self):
        with open('noquotes.csv') as csv_file:
            csv_reader = CsvReader(header_row=True, file=csv_file)
        rows = csv_reader.get_rows()
        self.assertEqual(rows, [['c', 'd']])

    def test_quote_char(self):
        with open('chicago-bulls.csv') as csv_file:
            csv_reader = CsvReader(header_row=True, file=csv_file)

        self.assertEqual(
            csv_reader.get_row(),
            ['1', 'PG', '10', 'United States', 'Armstrong, B.J.', '6 ft 2 in', '175 lb', 'Iowa', '12.3']
        )
