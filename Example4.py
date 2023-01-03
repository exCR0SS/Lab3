class Main:

    userNum1 = int(input("Введите первое число: "))
    userNum2 = int(input("Введите второе число: "))

    minNum = userNum1 if userNum1 < userNum2 else userNum2
    maxNum = userNum1 if userNum1 > userNum2 else userNum2

    while minNum <= maxNum:
        print(minNum)
        minNum += 1

    for i in range((maxNum-minNum) + 1):
        print(minNum)
        minNum += 1
