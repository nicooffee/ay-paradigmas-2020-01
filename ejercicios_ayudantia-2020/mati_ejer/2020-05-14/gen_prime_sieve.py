# algoritmo con programacion dinamica para generar los primeros n primos
import math , time, itertools

def primeUpperBound(n): # simple limite superior del tamaño del enesimo numero primo
    if n >= 6:          # existen muchas mejores aproximaciones que funcionan en distintos rangos numericos*
        return int(n*(math.log(n) + math.log(math.log(n)))) + 1
    else:
        return n

def primeSieve(np): # implementacion levemente modificada de la criba de aristotenes para encontrar numeros primos
    n=primeUpperBound(np)
    a = [0]*n
    t = int((math.sqrt(4+4*n)-2)//4)
    for i in range(1,t+1):
        u = int((n/2-i)//(1+2*i))
        for j in range(i,u+1):
            a[i + j + 2*i*j] = True
    for i in range(n//2 + 1):
        if not np:
            break
        if not a[i]:
            yield (i*2+1)
            np-=1

count = 0
start_time = time.time()
n = int(input()) # consultar al usuario por el numero de primos a generar
stream = primeSieve(n) # los calculos necesarios se realizan en la inicializacion por lo que es lento inicio pero rapido avance 

#for p in stream: # para imprimir 5 primos por segundo
#    print(p)
#    time.sleep(0.2)

for i in range(n-1): # para imprimir el enesimo primo
    next(stream)
for p in stream:
    print (p)

#for p in itertools.islice(stream, n-1, n): implementacion con itertools para conseguir seccion de los primos
#    print(p)

#for prime in stream: # para conocer cuantos primos se generaron, debiese ser igual a n
#    count += 1
#print(count)
