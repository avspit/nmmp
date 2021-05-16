import constants.variables as const

# функция логирования данных в консоль
def log(text, value="", print_anyway=False):
    if const.LOG or print_anyway:
        print(text)
        print(value)
        print('')