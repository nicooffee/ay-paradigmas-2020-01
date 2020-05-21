def exp_stream(s, e, exp): # iterador generico de la forma `range(s,e+1)^exp
    while (s <= e):
        yield s**exp
        s += 1

#fun(x)= 2*x**3 + 3*x**2 + 4
def fun_stream(s, e):
    cuadrado = exp_stream(s, e, 2) # guardamos en cuadrado un generador de cuadrados
    cubo = exp_stream(s, e, 3) # guardamos en cuadrado un generador de cubos
    for gen2 in cuadrado: # iteramos sobre cualquiera de los dos ya que tienen el mismo largo
        gen3 = next(cubo) # iteramos manualmente sobre el otro generador
        yield 2*gen3 + 3*gen2 + 4 # para cada iteracion de exp_stream, se entregara, por lo
                                  # fun_stream termina siendo similar (mismo largo)

for gen in fun_stream(0, 5):
    print(gen)
