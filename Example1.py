class Main:

    weekDay = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    userNumber = int(input())

    if userNumber <= 7:
        print(weekDay[userNumber - 1])
    else:
        print("Ведённое число должно быть не больше 7!")





