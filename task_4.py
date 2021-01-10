# 4. Для заданного числа N составьте программу
# вычисления суммы S=1+1/2+1/3+1/4+...+1/N, где N –
# натуральное число.


while True:
    try:

        N = int(input("Введите натуральное число: "))
        if N < 0:
            print("неверное значание")
            continue

    except ValueError:
        print("неверный ввод")
        continue
    S = 0
    i = 1

    while i <= N:
        if N > 0:
            S += 1/i
            i += 1
        print(S)

        # else:
        #     print(N)


