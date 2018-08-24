class TeamStats:
    @staticmethod
    def players_per_position(player_list):
        players_in_position = {}
        for player in player_list:
            position = player['Position']
            if position in players_in_position:
                players_in_position[position] = players_in_position[position] + 1
            else:
                players_in_position[position] = 1
        return players_in_position

    @staticmethod
    def average_points(player_list):
        players = len(player_list)
        if players == 0:
            return 0
        average = 0.0
        for player in player_list:
            average = average + player['PPG']
        return average/players

    @staticmethod
    def field_average(player_list, field_name, conversions=None):
        val = 0
        players = len(player_list)
        if conversions is None:
            for player in player_list:
                val = val + player[field_name]
        else:
            for player in player_list:
                val = val + conversions(player[field_name])
        return val / players

    @staticmethod
    def leaders(player_list):
        players_srt = sorted(player_list, key=lambda x: x['PPG'], reverse=True)
        ranks = ['Gold', 'Silver', 'Bronze']
        return [
            {
                ranks[i]:players_srt[i]['Name'],
                'PPG': players_srt[i]['PPG']
            } for i in range(min(3, len(players_srt)))
        ]
