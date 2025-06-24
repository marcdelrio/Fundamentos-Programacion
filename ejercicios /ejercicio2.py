try:
    lista = [n / n for n in range (3)]
except ArithmeticError:
    print('Error: error matemático')
except:
    print('Error desconocido')