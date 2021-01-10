# 6. Задан целочисленны список c n случайных
# элементов. Определить количество участков списка,
# на котором элементы монотонно возрастают (каждое
# следующее число больше предыдущего).



from random import randrange

n = int(input("вВведите количество элементов: "))

d = []

for i in range(n):
    z = randrange(100)
    d += [z]

print(d)

j = 1
sum = 0

if n > 2:

    while j < len(d)-1:

        if d[j] > d[j-1] and d[j] > d[j+1]:

            sum += 1

        j +=1



if n <= 2:

    while j < len(d):

        if d[j] > d[j - 1]:
            sum += 1

        j += 1

print(sum)