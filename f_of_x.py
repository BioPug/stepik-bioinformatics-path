"""
    Вычисляет кусочную функцию f(x):

        { 1 - (x + 2)^2,   при x <= -2
    f(x) = { -x^2,          при -2 < x <= 2
        { (x - 2)^2 + 1,  при x > 2

    Возвращает значение f(x).
"""

def f(x):
    if x <= -2:
        return 1-((x+2)**2)
    elif -2 < x <= 2:
        return -x/2
    elif 2 < x:
        return ((x-2)**2)+1
    return None
print(f(float(input())))