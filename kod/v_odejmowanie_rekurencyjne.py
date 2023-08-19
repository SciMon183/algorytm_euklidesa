# NWD z odejmowaniem rekurencyjnym 

def NWD(a, b):
    if a != b:
        if a > b:
            return NWD(a - b, a)
        else: 
            return NWD(a, b - a)
    return a

a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))

print("NWD wynosi: ", NWD(a, b))