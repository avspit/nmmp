import matplotlib.pyplot as plt
import nonlinearBoundaryValueProblem as nbvp
import constants.variables as const
import util.logger as logger
import util.util as util

'''
Иксы
'''
def calc_x(h,n):
    x = []
    for i in range(0, n, 1):
        x.append(round(const.a + h * i, 2))
    logger.log('иксы', x)
    return x


if __name__ == '__main__':
    for n in const.n_arr:
        h = util.calc_h(n)
        x = calc_x(h,n)
        y = nbvp.solve(n)
        plt.plot(x, y, label='h='+str(h))
    plt.legend()
    plt.show()

