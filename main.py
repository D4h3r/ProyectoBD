import sys
from GUI import *
from conexionBD import*
from PyQt5.QtWidgets import QTableWidgetItem

#INSERT INTO `Producto` (`id`, `stock`, `nombreProd`, `precio`, `marca`, `descuento`, `urlImagen`, `descripcion`, `Categoria_idCategoria`)

class MiApp(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Form() 
		self.ui.setupUi(self)

		self.datosTotal = Registro_datos()
		self.ui.bt_refrescar.clicked.connect(self.m_productos)
		self.ui.bt_agregar.clicked.connect(self.insert_productos)
		self.ui.bt_buscar.clicked.connect(self.buscar_producto)
		self.ui.bt_borrar.clicked.connect(self.eliminar_producto)
		self.ui.bt_actualizar.clicked.connect(self.modificar_productos)
		
		self.ui.tabla_productos.setColumnWidth(0,98)
		self.ui.tabla_productos.setColumnWidth(1,100)
		self.ui.tabla_productos.setColumnWidth(2,98)
		self.ui.tabla_productos.setColumnWidth(3,98)
		self.ui.tabla_productos.setColumnWidth(4,98)
		self.ui.tabla_productos.setColumnWidth(5,98)
		self.ui.tabla_productos.setColumnWidth(6,98)
		self.ui.tabla_productos.setColumnWidth(7,98)
		self.ui.tabla_productos.setColumnWidth(8,98)

		self.ui.tabla_borrar.setColumnWidth(0,98)
		self.ui.tabla_borrar.setColumnWidth(1,100)
		self.ui.tabla_borrar.setColumnWidth(2,98)
		self.ui.tabla_borrar.setColumnWidth(3,98)
		self.ui.tabla_borrar.setColumnWidth(4,98)
		self.ui.tabla_borrar.setColumnWidth(5,98)
		self.ui.tabla_borrar.setColumnWidth(6,98)
		self.ui.tabla_borrar.setColumnWidth(7,98)
		self.ui.tabla_borrar.setColumnWidth(8,98)

		self.ui.tabla_buscar.setColumnWidth(0,98)
		self.ui.tabla_buscar.setColumnWidth(1,100)
		self.ui.tabla_buscar.setColumnWidth(2,98)
		self.ui.tabla_buscar.setColumnWidth(3,98)
		self.ui.tabla_buscar.setColumnWidth(4,98)
		self.ui.tabla_buscar.setColumnWidth(5,98)
		self.ui.tabla_buscar.setColumnWidth(6,98)
		self.ui.tabla_buscar.setColumnWidth(7,98)
		self.ui.tabla_buscar.setColumnWidth(8,98)

	def m_productos(self):	
		datos = self.datosTotal.buscar_productos()
		i = len(datos)

		self.ui.tabla_productos.setRowCount(i)
		tablerow = 0
		for row in datos:
			self.ui.tabla_productos.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
			self.ui.tabla_productos.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
			self.ui.tabla_productos.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
			self.ui.tabla_productos.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
			self.ui.tabla_productos.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
			self.ui.tabla_productos.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[5]))
			self.ui.tabla_productos.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[6]))
			self.ui.tabla_productos.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[7]))
			self.ui.tabla_productos.setItem(tablerow,8,QtWidgets.QTableWidgetItem(row[8]))
			tablerow +=1

	def insert_productos(self):
		#id = self.ui.codigoA.text() 
		stock = self.ui.cantidadA.text()
		nombre = self.ui.nombreA.text()
		precio = self.ui.precioA.text()
		marca = self.ui.marcaA.text()
		descuento = self.ui.descuentoA.text()
		urlImagen = self.ui.imagenA.text()
		descripcion = self.ui.descripcionA.text()
		Categoria_idCategoria = self.ui.categoriaA.text()


		self.datosTotal.inserta_producto(stock, nombre, precio, marca, descuento, urlImagen, descripcion, Categoria_idCategoria)
		#self.ui.codigoA.clear()
		self.ui.cantidadA.clear()
		self.ui.nombreA.clear()
		self.ui.precioA.clear()
		self.ui.marcaA.clear()
		self.ui.descuentoA.clear()
		self.ui.imagenA.clear()
		self.ui.descripcionA.clear()
		self.ui.categoriaA.clear()
	
		

	def modificar_productos(self):
		id_producto = self.ui.id_producto.text() 
		id_producto = str("" + id_producto + "")
		nombreXX = self.datosTotal.busca_producto(id_producto)

		if nombreXX != None:

			#codigoM = self.ui.codigo_actualizar.text() 
			stockM = self.ui.cantidad_actualizar.text()
			nombreM = self.ui.nombre_actualizar.text()
			precioM = self.ui.precio_actualizar.text()
			marcaM = self.ui.marca_actualizar.text()
			descuentoM = self.ui.descuento_actualizar.text()
			urlImagenM = self.ui.urlImagen_actualizar.text()
			descripcionM = self.ui.descripcion_actualizar.text()
			Categoria_idCategoriaM = self.ui.categoria_actualizar.text()
			

			act = self.datosTotal.actualiza_productos(stockM, nombreM, precioM, marcaM, descuentoM, urlImagenM, descripcionM, Categoria_idCategoriaM, id_producto)
			if act == True:
				self.ui.id_buscar.setText("BUSCAR")
				#self.ui.codigo_actualizar.clear()
				self.ui.cantidad_actualizar.clear()
				self.ui.nombre_actualizar.clear()
				self.ui.precio_actualizar.clear()
				self.ui.marca_actualizar.clear()
				self.ui.descuento_actualizar.clear()
				self.ui.urlImagen_actualizar.clear()
				self.ui.descripcion_actualizar.clear()
				self.ui.categoria_actualizar.clear()
				self.ui.id_producto.clear()
			if act == 1:
				self.ui.id_buscar.setText("ACTUALIZADO")				
				#self.ui.codigo_actualizar.clear()
				self.ui.cantidad_actualizar.clear()
				self.ui.nombre_actualizar.clear()
				self.ui.precio_actualizar.clear()
				self.ui.marca_actualizar.clear()
				self.ui.descuento_actualizar.clear()
				self.ui.urlImagen_actualizar.clear()
				self.ui.descripcion_actualizar.clear()
				self.ui.categoria_actualizar.clear()
				self.ui.id_producto.clear()

			elif act == 0:
				self.ui.id_buscar.setText("ERROR")
			else:
				self.ui.id_buscar.setText("INCORRECTO")		
		else:
			self.ui.id_buscar.setText("NO EXISTE")

	def buscar_producto(self):
		nombre_producto = self.ui.codigoB.text()
		nombre_producto = str("'" + nombre_producto + "'")

		datosB = self.datosTotal.busca_producto(nombre_producto)
		i = len(datosB)

		self.ui.tabla_buscar.setRowCount(i)
		tablerow = 0
		for row in datosB:
			self.ui.tabla_buscar.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
			self.ui.tabla_buscar.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
			self.ui.tabla_buscar.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
			self.ui.tabla_buscar.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
			self.ui.tabla_buscar.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
			self.ui.tabla_buscar.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[5]))
			self.ui.tabla_buscar.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[6]))
			self.ui.tabla_buscar.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[7]))
			self.ui.tabla_buscar.setItem(tablerow,8,QtWidgets.QTableWidgetItem(row[8]))
			tablerow +=1

	def eliminar_producto(self):
		eliminar = self.ui.codigo_borrar.text()
		eliminar = str("'"+ eliminar + "'")

		resp = (self.datosTotal.elimina_productos(eliminar))
		datos = self.datosTotal.buscar_productos()
		i = len(datos)

		self.ui.tabla_borrar.setRowCount(i)
		tablerow = 0
		for row in datos:
			self.ui.tabla_borrar.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
			self.ui.tabla_borrar.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
			self.ui.tabla_borrar.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
			self.ui.tabla_borrar.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
			self.ui.tabla_borrar.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
			self.ui.tabla_borrar.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[5]))
			self.ui.tabla_borrar.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[6]))
			self.ui.tabla_borrar.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[7]))
			self.ui.tabla_borrar.setItem(tablerow,8,QtWidgets.QTableWidgetItem(row[8]))
			tablerow +=1

		if resp == None:
			self.ui.borrar_ok.setText("NO EXISTE")
		elif resp == 0:
			self.ui.borrar_ok.setText("NO EXISTE")

		else:
			self.ui.borrar_ok.setText("SE ELIMINO")

if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())		
