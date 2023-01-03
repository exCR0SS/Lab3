# Напишите программу, в которой создается целочисленный
# массив, заполняется случайными числами и после этого значения элементов в
# массиве сортируются в порядке убывания значений.
import random

class Maim:

    n = int(input("Введите размер массива: "))
    numArray = []

    for i in range(n):
        numArray.append(random.randint(1, 10))

    numArray.sort(reverse=True)

    print("Отсортированный массив: ", *numArray)