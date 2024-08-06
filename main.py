# def newton_gregory(x, x_vals, y_vals):
#   """
#   Реализует интерполяцию Ньютона-Грегори.
#
#   Args:
#     x: Точка, в которой вычисляется интерполяционный полином.
#     x_vals: Список значений узлов интерполяции.
#     y_vals: Список значений функции в узлах интерполяции.
#
#   Returns:
#     Значение интерполяционного полинома в точке x.
#   """
#
#   n = len(x_vals)
#   # Вычисление разделенных разностей
#
#   f_vals = y_vals.copy()
#   for k in range(1, n):
#     for i in range(n - k):
#       f_vals[i] = (f_vals[i + 1] - f_vals[i]) / (x_vals[i + k] - x_vals[i])
#
#   # Вычисление интерполяционного полинома
#
#   p = f_vals[0]
#   for k in range(1, n):
#     product = 1.0
#     for i in range(k):
#       product *= (x - x_vals[i])
#     p += product * f_vals[k]
#
#   return p
#
# # Пример использования
#
# x = 1.5
# x_vals = [1.0, 2.0, 3.0]
# y_vals = [2.0, 5.0, 10.0]
#
# y = newton_gregory(x, x_vals, y_vals)
#
#  print(f"Значение интерполяционного полинома в точке {x} = {y}")
import numpy as np

def newton_gregory(x, y, xi):
  """
  Функция интерполяции Ньютона-Грегори

  Args:
    x: массив с исходными значениями аргумента
    y: массив с исходными значениями функции
    xi: точка, в которой вычисляется интерполяция

  Returns:
    значение функции в точке xi
  """

  n = len(x)
  # Вычисление разделенных разностей
  f = np.zeros((n, n))
  for i in range(n):
    f[i, 0] = y[i]

  for i in range(1, n):
    for j in range(n-i):
      f[j, i] = (f[j+1, i-1] - f[j, i-1]) / (x[j+i] - x[j])

  # Вычисление значения интерполяционного многочлена
  p = f[0, 0]
  for i in range(1, n):
    term = f[0, i]
    for j in range(i):
      term *= (xi - x[j])
    p += term

  return p

# Пример использования

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 8, 16, 32])
xi = 3.5

# Вычисление значения интерполяции
y_interp = newton_gregory(x, y, xi)

# График зависимости итогов интерполяции от входящих значений
import matplotlib.pyplot as plt

plt.plot(x, y, 'o-', label='Исходные данные')
plt.plot(xi, y_interp, 'x', label='Интерполяция')
plt.legend()
plt.show()

# Вывод формулы Ньютона-Грегори
# print("Формула Ньютона-Грегори:")
# for i in range(n):
#   term = str(f[0, i])
#   for j in range(i):
#     term += " * (x - " + str(x[j]) + ")"
#   print(" + " + term)

print("Значение в точке x = {}: {}".format(xi, y_interp))