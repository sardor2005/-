import numpy as np

# Создание массива 5x5
arr = np.random.randint(1, 20, (5,5))

print("Массив 5x5:")
print(arr)

# Элемент (2,3)
print("Элемент (2,3):")
print(arr[2,3])

# Первый столбец
print("Первый столбец:")
print(arr[:,0])

# Элементы (1,1), (2,2), (3,3)
print("Диагональные элементы:")
print([arr[1,1], arr[2,2], arr[3,3]])