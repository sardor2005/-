import numpy as np

# Создание двух массивов
A = np.random.randint(1, 10, (3,3))
B = np.random.randint(1, 10, (3,3))

print("Массив A:")
print(A)

print("Массив B:")
print(B)

# Сложение
print("Сложение массивов:")
print(A + B)

# Вычитание
print("Вычитание массивов:")
print(A - B)

# Поэлементное умножение
print("Поэлементное умножение:")
print(A * B)