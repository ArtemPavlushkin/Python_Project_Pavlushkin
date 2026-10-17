#Вариант 19. Проверить истинность высказываия: "Среди 3-х данных чисел есть хотя-бы одна пара совпадающих"
while True:
 try:
     a = int(input("Введите первое число: "))
     b = int(input("Введите второе число: "))
     c = int(input("Введите третье число: "))
     break
 except ValueError:
     print("Введите целое число!!!")
     continue
#Проверка значений
if a==b or b==c or c==a:
    print(True)
else:
    print(False)