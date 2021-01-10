# 3. Дано число. На ти сумму и произведение его цифр.

num = int(input("Введите число:"))

d = []

while num:
    d += [num % 10]
    num //= 10

print("Сумма: ", sum(d))

p = 1

for i in d:
    p *= i
print("Произведение: ", p)

