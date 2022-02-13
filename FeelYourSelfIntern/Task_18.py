# Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y

x = 1
y = 0
print(not (x and y)) == (not x) and (not y)