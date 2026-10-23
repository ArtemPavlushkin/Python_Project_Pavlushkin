#Вариант 19. Дано вещественное число X и целое число N (> 0).Найти значение выражения X
#X^3/(3!)+X^5/(5!)-...+(-1)^N-X^2-N+1/((2+N+1)!) (N=12...N)
# Полученное число является приближенным значением функции sin в точке X.
while True:
    try:
        x=float(input("Введите число x: "))
        y=int(input("Введите число N>0: "))
        break
    except ValueError:
        print("Ты даун?")
        continue
reshenie=x
if y>0:
    k=1
    while k!=y:
       reshenie *= -x ** 2 / ((2 * k) * (2 * k + 1))
       k+=1
print(y)

