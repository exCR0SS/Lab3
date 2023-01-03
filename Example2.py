class Main:

    weekDay = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
    userDay = str.lower(input("Введите день недели: "))

    if userDay in weekDay:
        print(weekDay.index(userDay) + 1)
    else:
        print("Такого дня нет")





