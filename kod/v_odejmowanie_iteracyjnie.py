# NWD z odejmowaniem iteracyjnym 

def NWD(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

a = int(input('Podaj liczbę a: '))
b = int(input('Podaj liczbę b: '))

print('NWD wynosi: ', NWD(a, b))