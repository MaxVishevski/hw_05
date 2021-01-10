# 5. В списке целых случайных чисел с количеством
# элементов n определить максимальное число и
# заменить им все четные по значению элементы.




from random import randrange

import sys

n = int(input("вВведите количество элементов: "))

d = []

max_number = sys.maxsize


for i in range(n):
    z = randrange(max_number)
    d += [z]

print(d)

max_number_of_list = max(d)

j = 0
while j < len(d):
    if d[j] % 2 == 0:
        d[j] = max(d)

    j += 1
print(d)

