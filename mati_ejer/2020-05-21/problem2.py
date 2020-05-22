matriz1 = [
    [0,0,0,0,0,0],
    [1,1,0,0,0,0],
    [0,0,0,1,0,0],
    [0,0,0,1,0,0],
    [0,0,0,1,0,0],
    [0,0,0,1,0,0]]

matriz2 = [
    [0,0,0,0,0,0],
    [1,1,1,0,0,0],
    [0,0,1,0,1,0],
    [0,0,1,0,1,0],
    [0,0,0,0,0,1],
    [0,0,0,0,0,0]]

def recorrer(M, y, x):
    recorrido = []
    ultimos = [[y,x]]
    height = len(M)
    width = len(M[0])
    yield y,x
    while True:
        if (y+1 < height and x+1 < width) and M[y+1][x+1]==0:
            y += 1
            x += 1
        elif (x+1 < width) and M[y][x+1]==0:
            x += 1
        elif (y+1 < height) and M[y+1][x]==0:
            y += 1
        else:
            yield -1,0
            break
        yield y,x
        if y==height-1 and x==width-1:
            yield 0,-1
            break

for par in recorrer(matriz1, 0, 0):
    y,x = par
    if (y==-1):
        print("no se llega a el final!")
        break
    if (x==-1):
        print("se llego a el final!")
        break
    print("(%d,%d)"% (y, x))

for par in recorrer(matriz2, 0, 0):
    y,x = par
    if (y==-1):
        print("no se llega a el final!")
        break
    if (x==-1):
        print("se llego a el final!")
        break
    print("(%d,%d)"% (y, x))
                
            
