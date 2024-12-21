import cmath

print("\033[42mzd1\033[0m")
"""task1"""
a = [1, 1, 2, 3, 5, 8, 10, 12, 34, 38, 40, 41, 46, 50, 55, 89]
for i in a:
    if i < 15:
        print(i)
  

"""task2"""
print("\033[42mzd2\033[0m")
try:
    a = float(input("введите число:"))
except ValueError:
    print("написано некорректное число")
if a < 0:
    print(f"число {a} отрицательное")
elif a > 0:
    print(f"число {a} положительное")
else:
    print("вы ввели 0")        

"""task3"""
print("\033[42mzd3\033[0m")
print('zd 3')
a = 10
while(a>0):
    print(a)
    a-=1
"""С задержкой (отправляет каждую секунду):"""
print("\033[42mzd3 c zaderzkoy\033[0m")
import time
a = 10
while(a>0):
    print(a)
    a-=1
    time.sleep(1)


"""task4"""
print("\033[42mzd4\033[0m")
print('zd 4')
def solve_quadratic_equation(a, b, c):
    """Решает квадратное уравнение ax^2 + bx + c = 0."""


    if a == 0:
        return None  # Не квадратное уравнение

    delta = (b**2) - 4*(a*c)

    if delta >= 0:  # Реальные корни
        x1 = (-b - delta**0.5) / (2*a)
        x2 = (-b + delta**0.5) / (2*a)
    else:  # Комплексные корни
        x1 = (-b - cmath.sqrt(delta)) / (2 * a)
        x2 = (-b + cmath.sqrt(delta)) / (2 * a)

    return x1, x2


# Пример использования:
a = 1
b = -3
c = 2

roots = solve_quadratic_equation(a, b, c)

if roots is None:
    print("Уравнение не является квадратным.")
else:
    print("Корни уравнения:", roots)


a = 1
b = 2
c = 5

roots = solve_quadratic_equation(a, b, c)

if roots is None:
    print("Уравнение не является квадратным.")
else:
    print("Корни уравнения:", roots)