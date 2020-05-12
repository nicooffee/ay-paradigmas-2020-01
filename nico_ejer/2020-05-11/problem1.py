
def bloques(g, key):
    b = [] # el bloque
    for x in g: 
        if len(b) == 0 or key(b[-1]) <= key(x):
            b.append(x)
        else:
            yield b
            b = [x]
    if len(b)>0:
        yield b

g = [1,5,6,4,8,9,2,3,7]

it = bloques(g,lambda x: x)

print(list(it))