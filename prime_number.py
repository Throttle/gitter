# -*- coding: utf-8 -*-
# First release version

def reverse_numeric(x, y):
        return y - x
		
inputCount = int(raw_input("Input count numbers to check:"))
counter = 0
checkNumbers = []
while (counter < inputCount)
	checkNumbers.append(raw_input("Input number"+str(counter)+">>>"))
	print counter, checkNumbers[counter]
	counter++
		
min = int(raw_input("Input minimal limit:"))
max = int(raw_input("Input maximal limit:"))
a = [0] * (max) # создание массива с n количеством элементов
for i in range(max): # заполнение массива ...
    a[i] = i  # значениями от 0 до n-1
	print a[i]
	print 'square number = ', a[i]*a[i]
 
# вторым элементом является единица, которую не считают простым числом
# забиваем ее нулем.

m = 2 # замена на 0 начинается с 3-го элемента (первые два уже нули)
while m < max: # перебор всех элементов до заданного числа
    if a[m] != 0: # если он не равен нулю, то
        j = m + m # увеличить в два раза (текущий элемент простое число)
        while j < max:
            a[j] = 0 # заменить на 0
            j = j + m # перейти в позицию на m больше
    m += 1
	
#test print 
print a
 
# вывод простых чисел на экран (может быть реализован как угодно)
b = []
for i in a:
    if a[i] != 0 and a[i] > min:
        b.append(a[i])
 
del a
print (sorted(b, cmp=reverse_numeric))

filename = "test.dat"
FILE = open(filename,"w")
# Write all the lines at once:
FILE.writelines(b)
FILE.close()
