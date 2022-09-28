# Создать список, длины n, значение формируется по формуле
# 3k + 1, где K принимает значение от 1 до n включительно.

# in 3 out [4, 7, 10];
# in 6 out [4, 7, 10, 13, 16, 19]

n = int(input("Введите n: "))

numbers = list()

# k = 1
# for i in range(n):
#     numbers.append(3 * k + 1)
#     k += 1
# print(numbers)

# Вариант 2

for k in range(1, n + 1):
    numbers.append(3 * k + 1)
print(numbers)