def function(x):
    """Returns the value of the function F(x)"""
    return x * x + 4 * x - 1/4


def dichotomy(a, b, e, d):
    """Find the minimum value of the function on the segment [a, b]"""
    flag = True
    step = 0

    print("Метод дихотомии")

    while flag:
        # выбираем 2 точки ~ по центру
        u1 = (a + b - d) / 2
        u2 = (a + b + d) / 2

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
    print("Минимальное значение: F(x)" + str(minimum))


def main():
    # call the dichotomy method and set the parameters:
    # section [a, b], epsilon accuracy e and d
    dichotomy(-2, 8, 0.5, 0.2)


if __name__ == "__main__":
    main()



