import math
import numpy as np


def f(x):
    # наша функция
    return x ** 2 + (-1) * x * 14 + 1

def minimize_parabolic(a, b, epsilon=0.1):
    # Этап 2

    k = 0 # Инициализируем счётчик итераций.


    # Выбор точек x1, x2, x3 из интервала [a,b] при условие f(x1)≥f(x2)≤f(x3)

    x1 = np.random.randint(a, b)
    x2 = np.random.randint(a, b)
    x3 = np.random.randint(a, b)


    while f(x1) < f(x2) < f(x2):
        x1 = np.random.randint(a, b)
        x2 = np.random.randint(a, b)
        x3 = np.random.randint(a, b)

    print(x1, x2, x3)
    print(f(x1), f(x2), f(x3))

    # if f(x1) < f(x2) or f(x3) < f(x2):
    #     raise ValueError("Initial condition f(x1) >= f(x2) <= f(x3) is not satisfied.")

    '''
    ЭТАП 2  
    '''

    while True:

        # Вычисляем a1 и a2
        a1 = x1/x2 # Находим a1
        a2 = x2/x3 #!!! Нужны формулы для вычисления a2

        print(a1, a2)

        x_tilde= 0.5 * (x1 + x2 - a1 / a2) #  # Находим x~

        # Если k !=0 то к этапу 3
        if k != 0:

            # Этап 3
            if abs(x_tilde - xk_minus_1) <= epsilon: # Если абсолютное значение <= e, иначе переходим к этапу 4
                x_star = x_tilde
                f_x_star = f(x_tilde) #fx*
                break

        k += 1

        if k == 0:
            xk_minus_1 = x2
        else:
            xk_minus_1 = x_tilde

        # Этап 4
        # a)
        if x1 < x_tilde < x2 < x3 and f(x2) < f(x_tilde):
            x1 = x_tilde

        # б)
        elif x1 < x_tilde < x2 < x3 and f(x2) > f(x_tilde):
            x3 = x2
            x2 = x_tilde

        # в)
        elif x1 < x2 < x_tilde < x3 and f(x2) > f(x_tilde):
            x1 = x2
            x2 = x_tilde

        # г)
        elif x1 < x2 < x_tilde < x3 and f(x2) < f(x_tilde):
            x3 = x_tilde

        # д)
        elif x2==x_tilde:
            x2 = (x1 + x2) / 2

        # е)
            elif f(x2) == x_tilde:
            x2 = (x1 + x2) / 2


    return x_star, f_x_star


# Пример использования
a = 1
b = 10
epsilon = 0,1
x_star, f_x_star = minimize_parabolic(a, b, epsilon)
print(f"Minimum at x = {x_star}, f(x) = {f_x_star}")