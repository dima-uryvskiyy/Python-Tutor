"""
Условие
Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!.
По данному натуральному n вычислите значение n!. Пользоваться математической библиотекой math в этой задаче запрещено.
"""


factorial = 1
for number in range(1, int(input()) + 1):
    factorial *= number
print(factorial)
