# Решение квадратных уравнений с повышенной точностью

def get_roots(a, b, c):
    """Return the exact roots of the equation"""
    d = b*b - 4*a*c

    roots = []

    if d >= 0:
        d = d ** 0.5
        if b > 0:
            roots.append((-b - d) * 0.5 / a)
            roots.append(c / (a * roots[0]))
        elif b < 0:
            roots.append((-b + d) * 0.5 / a)
            roots.append(c / (a * roots[0]))
        else:
            roots.append((-c / a) ** 0.5)
            roots.append(-roots[0])

    return roots


def main():
    # input coefficients: ax^2 + bx + c = 0
    print("Input coefficients a, b, c: ")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    roots = get_roots(a, b, c)

    if len(roots) > 0:
        print("Roots of the equations: " + str(roots))
    else:
        print("There are no real roots")


if __name__ == "__main__":
    main()

