# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

def quarter_of(number):
    match number:
        case 1:
            print ("Месяц ", number, "(январь) является частью первого квартала")
        case 2:
            print ("Месяц ", number, "(февраль) является частью первого квартала")
        case 3:
            print ("Месяц ", number, "(март) является частью первого квартала")
        case 4:
            print ("Месяц ", number, "(апрель) является частью второго квартала")
        case 5:
            print ("Месяц ", number, "(май) является частью второго квартала")
        case 6:
            print ("Месяц ", number, "(июнь) является частью второго квартала")
        case 7:
            print ("Месяц ", number, "(июль) является частью третьего квартала")
        case 8:
            print ("Месяц ", number, "(август) является частью третьего квартала")
        case 9:
            print ("Месяц ", number, "(сентябрь) является частью третьего квартала")
        case 10:
            print ("Месяц ", number, "(октябрь) является частью 4 квартала")
        case 11:
            print ("Месяц ", number, "(ноябрь) является частью 4 квартала")
        case 12:
            print ("Месяц ", number, "(декабрь) является частью 4 квартала")
        case _:
            print ("вы ввели некорректное число, попробуйте 1-12")
number=int(input("введите номер месяца: "))
print (quarter_of(number))