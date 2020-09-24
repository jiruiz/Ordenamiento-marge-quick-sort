'''
Ejercicio 20.7.3. Ordenar la lista 6 0 3 2 5 7 4 1 usando el método quicksort. Mostrar el árbol
de recursividad explicando las llamadas que se hacen en cada paso, y el orden en el que se
realizan.
'''

def quick_sort(lista):
    """Ordena la lista de forma recursiva.
    Pre: los elementos de la lista deben ser comparables.
    Devuelve: una nueva lista con los elementos ordenados."""
    print("entra a quick sort")
    if len(lista) < 2:
        print("devuelve lista con 1 elemento")
        print(f"la lista es: {lista}")
        return lista

    menores, medio, mayores = _partition(lista)
    print(f"concatena {menores} + pivote({medio}) + {mayores}")
    return quick_sort(menores) + medio + quick_sort(mayores)

def _partition(lista):
    """Pre: lista no vacía.
    Devuelve: tres listas: menores, medio y mayores."""
    pivote = lista[0]
    menores = []
    mayores = []
    for x in range(1, len(lista)):#uno porque pivote esta en la posicoin [0]
        print("----------------------------------------------------------------------------------")
        print(f"vino para _particion ahora porque la lista es mayor a 1 por {x} veces")
        print()
        print(f"las 3 listas nos quedan asi: menores:{menores}, pivote:{pivote} y mayores{mayores}")
        print()
        print(f"pivote: {pivote}, valor de la lista: {lista[x]},la lista es: {lista}")

        if lista[x] < pivote:
            menores.append(lista[x])
        else:
            mayores.append(lista[x])
    print(f" {menores} + pivote({[pivote]}) + {mayores} en particion el IF de la funcion _particion")
    return menores, [pivote], mayores


print(quick_sort([6,0,3,2,5,7,4,1]))
