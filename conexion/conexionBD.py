import os
import sqlite3
from sqlite3 import Error

def connectionBD():
    try:
        # Se busca la base de datos almacenada en la carpeta
        ruta_bd = os.path.join('bd', 'equipos.sql')
        
        # Normaliza la ruta para evitar problemas de diagonales en diferentes sistemas
        ruta_bd = os.path.normpath(ruta_bd)

        mydb = sqlite3.connect(ruta_bd)
        return mydb
        
    except Error as e:
        print(f"Error en la conexión a BD: {e}")
        return None