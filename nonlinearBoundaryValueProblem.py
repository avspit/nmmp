import numpy as np
import constants.variables as const
import tridiagonalMatrixAlgorithm as tma
import util.logger as logger
import util.util as util


#правая часть уравнения
def g(h, i, x):
    return 3 * x + pow(h, 2) + 10 * pow(x, 3)
    #return 3*x + pow(i,2) * pow(h,2) + 10*pow(x,3)
    #return 3 * x + 1 + 10 * pow(x,3)

#производная правой части уравнения
def dg(x):
    return 3 + 30*pow(x,2)





# метод Ньютона
def solve(n):
    H = np.zeros((n, 1), dtype=np.float128)  # вектор правых частей
    dH = np.zeros((n, n), dtype=np.float128)  # якобиан правой части

    y = np.zeros((n, 1), dtype=np.float128)
    k = np.ones((n, 1), dtype=np.float128) # вектор-решение метода прогонки, является y(k)
    v = np.zeros((n, 1), dtype=np.float128)  # вектор-решение шага 2 метода Ньютона
    y[0] = 0
    y[v.size - 1] = n

    A = util.init_A(n)

    h = util.init_h(n)

    logger.log("Начинаем итерации методом Ньютона", "", True)
    while np.max(abs(k)) > const.stop_value:

        for i in range(0, n, 1):
            H[i] = pow(h,2) * g(h, i, v[i]) #вектор правых частей
            dH[i][i] = pow(h,2) * dg(v[i]) #якобиан правой части
        logger.log('H', H, False)
        logger.log('dH', dH, False)

        L = (A.toarray() + dH ) * k # левая часть в методе ньютона
        R = -1 * (np.dot(A.toarray(), v) + H)  # правая часть в методе ньютона
        logger.log('L', L, False)
        logger.log('R', R, False)

        #k = tma.solve(np.squeeze(np.asarray(np.matrix('2 -1 0; 5 4 2; 0 1 -3'))),np.array([3,6,2]))
        #logger.log('k', k, False)
        #break

        k = tma.solve(L, R)
        logger.log('k', k, True)

        #if np.isinf(np.max(abs(k))) or np.isnan(np.max(abs(k))):
        #    break

        v = v + k
        logger.log('v', v, True)



    for i in range(1,n):
        y[i] = v[i-1]
    logger.log('y', y, False)

    return y


