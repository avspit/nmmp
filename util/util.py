import numpy as np
from scipy.sparse import spdiags
import constants.variables as const
import util.logger as logger


# инициализация иксов
def calc_x(h,n):
    x = []
    for i in range(0, n, 1):
        x.append(round(const.A + h * i, 2))
    logger.log('иксы', x)
    return x


# инициализация h
def init_h(n):
    return (const.B - const.A) / n


# инициализация матрицы А
def init_A(n):
    Avalues = np.array([[-1] * n, [2] * n, [-1] * n])
    Adiags = np.array([-1, 0, 1])
    A = spdiags(Avalues, Adiags, n, n)
    logger.log('Матрица А', A.todense())
    return A.toarray()