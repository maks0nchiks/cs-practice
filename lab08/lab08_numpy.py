import numpy as np


# Задание 1. Создание векторов и матриц

hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=np.int32)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("Задание 1")

print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)

print("line:", line)
print("zeros:", zeros)
print("unknown_table:\n", unknown_table)
print("identity:\n", identity)


# Задание 2. Индексы и срезы в векторе

print("\nЗадание 2")

print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2–5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("Обратный порядок:", hours[::-1])


# Задание 3. Строки и столбцы таблицы

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("\nЗадание 3")

print("Форма:", temperatures.shape)
print("Число измерений:", temperatures.ndim)
print("Число элементов:", temperatures.size)

print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:")
print(temperatures[:2, 1:])

print("Центральный фрагмент 2x2:")
print(temperatures[:2, 1:3])


# Задание 4. Прямоугольные срезы

matrix = np.arange(1, 26).reshape(5, 5)

matrix_f3r = matrix[:3, :]
matrix_l2r = matrix[-2:, :]
matrix_f2c = matrix[:, :2]
matrix_frag = matrix[1:4, 2:5]
matrix_angle = matrix[-2:, -2:]

print("\nЗадание 4")

print("Первые три строки:")
print(matrix_f3r)
print("Форма:", matrix_f3r.shape)

print("Последние две строки:")
print(matrix_l2r)
print("Форма:", matrix_l2r.shape)

print("Первые два столбца:")
print(matrix_f2c)
print("Форма:", matrix_f2c.shape)

print("Фрагмент строк 1–3 и столбцов 2–4:")
print(matrix_frag)
print("Форма:", matrix_frag.shape)

print("Правый нижний блок 2x2:")
print(matrix_angle)
print("Форма:", matrix_angle.shape)


# Задание 5. Изменение массива с помощью срезов

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

changed_hours = hours.copy()

changed_hours[2:5] = 99
changed_hours[1::2] = -1

print("\nЗадание 5")

print("Изменённый hours:", changed_hours)
print("Исходный hours:", hours)

# .copy() нужен, чтобы изменения не затрагивали исходный массив.

changed_matrix = matrix.copy()

changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print("Изменённая матрица:")
print(changed_matrix)

print("Исходная матрица:")
print(matrix)


# Задание 6. Изменение формы

numbers = np.arange(0, 12)
table = numbers.reshape(3, 4)
transposed = table.T

print("\nЗадание 6")

print("numbers:")
print(numbers)
print("Форма:", numbers.shape)

print("table:")
print(table)
print("Форма:", table.shape)

print("transposed:")
print(transposed)
print("Форма:", transposed.shape)

# reshape(3, 4) работает, потому что 3 * 4 = 12.
# reshape(5, 3) вызовет ошибку, потому что 5 * 3 = 15,
# а в исходном массиве только 12 элементов.