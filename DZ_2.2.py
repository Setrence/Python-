#Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.
#В единственной строке входного файла INPUT.TXT записано единственное целое число N, не превышающее по абсолютной величине 10^4.
#В единственную строку выходного файла OUTPUT.TXT нужно вывести одно целое число — сумму чисел, расположенных между 1 и N включительно.

n = int (input ('Введите число N: '))
i = 0
k = 0
if (n > 10**4 or n < 1):
    print ('Введите число от 1 до 10^4')
else:
    while (i <= n):
        k += i
        i = i + 1
print (f'Сумма целых чисел = {k}')
