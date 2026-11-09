# Módulo de persistencia en archivos
import json
import os

ARCHIVO = "partida.json"

def guardar_partida(datos: dict):
    """Guarda los datos en un archivo JSON controlando errores."""
    try:
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        print("[Sistema] Partida guardada con éxito.")
    except IOError:
        print("[Error] No se pudo escribir el archivo.")


def cargar_partida() -> dict:
    """Carga los datos del archivo JSON si existe."""
    if not os.path.exists(ARCHIVO):
        return {}
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            print("[Sistema] Partida cargada con éxito.")
            return json.load(f)
    except (IOError, json.JSONDecodeError):
        print("[Error] Archivo dañado o no legible.")
        return {}