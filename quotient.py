def quotient():
    m = int(input("Введитте число m: "))
    n = int(input("Введите число n: "))
    if m/n != 1:
        print("Частно m и n равно:", m/n)
    else:
        print("Числа не частные, сумма равна:", m+n)