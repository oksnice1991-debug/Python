import math


def square(s):
    area = s * s
    return math.ceil(area)


s = float(input("Введите сторону квадрата: "))
result = square(s)
print(f"Площадь квадрата: {result}")
