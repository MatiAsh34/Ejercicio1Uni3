from Facultad import *

class Carrera():
	def __init__(self,codigo,nombre,titulo,duracion,nivel):
		self.__codigo = codigo
		self.__nombre = nombre
		self.__titulo = titulo
		self.__duracion = duracion
		self.__nivel = nivel

	def __str__(self):
		return ("%s %s %s %s %s") % (self.__codigo,self.__nombre,self.__titulo,self.__duracion,self.__nivel)

	def getNom(self):
		return self.__nombre

	def getCod(self):
		return self.__codigo

	def getDuracion(self):
		return self.__duracion