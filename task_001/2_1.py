# Напишите программу, которая принимает на вход число N  и выдает
# последовательность из N членов.

# in 5 out 1, -3, 9, -27, 81

import random

n = int(input("Введите N: "))

print([random.randint(-100, 100) for i in range(n)])
