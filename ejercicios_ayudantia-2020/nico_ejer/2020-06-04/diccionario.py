dic_celdas_visitas = {}

#(1,1)


x,y = 5,5

#visite la celda 5,5
key = "{},{}".format(x,y)
print("Key = "+key)

#marco que ya visite 5,5
dic_celdas_visitas[key] = True

# visité la celda 5,5?

if key in dic_celdas_visitas.keys() and dic_celdas_visitas[key] == True:
    print("ya la visite")

dic_celdas_visitas['5,6'] = True
dic_celdas_visitas['6,6'] = True
print(dic_celdas_visitas)

print(dic_celdas_visitas['5,6'])


#funcion que comprueba si (i,j) esta dentro de los límites de M
def esta_dentro(M,i,j):
    pass #True o False dependiendo de si (i,j) esta dentro de los limites de M

def adyacentes(x,y):
    Ad = []
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if i!= 0 or j!=0 :
                Ad.append((i+x,j+y))
    return Ad

#5,5
print(adyacentes(x,y))