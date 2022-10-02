# НЕОБЯЗАТЕЛЬНОЕ ЗАДАНИЕ
#Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
import time

def rondom (n2):
    list = []
    for i in range (1, n2+1):
        list.append(round(i * (time.time() * 1000)%100))
    return list
    
list = rondom(8)
print(list)
