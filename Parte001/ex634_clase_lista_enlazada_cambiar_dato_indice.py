# Ejercicio 634: Cambiar un dato en una lista enlazada a través de su índice.

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamagnio = 0
    
    def insertar(self, dato):
        nodo = Nodo(dato)
        self.tamagnio += 1

        if self.cabeza:
            self.cabeza.siguiente = nodo
            self.cabeza = nodo
        else:
            self.cabeza = nodo
            self.cola = nodo
    
    def iterar(self):
        actual = self.cola

        while actual:
            dato = actual.dato
            actual = actual.siguiente
            yield dato
    
    def buscar(self, dato):
        for n in self.iterar():
            if dato == n:
                return True
        
        return False
    
    def __getitem__(self, indice):
        if indice >= 0 and indice < self.tamagnio:
            actual = self.cola

            for i in range(indice):
                actual = actual.siguiente
            
            return actual.dato
        else:
            raise Exception('Índice no válido. Está por fuera del rango.')
    
    def __setitem__(self, indice, nuevo_dato):
        if indice >= 0 and indice < self.tamagnio:
            actual = self.cola

            for i in range(indice):
                actual = actual.siguiente
            
            actual.dato = nuevo_dato
        else:
            raise Exception('Índice no válido. Está por fuera del rango.')


numeros = ListaEnlazada()
numeros.insertar(2)
numeros.insertar(3)

print('Cantidad actual de elementos en la lista: %i' % numeros.tamagnio)

print()

for d in numeros.iterar():
    print(d)

print()

numeros.insertar(5)
numeros.insertar(7)

print('Cantidad actual de elementos en la lista: %i' % numeros.tamagnio)

print()

for d in numeros.iterar():
    print(d)

print()

print('¿El número 11 existe en la lista enlazada numeros?:', numeros.buscar(11))
print('¿El número 3 existe en la lista enlazada numeros?:', numeros.buscar(3))

print()

primos = [2, 3, 5, 7]
print(primos[1])
print(primos[3])
print(primos[-1])

print()

# print(numeros[-1]) # Genera excepción
print(numeros[0])
print(numeros[3])
# print(numeros[4]) # Genera excepción

print()

# numeros[-1] = 1 # Genera excepción
print(numeros[3])
numeros[3] = 11
print(numeros[3])

# numeros[4] = 13 # Genera excepción
