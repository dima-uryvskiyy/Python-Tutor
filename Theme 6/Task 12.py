"""
Условие
Последовательность состоит из различных натуральных чисел и завершается числом 0.
Определите значение второго по величине элемента в этой последовательности.
Гарантируется, что в последовательности есть хотя бы два элемента
"""


lst = []
value = int(input())
while value != 0:
    lst.append(value)
    value = int(input())

del lst[lst.index(max(lst))]
print(max(lst))