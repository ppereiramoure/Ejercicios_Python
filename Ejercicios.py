# 7.1
l = (1, 2, 3, 4)
l2 = (4, 3, 2, 1)


def orden(lista):
    if lista[0] > lista[1]:
        return "De mayor a menor"
    else:
        return "De menor a mayor"


print(orden(l))

# 7.2
l = (3, 4)
l2 = (5, 4)


# 1 corregir recorriendo la lista
def encaja1(lista1, lista2):
    if lista1[1] == lista2[0] or lista1[1] == lista2[1]:
        return "encaja"
    else:
        return "no encaja"


print(encaja1(l, l2))

# 2
l3 = "3-4"
l4 = "2-5"


def encaja2(ls1, ls2):
    lista1 = ls1.split()
    lista2 = ls2.split()

    if lista1 == lista2[0] or lista1[1] == lista2[1]:
        return "encaja"
    else:
        return "no encaja"


print(encaja2(l3, l4))

# 7.3
# 1
lNombres=("Pablo","Sol","Sofia","Eli","Jesus")


def estimadoUsuario(lista):
    for n in lista:
        print("Estimado "+n)

estimadoUsuario(lNombres)
#2
def estimadoUsuarioPosicion(lista,posicion,cantidad):
    num=0
    for n in lista[posicion:]:
        while num <cantidad:
           print("Estimado "+n)
            num=num+1

estimadoUsuarioPosicion(lNombres,1,2)

# 7.5
listaEnteros=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)

def primos(listaNumeros):
    listaPrimos=[]
    for l in listaNumeros:
        if l < 1:
            return False
        elif l==2:
            listaPrimos.append(l)
        else:
            for n in range(2, l):
                if l % n ==0:
                    return False
            listaPrimos.append(l)
    print(listaPrimos)
primos(listaEnteros)
