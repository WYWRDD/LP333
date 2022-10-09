def minimal(a, b, c):
    if a<b<c:
        print("Минимально значение A: ", a)
        return a
    elif b<a<c:
        print("Минимально значение B: ", b)
        return b
    elif c<a<b:
        print("Минимально значение C: ", c)
        return c
    else:
        print("Неизвестная ошибка")
        return None

def _minimal(a, b, c):
    if a<=b and a<=c:
        print("Минимально значение A: ", a)
        return a
    elif b<=a and b<=c:
        print("Минимально значение B: ", b)
        return b
    else:
        print("Минимально значение C: ", c)
        return c
  
        
# ТЕСТ
def test():
    print('Тест')
    print(minimal(1, 2, 3) == 1)
    print(minimal(2, 1, 3) == 1)
    print(minimal(3, 1, 2) == 1)
    print(minimal(3, 2, 1) == 1)
    print(minimal(1, 1, 3) == 1)
    print(minimal(3, 3, 1) == 1)
    print(minimal(3, 1, 3) == 1)
    print(minimal(2, 3, 1) == 1)
    
    print('Тест 2')
    print(_minimal(1, 2, 3) == 1)
    print(_minimal(2, 1, 3) == 1)
    print(_minimal(3, 1, 2) == 1)
    print(_minimal(3, 2, 1) == 1)
    print(_minimal(1, 1, 3) == 1)
    print(_minimal(3, 3, 1) == 1)
    print(_minimal(3, 1, 3) == 1)
    print(_minimal(2, 3, 1) == 1)

test()
'''
Output:
Тест
Минимально значение A:  1
True
Минимально значение B:  1
True
Неизвестная ошибка
False
Неизвестная ошибка
False
Неизвестная ошибка
False
Неизвестная ошибка
False
Неизвестная ошибка
False
Минимально значение C:  1
True
Тест 2
Минимально значение A:  1
True
Минимально значение B:  1
True
Минимально значение B:  1
True
Минимально значение C:  1
True
Минимально значение A:  1
True
Минимально значение C:  1
True
Минимально значение B:  1
True
Минимально значение C:  1
True
'''
