from .CsvReader import CsvReader


def ft_in_to_in(x: str):
    format_err = x == ''
    x = x.lower()
    inches = 0
    if 'ft' in x and 'in' in x:
        as_list = x.split(' ')
        if len(as_list) == 4:
            if as_list[1] == 'ft' and as_list[3] == 'in' and as_list[0].isnumeric() and as_list[2].isnumeric():
                inches = int(as_list[0]) * 12
                inches = inches + int(as_list[2])
            else:
                format_err = True
        else:
            format_err = True
    else:
        format_err = True
    if format_err:
        raise ValueError('Malformed input to ft_in_to_in. Expects "X ft Y in", recv: %s' % x)
    return inches


def lbs_value(x: str):
    format_err = x == ''
    x = x.lower()
    lbs = 0
    if 'lb' in x:
        as_list = x.split(' ')
        if len(as_list) == 2:
            if as_list[0].isnumeric() and as_list[1] == 'lb':
                lbs = int(as_list[0])
            else:
                format_err = True
        else:
            format_err = True
    else:
        format_err = True
    if format_err:
        raise ValueError('Malformed input to ft_in_to_in. Expects "X ft Y in"')
    return lbs


def main():
    field_lambdas = [None for _ in range(9)]
    field_lambdas[5] = lambda x: ft_in_to_in(x)
    field_lambdas[6] = lambda x: lbs_value(x)

    with open('ExecviewNiallFrench/chicago-bulls.csv') as csv_file:
        csv_reader = CsvReader(header_row=True, file=csv_file, field_lambdas=field_lambdas)
        print(csv_reader.get_rows())

if __name__ == '__main__':
    main()
