import mysql.connector

class Registro_datos():

    def __init__(self):
        self.conexion = mysql.connector.connect( host='localhost',
                                            database ='TiendaPC', 
                                            user = 'root',
                                            password ='root')


#######################################PRODUCTOS####################################################################################


    #Una buena practica no usar .format() para el filtrado de datos

    def inserta_producto(self, id, stock, nombreProd, precio, marca, descuento, urlImagen, descripcion, categoria):
        cur = self.conexion.cursor()
        sql = '''INSERT INTO Producto (id, stock, nombreProd, precio, marca, descuento, urlImagen, descripcion, categoria)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        cur.execute(sql, (id, stock, nombreProd, precio, marca, descuento, urlImagen, descripcion, categoria))
        self.conexion.commit()    
        cur.close()
        
    def buscar_productos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM Producto "
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro
 
    def busca_producto(self, id):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM Producto WHERE id = %s"
        cur.execute(sql, (id,))
        nombreX = cur.fetchall()
        cur.close()     
        return nombreX

    def elimina_productos(self,nombre):
        cur = self.conexion.cursor()
        sql = '''DELETE FROM Producto WHERE NOMBREPROD = %s'''
        cur.execute(sql, (nombre,))
        a = cur.rowcount
        self.conexion.commit()    
        cur.close()
        return a


    def actualiza_productos(self, stock, nombreProd, precio, marca, descuento, urlImagen, descripcion, categoria):
        cur = self.conexion.cursor()
        sql ='''UPDATE Producto SET stock = %s, nombreProd = %s, precio = %s, marca = %s, descuento = %s, urlImagen = %s, descripcion = %s, categoria = %s
        WHERE NOMBRE = %s'''
        cur.execute(sql, (stock, nombreProd, precio, marca, descuento, urlImagen, descripcion, categoria))
        a = cur.rowcount
        self.conexion.commit()    
        cur.close()
        return a

#####################################################################################################################################################

        


