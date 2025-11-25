import sqlite3 #importa la libreria sqlite3 para manejar bases de datos


#conexion a la base de datos
def conectar():
    try:
        return sqlite3.connect("inventario.db")
    except:
        return None

#crear la tabla inventario si no existe
def crear_tabla(conexion):
    cursor = conexion.cursor()
    cursor.execute(
        '''
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

#cerrar la conexion a la base de datos
def cerrar_conexion(conexion):
    try:
        if conexion:
            conexion.close()
    except sqlite3.Error as e:
        print("Error al cerrar:", e)

#agrega un nuevo producto a la base de datos por parametros
def agregar_productos(conexion,nombre,descripcion,cantidad,precio,categoria):
    
    cursor = conexion.cursor()
    try: 
        query = '''
                INSERT INTO inventario (nombre,descripcion,cantidad,precio,categoria)
                VALUES (?, ?, ?, ?, ?)
                '''
        cursor.execute(query, (nombre,descripcion,cantidad, precio, categoria))
        conexion.commit()
        print(f"Producto '{nombre}' agregado")
    except sqlite3.Error as e:
        print(f"Error al agregar el producto: {e}")
        conexion.rollback()
        
#obtiene todos los productos de la base de datos
def mostrar_productos(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM inventario')
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error al obtener los productos: {e}")

#busca productos por id en la base de datos            
def buscar_productos(conexion, idProducto):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM inventario WHERE id = ? ", (idProducto,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error al buscar el producto: {e}")
  
#actualiza productos por id en la base de datos mediante parametros         
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

#elimina productos por id en la base de datos 
def eliminar_productos(conexion,id_producto):
    try: 
        cursor = conexion.cursor()
        query = '''
                DELETE FROM inventario WHERE id = ? 
                '''
        cursor.execute(query,(id_producto,))
        conexion.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"Error al eliminar el producto: {e}")
        conexion.rollback()        

#genera un reporte de productos con bajo stock de la base de datos
def reportes_bajo_stock(conexion, limite):
    try:
        cursor = conexion.cursor()
        query = '''
                SELECT * FROM inventario WHERE cantidad < ?
                '''
        cursor.execute(query, (limite,))
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error al generar el reporte de bajo stock: {e}")
 
