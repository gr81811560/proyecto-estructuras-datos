# Módulo principal del juego
from estructuras import (
    sala_1_vestibulo, sala_2_estanterias, sala_3_mapas, 
    sala_4_fichas, sala_5_sellos, ArbolBinarioBusqueda
)
from persistencia import guardar_partida, cargar_partida

def main():
    print("=== JUEGO SERIO: EL ARCHIVO PERDIDO ===")
    
    partida = cargar_partida()
    if not partida:
        jugador = sala_1_vestibulo()
        inventario = []
        catalogo = {}
    else:
        jugador = partida.get("jugador", {})
        inventario = partida.get("inventario", [])
        catalogo = partida.get("catalogo", {})

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Sala 1: Ver datos del jugador")
        print("2. Sala 2: Gestionar inventario (Listas)")
        print("3. Sala 3: Ver coordenadas (Tuplas)")
        print("4. Sala 4: Registrar ficha (Diccionarios)")
        print("5. Sala 5: Depurar con Conjuntos")
        print("6. Sala Central: Actividad Clave (Árbol Binario)")
        print("7. Guardar y Salir")
        
        opcion = input("Elige una opción (1-7): ")
        
        if opcion == "1":
            print(jugador)
        elif opcion == "2":
            sala_2_estanterias(inventario)
        elif opcion == "3":
            sala_3_mapas()
        elif opcion == "4":
            sala_4_fichas(catalogo)
        elif opcion == "5":
            prueba = inventario + ["101", "101", "102"]
            sala_5_sellos(prueba)
        elif opcion == "6":
            print("\n--- SALA CENTRAL: RECONSTRUCCIÓN DEL CATÁLOGO ---")
            arbol = ArbolBinarioBusqueda()
            arbol.insertar(50, {"titulo": "Matemáticas"})
            arbol.insertar(30, {"titulo": "Física"})
            arbol.insertar(70, {"titulo": "Química"})
            
            resultado = []
            arbol.recorrido_inorden(arbol.raiz, resultado)
            print("Recorrido Inorden (claves ordenadas):", resultado)
            
            buscado = input("Ingresa clave a buscar (ej. 30): ")
            if buscado.isdigit():
                res = arbol.buscar(int(buscado))
                print(f"Resultado: {res} | Comparaciones realizadas: {arbol.comparaciones}")
            else:
                print("Entrada inválida.")
                
        elif opcion == "7":
            estado = {"jugador": jugador, "inventario": inventario, "catalogo": catalogo}
            guardar_partida(estado)
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()