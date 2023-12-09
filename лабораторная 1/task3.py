list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
player_numbers = int(len(list_players)/2 )
print(list_players[:player_numbers])
print(list_players[player_numbers:])