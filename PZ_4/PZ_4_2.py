#Дано целое число N (> 0). Найти сумму 1^1 + 2^2 + ... + N^N

while True:
    try:
        N = int(input("Введите целое число N (> 0): "))
        if N > 0:
            break
        print("N должно быть больше 0. Попробуйте снова.")
    except ValueError:
        print("Ошибка: введите целое число. Попробуйте снова.")
i = 1
a = 1
res = 0
ans = 0
while i-1 < N:
    res = i ** i
    ans += res
    i += 1
print(ans)

