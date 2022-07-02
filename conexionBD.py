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
        VALUES('{}', '{}','{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(id, stock, nombreProd, precio, marca, descuento, urlImagen, descripcion, categoria)
        cur.execute(sql)
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
        sql = "SELECT * FROM Producto WHERE id = {}".format(id)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()     
        return nombreX 

    def elimina_productos(self,nombre):
        cur = self.conexion.cursor()
        sql='''DELETE FROM Producto WHERE NOMBREPROD = {}'''.format(nombre)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()    
        cur.close()
        return a   


    def actualiza_productos(self, stock, nombreProd, precio, marca, descuento, urlImagen, descripcion, categoria):
        cur = self.conexion.cursor()
        sql ='''UPDATE Producto SET  
        WHERE NOMBRE = '{}' '''.format(stock, nombreProd, precio, marca, descuento, urlImagen, descripcion, categoria)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()    
        cur.close()
        return a  

#####################################################################################################################################################

        


