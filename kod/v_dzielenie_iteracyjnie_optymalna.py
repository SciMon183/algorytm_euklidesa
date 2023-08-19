# NWD dzilenei iteracyjne z opytmalizacją 

def NWD(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))

print(NWD(a, b))