# Напишите программу, которая принимает на вход число N и выдает
#  последовательность из N членов.

# in 5 out 1, -3, 9, -27, 81 

n = int(input("Введите N: "))

number = 1

for i in range(n):
    print(number, end=", ")
    number = number * -3
print()