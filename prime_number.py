﻿# -*- coding: utf-8 -*-
# We are fighting with git
# It's a simple test

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
a = [0] * (max) # �������� ������� � n ����������� ���������
for i in range(max): # ���������� ������� ...
    a[i] = i # ���������� �� 0 �� n-1
	print a[i]
	print 'square number = ', a[i]*a[i]
 
# ������ ��������� �������� �������, ������� �� ������� ������� ������
# �������� �� �����.

m = 2 # ������ �� 0 ���������� � 3-�� �������� (������ ��� ��� ����)
while m < max: # ������� ���� ��������� �� ��������� �����
    if a[m] != 0: # ���� �� �� ����� ����, ��
        j = m + m # ��������� � ��� ���� (������� ������� ������� �����)
        while j <= max:
            a[j] = 0 # �������� �� 0
            j = j + m # ������� � ������� �� m ������
    m += 1
	
#test print 
print a
 
# ����� ������� ����� �� ����� (����� ���� ���������� ��� ������)
b = []
for i in a:
    if a[i] != 0 and a[i] > min:
        b.append(a[i])
 
del a
print (sorted(b, cmp=reverse_numeric))
print "pumpumpum"
print "pampam"
