import numpy as np
import constants.variables as const
import tridiagonalMatrixAlgorithm as tma
import util.logger as logger
import util.util as util


#правая часть уравнения
def g(h, i, x):
    return 3*x + pow(i,2) * pow(h,2) + 10*pow(x,3)
    #return 3 * x + 1 + 10 * pow(x,3)

#производная правой части уравнения
def dg(x):
    return 3 + 30*pow(x,2)



# alpha = np.zeros((n - 1, 1))  # коэффициенты в методе прогонки
# beta = np.zeros((n - 1, 1))  # коэффициенты в методе прогонки

'''
Метод конечных разностей
'''
def solve(n):
    H = np.zeros((n, 1), dtype=np.float128)  # вектор правых частей
    dH = np.zeros((n, n), dtype=np.float128)  # якобиан правой части

    y = np.zeros((n, 1), dtype=np.float128)
    e = np.ones((n, 1), dtype=np.float128)
    v = np.zeros((n, 1), dtype=np.float128)  # вектор-решение метода прогонки
    y[0] = 0
    y[v.size - 1] = n

    A = util.init_A(n)

    h = util.init_h(n)

    # Метод Ньютона
    while np.max(abs(e)) > const.stop_value:

        for i in range(0, n, 1):
            H[i] = pow(h,2) * g(h, i, v[i]) #вектор правых частей
            dH[i][i] = 2 + pow(h,2) * dg(v[i]) #якобиан правой части
        logger.log('H', H)
        logger.log('dH', dH)

        L = (A.toarray() + dH ) #* y  # левая часть в методе ньютона
        R = -1 * (np.dot(A.toarray(), v) + H)  # правая часть в методе ньютона
        logger.log('L', L)
        logger.log('R', R)

        e = tma.solve(L, R)
        logger.log('e', e)

        if np.isinf(np.max(abs(e))) or np.isnan(np.max(abs(e))):
            break

        v = v + e
        logger.log('v', v)


    for i in range(1,n):
        y[i] = v[i-1]
    logger.log('y', y)

    return y


