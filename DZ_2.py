#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print ('Введите числа X, Y, Z : ')
X = int (input ())
Y = int (input ())
Z = int (input ())
if (not (X or Y or Z) == (not X and not Y and not Z)):
    print ('Утверждение истинно')
else:
    print ('Утверждение ложно')
