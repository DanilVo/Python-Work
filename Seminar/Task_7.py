# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

z = 0
x = 1
y = 0
print(not(x and y and z)) == (not x) and (not y) and (not z)