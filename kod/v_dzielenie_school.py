# NWD wersja dzielenie mocno szkolna 

def NWD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else: 
            b = b % a
        
        if a != 0:
            return a
        else:
            return b

a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))

print(NWD(a, b))