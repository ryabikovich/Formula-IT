money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

balance = money_capital + salary - spend
if balance > 0 :
    month_number = 1

while True:
    spend = (increase+1)*spend
    balance -= (spend-salary)
    if balance < 0:
        break
    month_number += 1
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", month_number)

