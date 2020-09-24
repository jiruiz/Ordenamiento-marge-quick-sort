'''
Ejercicio 20.7.2. Mostrar los pasos del ordenamiento de la lista: 6 0 3 2 5 7 4 1 con los métodos
de inserción y con merge sort. ¿Cuáles son las principales diferencias entre los métodos?
¿Cuál usarías en qué casos?

'''
listaEntrada = [6,0,3,2,5,7,4,1]
# listaOrdenada = [-1, 3, 4, 5, 6, 7]

#O(n2)
def orden_insercion(lista):
    for i in range(len(lista) -1): # N
        if lista[i+1] < lista[i]:
            reubicar(lista, i+1)
        print("DEBUG: ", lista)

def reubicar(lista, pos):
    valorPos = lista[pos]
    posOrig = pos
    print(f" valor es {valorPos} para la posicion {posOrig}")
    print(f"{lista[posOrig - 1]}")
    while posOrig > 0 and valorPos < lista[posOrig - 1]: #N

        lista[posOrig] = lista[posOrig - 1]
        print(f" {posOrig} es ahora {lista[posOrig]}")
        posOrig -= 1

    lista[posOrig] = valorPos

orden_insercion(listaEntrada)
print("*************************************")
print("*************************************")
print("*************************************")

def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
    Pre: lista debe contener elementos comparables.
    Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        #print("devuelve lista porque len < 2")
        return lista
    medio = len(lista) // 2
    #print("hola soy merge sort")
    izq = merge_sort(lista[:medio])
    #print("izq")
    der = merge_sort(lista[medio:])
    #print("derecho")

    return merge(izq, der)

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
    Pre: lista1 y lista2 deben estar ordenadas.
    Devuelve: una lista con los elementos de lista1 y lista2."""
    #print("DEBUG", "lista1", lista1, "lista2", lista2)
    i, j = 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):

        if (lista1[i] < lista2[j]):
            print(f"lista 1 valor {lista1[i]}  es menor a lista2  {lista2[j]}")
            resultado.append(lista1[i])
            i += 1
        else:
            print(f"lista 2 valor {lista2[j]}  es menor a lista1  {lista1[i]}")


            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta
    print("queda", resultado)
    resultado += lista1[i:]
    print("despues de agregar al resto I ", resultado)

    resultado += lista2[j:]
    print("despues de agregar al resto J", resultado)


    return resultado


print(merge_sort([6,0,3,2,5,7,4,1]))
