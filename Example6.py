class Main:

    numArray = list()
    number, i = 0, 0
    userNumber = input()

    if userNumber.isdigit():
        size = int(userNumber)

        while i <= size:
            if number % 5 == 2:
                numArray.append(number)
            number += 1
            i += 1
    else:
        print("Введите число!")

    print(*numArray)