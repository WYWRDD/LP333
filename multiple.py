def multiple():
    n = int(input("Введите четырехзначное число: "))
    if n%3 == 0:
        d1 = n % 10
        n = n // 10
        d2 = n % 10
        n = n // 10
        print("Сумма цифр числа: ", n + d1 + d2)
    else:
        print("Число не кратно трем")