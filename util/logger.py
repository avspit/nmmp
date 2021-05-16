import constants.variables as const

def log(text, value, print_anyway):
    if const.log or print_anyway:
        print(text)
        print(value)
        print('')