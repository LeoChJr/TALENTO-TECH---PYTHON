import sqlite3
import colorama
from colorama import Fore, Style


def conectar():
    try:
        return sqlite3.connect("inventario.db")
    except:
        return None
def crear_tabla(conexion):
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT NOT NULL
        )
        ''')
    conexion.commit()
def cerrar_conexion(conexion):
    try:
        if conexion:
            conexion.close()
    except sqlite3.Error as e:
        print("❌ Error al cerrar:", e)

def agregar_productos(conexion,nombre,descripcion,cantidad,precio,categoria):
    
    cursor = conexion.cursor()
    try: 
        query = '''
                INSERT INTO inventario (nombre,descripcion,cantidad,precio,categoria)
                VALUES (?, ?, ?, ?, ?)
                '''
        cursor.execute(query, (nombre,descripcion,cantidad, precio, categoria))
        conexion.commit()
        print(f"Producto '{nombre}' agregado con éxito.")
    except sqlite3.Error as e:
        print(f"Error al agregar el producto: {e}")
        conexion.rollback()
    
        
def mostrar_productos(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM inventario')
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error al obtener los productos: {e}")
            
def buscar_productos(conexion, idProducto):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM inventario WHERE id = ? ", (idProducto,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error al buscar el producto: {e}")
    
       
def actualizar_productos(conexion,id, nombre,descripcion,cantidad, precio,categoria):
    
    try:
        cursor = conexion.cursor()
        query = '''
                UPDATE inventario
                SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
                WHERE id = ?
        '''
        cursor.execute(query,(nombre, descripcion, cantidad, precio, categoria, id))
        conexion.commit()
        return cursor.rowcount
    except sqlite3.Error as e:
        print(f"Error al actualizar el producto: {e}")
        conexion.rollback()

def eliminar_productos(conexion,id_producto):
    try: 
        cursor = conexion.cursor()
        query = '''
                DELETE FROM inventario WHERE id = ? 
                '''
        cursor.execute(query,(id_producto,))
        conexion.commit()
        return cursor.rowcount >0
    except sqlite3.Error as e:
        print(f"Error al eliminar el producto: {e}")
        conexion.rollback()
        

def reportes_bajo_stock(conexion, umbral):
    try:
        cursor = conexion.cursor()
        query = '''
                SELECT * FROM inventario WHERE cantidad < ?
                '''
        cursor.execute(query, (umbral,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error al generar el reporte de bajo stock: {e}")
 
