import matplotlib.pyplot as plt
import nonlinearBoundaryValueProblem as nbvp
import constants.variables as const
import util.logger as logger
import util.util as util


if __name__ == '__main__':
    for n in const.N_ARR:
        h = util.init_h(n)
        logger.log('Начинаем вычисление для h:', str(h), True)
        x = util.calc_x(h,n)
        y = nbvp.solve(n)
        plt.plot(x, y, label='h='+str(h))
        logger.log('Вычисление завершено для h:', str(h), True)
    plt.legend()
    plt.show()

