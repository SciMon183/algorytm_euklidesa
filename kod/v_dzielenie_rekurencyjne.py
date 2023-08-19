# NWD dzielenie rekurencyjne 

def NWD(a, b):
    if b:
        return NWD(b, a%b)
    return a

a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))

print(NWD(a, b))