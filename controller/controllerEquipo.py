from random import sample
import sqlite3
from conexion.conexionBD import * 

def registrarUsuario(nombre, clave):
    try:
        conexion = connectionBD()
        cursor = conexion.cursor()
        
        # Verificar si el usuario ya existe para no duplicarlo
        cursor.execute("SELECT id FROM usuario WHERE nombre = ?", (nombre,))
        if cursor.fetchone():
            return "existe" # Se indica que el nombre ya está en uso
            
        # Si no existe se ingresara el usuario
        sql = "INSERT INTO usuario (nombre, clave) VALUES (?, ?)"
        cursor.execute(sql, (nombre, clave))
        conexion.commit()
        
        resultado_insert = cursor.rowcount
        
        cursor.close()
        conexion.close()
        
        return resultado_insert 
        
    except Exception as e:
        print(f"Error al registrar usuario: {e}")
        return 0

def verificarUsuario(nombre, clave):
    try:
        conexion = connectionBD()
        conexion.row_factory = sqlite3.Row
        cursor = conexion.cursor()
        
        # Consultamos buscando coincidencia exacta de nombre y clave
        sql = "SELECT * FROM usuario WHERE nombre = ? AND clave = ?"
        cursor.execute(sql, (nombre, clave))
        row = cursor.fetchone()
        
        # Si existe se retorma los datos del usuario incluyendo su id
        resultadoQuery = dict(row) if row else None
        
        cursor.close()
        conexion.close()
        
        return resultadoQuery
        
    except Exception as e:
        print(f"Error al verificar usuario: {e}")
        return None
    
def listaEquipos(id_usuario):
    conexion = connectionBD() 
    
    if conexion is None:
        print("Advertencia: No se pudo conectar a la base de datos.")
        return []
        
    conexion.row_factory = sqlite3.Row 
    cur = conexion.cursor()

    querySQL = "SELECT * FROM equipos WHERE id_usuario = ? ORDER BY id DESC"
    cur.execute(querySQL, (id_usuario,)) 
    
    resultadoBusqueda = [dict(row) for row in cur.fetchall()]
    
    cur.close() 
    conexion.close()  
    return resultadoBusqueda

def updateEquipo(id=''):
    conexion = connectionBD()
    conexion.row_factory = sqlite3.Row 
    cursor = conexion.cursor()
    
    cursor.execute("SELECT * FROM equipos WHERE id = ? LIMIT 1", (id,))
    row = cursor.fetchone() 
    resultQueryData = dict(row) if row else None
    
    cursor.close()
    conexion.close()
    return resultQueryData
    
def registrarEquipo(id_usuario, marca='', modelo='', clase='', area='', observacion='', revisado='', nuevoNombreFile=''):       
    conexion = connectionBD()
    cursor = conexion.cursor()
        
    sql = ("INSERT INTO equipos(id_usuario, marca, modelo, clase, area, observacion, revisado, foto) VALUES (?, ?, ?, ?, ?, ?, ?, ?)")
    valores = (id_usuario, marca, modelo, clase, area, observacion, revisado, nuevoNombreFile)
    
    cursor.execute(sql, valores)
    conexion.commit()
    
    resultado_insert = cursor.rowcount
    
    cursor.close() 
    conexion.close() 
    
    return resultado_insert

def detallesdelEquipo(idEquipo):
    conexion = connectionBD()
    conexion.row_factory = sqlite3.Row
    cursor = conexion.cursor()
    
    cursor.execute("SELECT * FROM equipos WHERE id = ?", (idEquipo,))
    row = cursor.fetchone()
    resultadoQuery = dict(row) if row else None
    
    cursor.close() 
    conexion.close() 
    
    return resultadoQuery
    
def recibeActualizarEquipo(marca, modelo, clase, area, observacion, revisado, foto_equipo, idEquipo):
    try:
        conexion = connectionBD()
        cursor = conexion.cursor()
        
        query_base = """
            UPDATE equipos
            SET 
                marca = ?,
                modelo = ?,
                clase = ?,
                area = ?,
                observacion = ?,
                revisado = ?
        """
        params = [marca, modelo, clase, area, observacion, revisado]

        if foto_equipo:
            query_base += ", foto = ?"
            params.append(foto_equipo)

        query_base += " WHERE id = ?"
        params.append(idEquipo)

        cursor.execute(query_base, tuple(params))
        conexion.commit()

        row_count = cursor.rowcount
        
        cursor.close()
        conexion.close()
        
        return row_count or 0
        
    except Exception as e:
        print(f"Ocurrió un error en recibeActualizarEquipo: {e}")
        return 0

def stringAleatorio():
    string_aleatorio = "0123456789abcdefghijklmnopqrstuvwxyz_"
    longitud         = 20
    secuencia        = string_aleatorio.upper()
    resultado_aleatorio  = sample(secuencia, longitud)
    string_aleatorio     = "".join(resultado_aleatorio)
    return string_aleatorio