# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

def switch_it_up(number):
    match number:
        case 1:
            print ("one")
        case 2:
            print ("two")
        case 3:
            print ("three")
        case 4:
            print ("four")
        case 5:
            print ("five")
        case 6:
            print ("six")
        case 7:
            print ("seven")
        case 8:
            print ("eight")
        case 9:
            print ("nine")
        case _:
            print ("вы ввели некорректное число, попробуйте 0-9")
number=int(input('введите число от 0-9: '))
print (switch_it_up(number))