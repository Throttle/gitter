# -*- coding: utf-8 -*-

# develop version

def reverse_numeric(x, y):
        return y - x

min = int(raw_input("Input minimal limit:"))
max = int(raw_input("Input maximal limit:"))
a = [0] * (max) # �������� ������� � n ����������� ���������
for i in range(max): # ���������� ������� ...
    a[i] = i # ���������� �� 0 �� n-1
 
# ������ ��������� �������� �������, ������� �� ������� ������� ������
# �������� �� �����.
numb_arr[1] = 0
 
m = 2 # ������ �� 0 ���������� � 3-�� �������� (������ ��� ��� ����)
while m < max: # ������� ���� ��������� �� ��������� �����
    if a[m] != 0: # ���� �� �� ����� ����, ��
        j = m * 2 # ��������� � ��� ���� (������� ������� ������� �����)
        while j < max:
            a[j] = 0 # �������� �� 0
            j +=  m # ������� � ������� �� m ������
    m += 1
 
# ����� ������� ����� �� ����� (����� ���� ���������� ��� ������)
b = []
for i in a:
    if a[i] != 0 and a[i] > min:
        b.append(a[i])
 
del a
print (sorted(b, cmp=reverse_numeric))