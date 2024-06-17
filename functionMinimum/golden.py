import math


def function(x):
    """Returns the value of the function F(x)"""
    return x * x + 4 * x - 1/4


def golden(a, b, e):
    """Поиск минимального значения функции по методу золотого сечения"""
    flag = True
    step = 0

    print("Метод золотого сечения")

    while flag:
        # выбираем 2 точки
        u1 = a + 0.382 * (b - a)
        u2 = b - 0.382 * (b - a)

        step += 1

        print(str(step) + " Шаг ")
        print("Отрезок [" + str(a) + "; " + str(b) + "]")

        # теперь проверяем, в какой точке значение больше
        # определяем новый отрезок [a, b]
        if function(u1) > function(u2):
            a = u1
        else:
            b = u2

        # проверяем, не нужно ли остановиться
        if (b - a) < e:
            minimum = function((a + b) / 2)
            flag = False

        # Выводы для наглядности

        print("Две точки: u1 = " + str(u1) + ", u2 = " + str(u2))
        print("F(u1) = " + str(function(u1)) + ", F(u2) = " + str(function(u2)))
        print("Новый отрезок [" + str(a) + "; " + str(b) + "]")
        print()

    print("Точка минимума: x = " + str((a + b) / 2))
    print("Минимальное значение: " + str(minimum))


def main():
    # call the golden method and set the parameters:
    # section [a, b] and epsilon accuracy e
    golden(-2, 8, 0.5)


if __name__ == "__main__":
    main()