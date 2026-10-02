while True:
    try:
        while True:
            num = int(input("Введите трёхзначное число"))
            #Проверка на 3-х значное число
            if 100<= num <= 999:
                a,b = divmod(num,10)
                print(b,a, sep="")
            else:
                print("Попробуйте ещё раз!")
                continue
            break
    except ValueError:
        print("Попробуйте ещё раз!")
        continue