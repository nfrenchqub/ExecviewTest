class Conversions:
    @staticmethod
    def ft_in_to_in(x: str) -> int:
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

    @staticmethod
    def lbs_value(x: str) -> int:
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
            raise ValueError('Malformed input to lbs_value. Expects "X lb" recv: %s' % x)
        return lbs

    @staticmethod
    def in_to_cm(x: int) -> float:
        return 2.54 * x
