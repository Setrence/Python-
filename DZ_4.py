#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

print ('Введите номер четверти: ')
nomerChetverty = int (input ())

if (nomerChetverty == 1):
    print ('X > 0, Y > 0')
elif (nomerChetverty == 4):
    print ('X > 0, Y < 0')
elif (nomerChetverty == 2):
    print ('X < 0, Y > 0')
elif (nomerChetverty == 3):
    print ('X < 0, Y < 0')
else:
    print ('Введена некорректная четверть')