# Решение задачи 1: Составить пограмму нахождения среднего арифметического из 4-х чисел.
from typing import List

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))
d = int(input("Введите число d: "))

avr = (a + b + c + d) / 4
print("Среднее арифметическое = ", avr)
##################################################################
## Идея интересная, и решается хорошо.

Решение
задачи
2: Составить
программу
нахождения
факториала
N.
N = int(input("Введите число N: "))
fact = 1
i = 1

while (i <= N):
    fact = fact * i
    i = i + 1
print("Факториал = ", fact)
##################################################################
## Практичное решение!

# Решение задачи 3: Нахождение индексов максимального и минимального элемента массива
A = [5, 3, 9, 2, 7]

minIndex = 0
maxIndex = 0
minVal = A[0]
maxVal = A[0]
i = 0

while (i <= len(A) - 1):
    if A[i] < minVal:
        minIndex = i
        minVal = A[i]
    if A[i] > maxVal:
        maxIndex = i
        maxVal = A[i]
    i = i + 1

print(minIndex)
print(maxIndex)
##################################################################
## Работает! Только почему не input? Или ты сам для себя поставил нужное?

Решение
задачи
4: Задание
на «разворот» массива.Нужно
перевернуть
массив
и
записать
его
в
обратном
порядке.
A = [5, 9, 3, 7, 2]
i = 0

while (i <= (len(A) // 2) - 1):
    temp = A[i]
    A[i] = A[len(A) - i - 1]
    A[len(A) - i - 1] = temp
    i = i + 1

print(*A, sep=' ')
##################################################################
##Отлично!

# Решение задачи 5: Найти сумму элементов массива, лежащих между максимальным и минимальным по значению элементами
A = [5, 9, 3, 7, 2]
minIndex = 0
maxIndex = 0
sum = 0
i = 0

while (i <= len(A) - 1):
    if A[i] < A[minIndex]:
        minIndex = i
if A[i] > A[maxIndex]:
    maxIndex = i
i = i + 1

if minIndex > maxIndex:
    minIndex, maxIndex = maxIndex, minIndex

for i in range(minIndex + 1, maxIndex):
    sum += A[i]

print(sum)
##################################################################
## мой код длиннее)))
# array = input('Enter array: ').split()
# size = len(array)
# index = 0
# max_value_index = 0
# max_value_index = 0
# max = int(array[0])
# sum = 0
# while index < size:
#   if int(array[index]) > max:
#        max = int(array[index])
#        max_value_index = index
#        index += 1
#    elif int(array[index]) < max:
#        min = int(array[index])
#        min_value_index = index
#        index += 1
#    else:
#        index += 1
# if max_value_index > min_value_index:
#    while min_value_index < max_value_index:
#        sum = sum + int(array[min_value_index])
#        min_value_index += 1
# else:
#    while max_value_index < min_value_index:
#        sum = sum + int(array[max_value_index])
#        max_value_index += 1
# print(sum)
## вот он))

# Решение задачи 6: Найти среднее арифметическое среди всех элементов массива
# A = [5, 9, 3, 7, 2]
# sum = 0
# i = 0
#
# while (i <= len(A) - 1):
#     sum += A[i]
#     i += 1
#
# print("Среднее арифметическое элементов массива = ", sum/len(A))
