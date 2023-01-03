# Напишите программу, в которой создается одномерный
# символьный массив из 10 элементов. Массив заполняется буквами «через
# одну», начиная с буквы ' а ': то есть массив заполняется буквами ' а ' , ' с ' , ' е ' ,
# ' д ' и так далее. Отобразите массив в консольном окне в прямом и обратном
# порядке. Размер массива задается переменной.

class Main:

    alphabet ='abcdefghijklmnopqrstuvwxyz'

    size = int(input("Задайте размер массива: "))

    newResult = []
    resultLst = list(alphabet[::2])
    newResult = resultLst[::-1]

    print("Normal: ", *resultLst[:size:])
    print("Reverse: ", *newResult[len(newResult) - size::])

