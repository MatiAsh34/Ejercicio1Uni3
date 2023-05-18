from Carrera import *

class Facultad():
	__carrera: list
	def __init__(self,codigo,nombre,direccion,localidad,telefono):
		self.__codigo = codigo
		self.__nombre = nombre
		self.__direccion = direccion
		self.__localidad = localidad
		self.__telefono = telefono
		self.__carrera = []

	def getCod(self):
		return self.__codigo

	def getCarreras(self):
		return self.__carrera

	def getNom(self):
		return self.__nombre

	def getDireccion(self):
		return self.__direccion

	def AgregarCarrera(self,fila):
		carrera = Carrera(int(fila[1]),fila[2],fila[3],fila[4],fila[5])
		self.__carrera.append(carrera)

	def MostrarDatos(self):
		print("Facultad: ",self.__nombre)
		for i in range(len(self.__carrera)):
			print("Nombre de la carrera: ",self.__carrera[i].getNom())
			print("Duracion de la carrera: ",self.__carrera[i].getDuracion())
