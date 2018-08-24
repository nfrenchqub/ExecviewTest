from .CsvReader import CsvReader
from .TeamStats import TeamStats
from .Conversions import Conversions
import sys
import json


def main():

    field_lambdas = [None for _ in range(9)]
    field_lambdas[0] = lambda x: int(x)
    field_lambdas[2] = lambda x: int(x)
    field_lambdas[8] = lambda x: float(x)

    team_data = []
    fields = {}

    with open(sys.argv[1]) as csv_file:
        csv_reader = CsvReader(header_row=True, file=csv_file, field_lambdas=field_lambdas)
        team_data = csv_reader.get_rows()
        fields = csv_reader.get_headers()

    if not team_data or not fields:
        raise Exception('No data read or column headers missing. Check input.')

    team_output = {
        'Players': sorted(team_data, key=lambda x: x['PPG'], reverse=True),
        'Average_PPG': TeamStats.average_points(team_data),
        'Leaders': TeamStats.leaders(team_data),
        'PlayersPerPosition': TeamStats.players_per_position(team_data),
        'AverageHeight': round(
            TeamStats.field_average(
                team_data,
                'Height',
                lambda x: Conversions.in_to_cm(Conversions.ft_in_to_in(x))
            ),
            2)
    }

    with open('output.json', 'w') as out_file:
        json.dump(team_output, out_file, indent=4)


if __name__ == '__main__':
    main()
