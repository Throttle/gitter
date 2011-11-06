# -*- coding: utf-8 -*-

# develop version

def reverse_numeric(x, y):
        return y - x

min = int(raw_input("Input minimal limit:"))
max = int(raw_input("Input maximal limit:"))
a = [0] * (max) # создание массива с n количеством элементов
for i in range(max): # заполнение массива ...
    a[i] = i # значениями от 0 до n-1
 
# вторым элементом является единица, которую не считают простым числом
# забиваем ее нулем.
numb_arr[1] = 0
 
m = 2 # замена на 0 начинается с 3-го элемента (первые два уже нули)
while m < max: # перебор всех элементов до заданного числа
    if a[m] != 0: # если он не равен нулю, то
        j = m * 2 # увеличить в два раза (текущий элемент простое число)
        while j < max:
            a[j] = 0 # заменить на 0
            j +=  m # перейти в позицию на m больше
    m += 1
 
# вывод простых чисел на экран (может быть реализован как угодно)
b = []
for i in a:
    if a[i] != 0 and a[i] > min:
        b.append(a[i])
 
del a
print (sorted(b, cmp=reverse_numeric))
