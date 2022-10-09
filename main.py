import minVALUE
import threeDigit
import multiple
import quotient


while True:
    print("Выберите задание: \n"
          "1)Поиск минимального значения\n"
          "2)Узнать является ли число трехзначным или нет\n"
          "3)Узнать кратно ли число и сложение цифр числа\n"
          "4)Узнать кратность чисел\n")
    number = int(input())

    if number == 1:
        minVALUE.minimal()
    elif number == 2:
        threeDigit.threeDigit()
    elif number == 3:
        multiple.multiple()
    elif number == 4:
        quotient.quotient()
    else:
        break  
