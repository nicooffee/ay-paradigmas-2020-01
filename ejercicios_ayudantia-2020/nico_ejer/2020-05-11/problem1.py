# g en alguna parte tiene un yield
#key: function(x) -> y
#ej: key: (lambda x: -x)

#key(g_1)<=key(g_2) ? 
#key: (lambda x: x)
def bloques(g,key):
    bloque = []
    for elemento in g: 
        #bloque[0] -> bloque[-1] = bloque[len(bloque) - 1]
        #me va a generar un bloque hasta que se rompa la condición
        if len(bloque) == 0 or key(bloque[-1])<=key(elemento):
            bloque.append(elemento)
        else:
            yield bloque
            bloque = [elemento] # [4]
    #si existe un bloque restante === len(bloque)>0
    if len(bloque)>0:
        yield bloque

g = [1,5,6,4,8,9,2,3,7]
key = (lambda x: x)
print( list( bloques( g,key) ) )
#actual bloque: [1,5,6]
#6 <= 4
#genero [1,5,6]
#empiezo con nuevo bloque: [4]
#...
#[2,3] -> 3 <= 7
#nuevo bloque: [2,3,7]
#