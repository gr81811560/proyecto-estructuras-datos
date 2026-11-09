# Módulo de estructuras de datos y salas

def sala_1_vestibulo():
    """Sala 1: Variables y tipos de datos del jugador."""
    nombre = input("Nombre del explorador (str): ")
    vida = float(input("Vida inicial (float, ej. 100.0): "))
    nivel = int(input("Nivel de acceso (int): "))
    activo = True
    return {"nombre": nombre, "vida": vida, "nivel": nivel, "activo": activo}


def sala_2_estanterias(inventario: list):
    """Sala 2: Listas y comprensión de listas."""
    item = input("Ingresa un fragmento para el inventario: ")
    inventario.append(item)
    # Comprensión de listas exigida por la seño
    mayus = [x.upper() for x in inventario]
    print("Inventario en mayúsculas:", mayus)


def sala_3_mapas():
    """Sala 3: Tuplas inmutables y desempaquetado."""
    coordenada = (4, 12)  # Fila, columna
    fila, columna = coordenada
    print(f"Coordenada actual -> Fila: {fila}, Columna: {columna}")


def sala_4_fichas(catalogo: dict):
    """Sala 4: Diccionarios y consultas por clave."""
    codigo = input("Código del fragmento (ej. 101): ")
    if codigo in catalogo:
        print("Ya existe:", catalogo[codigo])
    else:
        titulo = input("Título del fragmento: ")
        catalogo[codigo] = {"titulo": titulo, "sala": "Sala 4", "valor": 50}
        print("Fragmento guardado en el diccionario con éxito.")


def sala_5_sellos(recolectados: list):
    """Sala 5: Conjuntos (Sets) para eliminar duplicados."""
    unicos = set(recolectados)
    print(f"Originales con duplicados: {len(recolectados)}")
    print(f"Únicos sin duplicados (Set): {len(unicos)}")
    return unicos


#ÁRBOL BINARIO DE BÚSQUEDA (Actividad Clave - Sala Central) 
class NodoArbol:
    """Clase nodo para el Árbol Binario de Búsqueda."""
    def __init__(self, clave, valor):
        self.clave = int(clave)
        self.valor = valor
        self.izq = None
        self.der = None


class ArbolBinarioBusqueda:
    """Implementación propia de un ABB sin librerías externas."""
    def __init__(self):
        self.raiz = None
        self.comparaciones = 0

    def insertar(self, clave, valor):
        """Inserta un nodo en el árbol de forma recursiva."""
        if not self.raiz:
            self.raiz = NodoArbol(clave, valor)
        else:
            self._insertar_recursivo(self.raiz, clave, valor)

    def _insertar_recursivo(self, nodo, clave, valor):
        if clave < nodo.clave:
            if not nodo.izq:
                nodo.izq = NodoArbol(clave, valor)
            else:
                self._insertar_recursivo(nodo.izq, clave, valor)
        elif clave > nodo.clave:
            if not nodo.der:
                nodo.der = NodoArbol(clave, valor)
            else:
                self._insertar_recursivo(nodo.der, clave, valor)

    def recorrido_inorden(self, nodo, lista_resultado):
        """Recorre el árbol inorden para verificar ordenamiento."""
        if nodo:
            self.recorrido_inorden(nodo.izq, lista_resultado)
            lista_resultado.append(nodo.clave)
            self.recorrido_inorden(nodo.der, lista_resultado)

    def buscar(self, clave):
        """Busca un fragmento contando las comparaciones realizadas."""
        self.comparaciones = 0
        return self._buscar_recursivo(self.raiz, int(clave))

    def _buscar_recursivo(self, nodo, clave):
        if not nodo:
            return None
        self.comparaciones += 1
        if clave == nodo.clave:
            return nodo.valor
        elif clave < nodo.clave:
            return self._buscar_recursivo(nodo.izq, clave)
        else:
            return self._buscar_recursivo(nodo.der, clave)