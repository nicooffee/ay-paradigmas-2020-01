import time

def lista(N):
    L = []
    for x in range(N):
        L.append(x)
    return L

def lista_yield(N):
    for x in range(N):
        yield x


print(lista(10))

print(lista_yield(10))

Generador = lista_yield(10)

#0 1 2 3 4 5 6 7 8 9
for x in Generador:
    print(x)

Generador_2 = lista_yield(15)

print( list(Generador_2) )

#generador infinito
def generador_infinito_inef():
    x = 0
    while True:
        yield 2**x
        x += 1

def generador_infinito_ef():
    x = 1
    while True:
        yield x
        x = x*2

generador_3 = generador_infinito_ef()

for x in generador_3:
    print(x)
    time.sleep(1)