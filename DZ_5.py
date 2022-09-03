#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

import math

print ('Введите координаты точки A : ')
x1 = int (input ('x = '))
y1 = int (input ('y = '))
print ('Введите координаты точки B : ')
x2 = int (input ('x = '))
y2 = int (input ('y = '))

rastoyanie = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print (f'Растояние = {rastoyanie}')