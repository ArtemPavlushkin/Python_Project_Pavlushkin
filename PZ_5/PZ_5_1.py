#Вариант 19.Составить функцию решения задачи: из заданного числа вычли сумму его цифр.
#Из результата вновь вычли сумму его цифр и т.д. Через сколько таких действий получится нуль?


def vichitanie_summi(n):
    summa_ts = 0
    coppy_n = n
    i = 0
    while coppy_n > 0:
        pos_ts = coppy_n % 10
        summa_ts = summa_ts + pos_ts
        coppy_n = coppy_n // 10
    while n > 0:
        n = n - summa_ts
        i = i + 1
    return i
t = int(input("Введите число: "))
print(vichitanie_summi(t))#hdjhvjxhkfhbkjfchkbjhcfjb