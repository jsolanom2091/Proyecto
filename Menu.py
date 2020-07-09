import Personas
import Libros

Menu = {'a': 'a - Ver lista de personas','b': 'b - Ordenar lista de personas','c': 'c - Imprimir registro de lista de persona','d': 'd - Ver lista de libros',
    'e': 'e - Buscar libro','f': 'f - Prestar libro','g': 'g - Ver prestamo de libros','h': 'h - Salir'}

def Seleccion(pSeleccion):
    if pSeleccion == "a":
        Personas.ImprimirLista()
    elif pSeleccion == "b":
	   	Personas.OrdenarLista()
    elif pSeleccion == "c":
       Personas.RegistroPersona()
    elif pSeleccion == "d":
        Libros.ImprimirLista()
    elif pSeleccion == "e":
        Libros.BuscarLibro()
    elif pSeleccion == "f":
        Libros.PrestarLibro()
    elif pSeleccion == "g":
        Libros.ImprimirPrestados()
    elif pSeleccion == "h":
        exit()
               

Activo = True 
while (Activo == True):
    print("Menú Principal: ")
    print (Menu['a'])
    print (Menu['b'])
    print (Menu['c'])
    print (Menu['d'])
    print (Menu['e'])
    print (Menu['f'])
    print (Menu['g'])
    print (Menu['h'])
    print(" ")
    print(" ")
    print("Seleccione una de las opciones del menú: ")
    Opcion = str(input())
    Seleccion(Opcion)

    if Opcion == "h":
        Activo = False
        