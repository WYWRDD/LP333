def minimal():
    a = int(input("Введите переменную a:"))
    b = int(input("Введите переменную b:"))
    c = int(input("Введите переменную c:"))

    if a<b<c:
        print("Минимально значение A: ", a)
    elif b<a<c:
        print("Минимально значение B: ", b)
    elif c<a<b:
        print("Минимально значение C: ", c)
    else:
        print("Неизвестная ошибка")