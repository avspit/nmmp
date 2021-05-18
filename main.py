import matplotlib.pyplot as plt
import nonlinearBoundaryValueProblem as nbvp
import constants.variables as const
import utils.logger as logger
import utils.util as util
import numpy as np
from scipy.interpolate import splrep, splev


if __name__ == '__main__':
    for n in const.N_ARR:
        h = util.init_h(n)
        logger.log(text='Начинаем вычисление для h:', value=str(h), force=True)
        x = util.calc_x(h,n)
        y = nbvp.solve(n)
        # Сделаем график более гладким с помощью сплайн-фитинга
        tck = splrep(x, y)
        xnew = np.linspace(x[0], x[-1])
        ynew = splev(xnew, tck)
        # Нарисуем график
        plt.plot(xnew, ynew, label='h='+str(h))
        logger.log(text='Вычисление завершено для h:', value=str(h), force=True)
    plt.legend()
    plt.show()

