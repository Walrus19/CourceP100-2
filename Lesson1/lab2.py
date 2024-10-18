list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

total = len(list_players)
total_in_team = total // 2
team1 = list_players[0:total_in_team]
team2 = list_players[total_in_team:]
print(team1)
print(team2)
