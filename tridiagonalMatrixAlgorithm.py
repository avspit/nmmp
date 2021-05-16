import numpy as np

'''
Метод прогонки

A - матрица
B - решения
'''
def solve(A, B):
    # известные константы
    k1 = -A[0, 1]
    m1 = B[0]
    k2 = -A[A.shape[0] - 1, A.shape[1] - 2]
    m2 = B[B.shape[0] - 1]
    alfa = k1
    beta = m1
    # поиск alfa и beta
    c = 2
    a = 0
    b = 1
    alf = [alfa]
    bet = [beta]
    for i in range(1, A.shape[0] - 1):
        beta = (B[i] - A[i, a] * beta) / (A[i, a] * alfa + A[i, b])
        alfa = -A[i, c] / (A[i, a] * alfa + A[i, b])
        a += 1
        b += 1
        c += 1
        alf.append(alfa)
        bet.append(beta)
    # расчет y
    y = (k2 * beta + m2) / (1 - k2 * alfa)
    otv = [y]
    for i in range(len(alf) - 1, -1, -1):
        y = alf[i] * y + bet[i]
        otv.append(y)
    # переворачиваем значения в списке
    return np.array(otv)[::-1]


    # # метод прогонки
    # alpha[1] = -L[0][1] / L[0][0]
    # beta[1] = R[0] / L[0][0]
    # # прямой ход
    # for i in range(2, n - 1):
    #     alpha[i] = -L[i - 1][i] / (L[i - 1][i - 1] + alpha[i - 1] * L[i - 1][i - 2])
    #     beta[i] = (R[i - 1] - beta[i - 1] * L[i - 1][i - 2]) / (L[i - 1][i - 1] + alpha[i - 1] * L[i - 1][i - 2])
    # # обратный ход
    # e[n - 2] = (R[i - 2] - beta[n - 2] * L[n - 2][n - 3]) / (L[n - 2][n - 2] + alpha[n - 2] * L[n - 2][n - 3])
    #
    # for i in range(n - 3, 0, -1):
    #     e[i] = alpha[i + 1] * e[i + 1] + beta[i + 1]
    #     # y[i] = v[i]
    # e[0] = alpha[1] * v[1] + beta[1]