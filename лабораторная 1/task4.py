users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
visit = {'Общее количество': 0,
         'Уникальные посещения': 0
         }
visit['Общее количество'] = len(users)
unique = set(users)
visit['Уникальные посещения'] = len(unique)
print(visit)