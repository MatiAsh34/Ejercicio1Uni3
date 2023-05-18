from Facultad import Facultad
import csv

class ManejadorFacultades():
	def __init__(self):
		self.__lista = []

	def CargaLista(self):
		archivo = open('Facultades.csv',encoding='utf8')
		reader = csv.reader(archivo,delimiter=',')
		facultad = None

		for fila in reader:
			if len(fila)==5:
				facultad = Facultad(int(fila[0]),fila[1],fila[2],fila[3],fila[4])
				self.__lista.append(facultad)
			else:
				facultad.AgregarCarrera(fila)
		

	def BuscaFacultad(self,codigo):
		i = 0
		while (i < len(self.__lista)) and (self.__lista[i].getCod() != codigo):
			i += 1

		if i < len(self.__lista):
			self.__lista[i].MostrarDatos()
		else:
			print("No se encontro codigo")

	def Mostrar(self,carrera,codigo,i):
		print("Nombre carrera: {}, Codigo: {}, Nombre de Facultad: {}, Direccion de la Facultad: {}".format(carrera.getNom(),
																														codigo,
																														self.__lista[i].getNom(),
																														self.__lista[i].getDireccion()))

	def BuscaCarrera(self,nom):
		i = 0
		band = False
		while (i < len(self.__lista) and not band):
			j = 0
			carreras = self.__lista[i].getCarreras()
			while (j < len(carreras)):
				carrera = carreras[j]
				if nom == carrera.getNom():
					codigofacu = str(self.__lista[i].getCod())
					codigocarrera = str(carrera.getCod())
					codigo = codigofacu+codigocarrera
					self.Mostrar(carrera,codigo,i)
					band = True
				j += 1
			i += 1


