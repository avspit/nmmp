import numpy as np
from util import logger

'''
Метод прогонки

A - матрица
B - решения
'''
def solve(A, B):
    logger.log("Начинаем расчет СЛАУ методом прогонки", "", True)

    n = B.size

    # 1. прямой ход
    # вычисление альфы и беты для первой строки матрицы
    b0 = A[0][0]
    c0 = A[0][1]
    d0 = B[0]
    y0 = b0
    alfa0 = -c0 / y0
    beta0 = d0 / y0
    alfas = [alfa0]
    betas = [beta0]
    # вычисление альф и бет для оставшихся строк матрицы
    for i in range(1, n, 1):
        a = A[i][i-1]
        b = A[i][i]
        c = A[i][i+1] if i < n-1 else 0
        d = B[i]
        y = b + a * alfas[i-1]
        alfa = -c / y
        beta = (d - a * betas[i-1]) / y
        alfas.append(alfa)
        betas.append(beta)

    # 2. обратный ход
    # вычисление первого х
    x = [betas[betas.__len__()-1]]
    # вычисление оставшихся х
    for i in range(n-2, -1, -1):
        x.append(alfas[i] * x[n-i-2] + betas[i])
    # переворачиваем список х-ов
    x = np.array(x)[::-1]

    logger.log("Расчет СЛАУ методом прогонки завершен", "", True)

    return x




    # # известные константы
    # k1 = -A[0, 1]
    # m1 = B[0]
    # k2 = -A[A.shape[0] - 1, A.shape[1] - 2]
    # m2 = B[B.shape[0] - 1]
    # alfa = k1
    # beta = m1
    # # поиск alfa и beta
    # c = 2
    # a = 0
    # b = 1
    # alf = [alfa]
    # bet = [beta]
    # for i in range(1, A.shape[0] - 1):
    #     beta = (B[i] - A[i, a] * beta) / (A[i, a] * alfa + A[i, b])
    #     alfa = -A[i, c] / (A[i, a] * alfa + A[i, b])
    #     a += 1
    #     b += 1
    #     c += 1
    #     alf.append(alfa)
    #     bet.append(beta)
    # # расчет y
    # y = (k2 * beta + m2) / (1 - k2 * alfa)
    # otv = [y]
    # for i in range(len(alf) - 1, -1, -1):
    #     y = alf[i] * y + bet[i]
    #     otv.append(y)
    # # переворачиваем значения в списке
    # return np.array(otv)[::-1]




    # n = 10
    # e = np.ones((n, 1), dtype=np.float128)
    # alpha = np.zeros((n - 1, 1))  # коэффициенты в методе прогонки
    # beta = np.zeros((n - 1, 1))  # коэффициенты в методе прогонки
    # # метод прогонки
    # alpha[1] = -A[0][1] / A[0][0]
    # beta[1] = B[0] / A[0][0]
    # # прямой ход
    # for i in range(2, n - 1):
    #     alpha[i] = -A[i - 1][i] / (A[i - 1][i - 1] + alpha[i - 1] * A[i - 1][i - 2])
    #     beta[i] = (B[i - 1] - beta[i - 1] * A[i - 1][i - 2]) / (A[i - 1][i - 1] + alpha[i - 1] * A[i - 1][i - 2])
    # # обратный ход
    # e[n - 2] = (B[i - 2] - beta[n - 2] * A[n - 2][n - 3]) / (A[n - 2][n - 2] + alpha[n - 2] * A[n - 2][n - 3])
    #
    # for i in range(n - 3, 0, -1):
    #     e[i] = alpha[i + 1] * e[i + 1] + beta[i + 1]
    #     # y[i] = v[i]
    # e[0] = alpha[1] * e[1] + beta[1]
    # return e