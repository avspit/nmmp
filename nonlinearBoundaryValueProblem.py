import numpy as np
import constants.variables as const
import tridiagonalMatrixAlgorithm as tma
import util.logger as logger
import util.util as util


# g(x)
def g(h, i, x):
    return 3*x + pow(i+1,2) * pow(h,2) + 10*pow(x,3)


# производная g(x)
def dg(x):
    return 3 + 30*pow(x,2)


# метод Ньютона
def solve(n):
    H = np.zeros((n, 1)) # вектор-функция H
    dH = np.zeros((n, n)) # вектор-функция производных значений H
    k = np.ones((n, 1))  # вектор-решение метода прогонки, является y(k)
    v = np.zeros((n, 1))  # вектор-решение шага 2 метода Ньютона
    A = util.init_A(n)  # матрица А
    h = util.init_h(n)  # h
    y = np.zeros((n, 1)) # результат решения методом Ньютона, игрики

    logger.log("Начинаем итерации методом Ньютона", "", True)
    while np.max(abs(k)) > const.STOP_VALUE:

        # Шаг 1
        for i in range(0, n, 1):
            H[i] = pow(h,2) * g(h, i, v[i])
            dH[i][i] = pow(h,2) * dg(v[i])
        logger.log('H', H)
        logger.log('dH', dH)

        L = (A + dH ) # * k # метод Ньютона, левая часть
        R = -1 * (np.dot(A, v) + H)  # метод Ньютона, правая часть
        logger.log('L', L)
        logger.log('R', R)

        # вычисление вектора-решения методом прогонки
        k = tma.solve(L, R)
        logger.log('k', k, True)

        #if np.isinf(np.max(abs(k))) or np.isnan(np.max(abs(k))):
        #    break

        # Шаг 2
        v = v + k
        logger.log('v', v, True)

    # заполняем y
    for i in range(1, n, 1):
        y[i] = v[i-1]
    logger.log('y', y)

    return y


