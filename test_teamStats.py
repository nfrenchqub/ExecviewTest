from unittest import TestCase
from .TeamStats import TeamStats
from .Conversions import Conversions


class TestTeamStats(TestCase):
    def setUp(self):
        self._team = [{
            "Id": 4,
            "Position": "SG",
            "Number": 23,
            "Country": "United States",
            "Name": "Jordan, Michael",
            "Height": "6 ft 6 in",
            "Weight": "215 lb",
            "University": "North Carolina",
            "PPG": 32.6
        },
            {
                "Id": 10,
                "Position": "SF",
                "Number": 33,
                "Country": "United States",
                "Name": "Pippen, Scottie",
                "Height": "6 ft 7 in",
                "Weight": "220 lb",
                "University": "Central Arkansas",
                "PPG": 18.6
            },
            {
                "Id": 3,
                "Position": "PF",
                "Number": 54,
                "Country": "United States",
                "Name": "Grant, Horace",
                "Height": "6 ft 10 in",
                "Weight": "245 lb",
                "University": "Clemson",
                "PPG": 13.2
            },
            {
                "Id": 1,
                "Position": "PG",
                "Number": 10,
                "Country": "United States",
                "Name": "Armstrong, B.J",
                "Height": "6 ft 2 in",
                "Weight": "175 lb",
                "University": "Iowa",
                "PPG": 12.3
            },
            {
                "Id": 14,
                "Position": "PF",
                "Number": 42,
                "Country": "United States",
                "Name": "Williams, Scott",
                "Height": "6 ft 10 in",
                "Weight": "230 lb",
                "University": "North Carolina",
                "PPG": 5.9
            },
            {
                "Id": 2,
                "Position": "C",
                "Number": 24,
                "Country": "United States",
                "Name": "Cartwright, Bill",
                "Height": "7 ft 1 in",
                "Weight": "246 lb",
                "University": "San Francisco",
                "PPG": 5.6
            },
            {
                "Id": 5,
                "Position": "PF",
                "Number": 21,
                "Country": "United States",
                "Name": "King, Stacey",
                "Height": "6 ft 11 in",
                "Weight": "230 lb",
                "University": "Oklahoma",
                "PPG": 5.4
            },
            {
                "Id": 11,
                "Position": "SG",
                "Number": 6,
                "Country": "United States",
                "Name": "Tucker, Trent",
                "Height": "6 ft 5 in",
                "Weight": "193 lb",
                "University": "Minnesota",
                "PPG": 5.2
            },
            {
                "Id": 9,
                "Position": "C",
                "Number": 32,
                "Country": "United States",
                "Name": "Perdue, Will",
                "Height": "7 ft 0 in",
                "Weight": "240 lb",
                "University": "Vanderbilt",
                "PPG": 4.7
            },
            {
                "Id": 8,
                "Position": "PG",
                "Number": 5,
                "Country": "United States",
                "Name": "Paxson, John",
                "Height": "6 ft 2 in",
                "Weight": "185 lb",
                "University": "Notre Dame",
                "PPG": 4.2
            },
            {
                "Id": 6,
                "Position": "SF",
                "Number": 22,
                "Country": "United States",
                "Name": "McCray, Rodney",
                "Height": "6 ft 7 in",
                "Weight": "220 lb",
                "University": "Louisville",
                "PPG": 3.5
            },
            {
                "Id": 12,
                "Position": "SG",
                "Number": 20,
                "Country": "United States",
                "Name": "Walker, Darrell",
                "Height": "6 ft 4 in",
                "Weight": "180 lb",
                "University": "Arkansas",
                "PPG": 2.6
            },
            {
                "Id": 13,
                "Position": "PG",
                "Number": 12,
                "Country": "United States",
                "Name": "Williams, Corey",
                "Height": "6 ft 2 in",
                "Weight": "190 lb",
                "University": "Oklahoma State",
                "PPG": 2.3
            },
            {
                "Id": 7,
                "Position": "PF",
                "Number": 45,
                "Country": "United States",
                "Name": "Nealy, Ed",
                "Height": "6 ft 7 in",
                "Weight": "238 lb",
                "University": "Kansas State",
                "PPG": 2.1
            }]

    def test_players_per_position(self):
        expected_players_per_position = {
            "PG": 3,
            "C": 2,
            "PF": 4,
            "SG": 3,
            "SF": 2
        }
        self.assertEqual(TeamStats.players_per_position(self._team), expected_players_per_position)

    def test_average_points(self):
        self.assertEqual(
            round(TeamStats.average_points(self._team), 2),
            8.44
        )

    def test_field_average(self):
        self.assertEqual(
            round(TeamStats.average_points(self._team), 2),
            8.44
        )
        self.assertEqual(
            round(
                TeamStats.field_average(
                    self._team,
                    'PPG'
                ),
                2),
            8.44
        )
        self.assertEqual(
            round(
                TeamStats.field_average(
                    self._team,
                    'Height',
                    lambda x: Conversions.in_to_cm(Conversions.ft_in_to_in(x))
                ),
                2),
            200.66  # Was 205.8, but believe value in file incorrect
        )
