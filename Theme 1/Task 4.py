"""
Условие
Напишите программу, которая считывает три числа и выводит их сумму. Каждое число записано в отдельной строке.
"""


n = int(input())
hours = n % (60 * 24) // 60
minutes = n % 60
print(hours, minutes)

