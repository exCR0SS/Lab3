# Напишите программу, в которой создается массив и заполняется
# случайными числами. Массив отображается в консольном окне. В этом
# массиве необходимо определить элемент с минимальным значением. В
# частности, программа должна вывести значение элемента с минимальным
# значением и индекс этого элемента. Если элементов с минимальным
# значением несколько, должны быть выведены индексы всех этих элементов.

import random

class Main:

    n = int(input("Введите размер массива: "))
    numArray = []
    maxIndexes = []
    minIndexes = []

    for i in range(n):
        numArray.append(random.randint(1, 10))

    for i in range(n):
        if numArray[i] == max(numArray):
            maxIndexes.append(i)

        if numArray[i] == min(numArray):
            minIndexes.append(i)

    print(*numArray)
    print("Минимальное значение: ", min(numArray), " его индекс(ы) в массиве: ", *minIndexes)
    print("Максимальное значение: ", max(numArray), " его индекс(ы) в массиве: ", *maxIndexes)