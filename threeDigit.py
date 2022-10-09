def threeDigit():
    n = int(input("Введите число: "))
    if 100 <= n <= 999:
        print("Число трехзначное")
    else:
        print("Число не трехзначное")