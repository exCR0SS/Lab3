# Напишите программу, в которой создается символьный массив из
# 10 элементов. Массив заполнить большими (прописными) буквами
# английского алфавита. Буквы берутся подряд, но только согласные (то есть
# гласные буквы ’ А ' , 1 Е ' и ' I ' при присваивании значений элементам массива
# нужно пропустить). Отобразите содержимое созданного массива в консольном
# окне.

class Main:

    alphabet ='bcdfghjklmnpqrstvwxz'

    size = int(input("Задайте размер массива: "))

    resultLst = list(alphabet.upper())

    print(*resultLst[:size:])


    