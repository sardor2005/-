import numpy as np

# Создание массива
arr = np.random.randint(1, 20, (3,3))

print("Массив:")
print(arr)

# Сумма элементов
print("Сумма:", np.sum(arr))

# Среднее значение
print("Среднее:", np.mean(arr))

# Минимум и максимум
print("Минимум:", np.min(arr))
print("Максимум:", np.max(arr))