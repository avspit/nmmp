import numpy as np
from scipy.sparse import spdiags
import constants.variables as const
import util.logger as logger

# h
def init_h(n):
    return (const.b - const.a) / n

# Матрица А
def init_A(n):
    An = n
    Avalues = np.array([[-1] * An, [2] * An, [-1] * An], dtype=np.float128)
    Adiags = np.array([-1, 0, 1], dtype=np.float128)
    A = spdiags(Avalues, Adiags, An, An)
    logger.log('Матрица А', A.todense())
    return A