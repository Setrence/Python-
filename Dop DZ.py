#Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
#a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
#Требуется найти N-е число Фибоначчи.

n = int (input ('N = '))
a = 0
k = 3
b = 2
c = 1

if (n < 0 or n > 30):
    print ('Введите число от 0 до 30')
elif (n == 0):
    print ('a = 0')
elif (n == 1):
    print ('a = 1')
else:
    while (k != n):
        a = b + c
        c = b
        b = a
        k = k + 1
    print (f'{a}')
