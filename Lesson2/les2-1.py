money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 2

budget = money_capital + salary - spend
# spend_add = spend * increase
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while budget > spend:
    count += 1
    spend += spend * increase
    budget = budget + salary - spend



print("Количество месяцев, которое можно протянуть без долгов:", count)
