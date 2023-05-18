from ManejaFacultades import *

if __name__ == '__main__':
	Manejador = ManejadorFacultades()
	Manejador.CargaLista()

	opcion = None
	while opcion != '0':
		print("\nMenu opciones")
		print("1- Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad.")
		print("2- Dado el nombre de una carrera, mostrar código (se conforma con número de código de Facultad y código de carrera), nombre y localidad de la facultad donde esta se dicta.")
		print("0- Salir")

		opcion = input("\nIngrese opcion: ")

		if opcion == '1':
			codigo = int(input("Ingrese codigo de facultad: "))
			Manejador.BuscaFacultad(codigo)

		if opcion == '2':
			nomCarrera = input("Ingrese nombre de la carrera: ")
			Manejador.BuscaCarrera(nomCarrera)

		if opcion == '3':
			print("Saliendo...")