# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

def maximum(list1):
    maxim=-10000
    for i in list1:
        if i >= maxim:
           maxim=i
    return maxim

def minimum(list1):
    minim=10000
    for i in list1:
        if i <= minim:
            minim=i
    return minim        
list1=[]
x=int(input('введите кол-во элементов списка: '))
d=0
while d<x:
   pp=int(input())
   list1.append(pp)
   d+=1
print("максимальное число=",maximum(list1), "минимальное число=",minimum(list1))