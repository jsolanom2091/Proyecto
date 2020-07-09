import Personas

Libros = [{'idLibro':1,'nombre': 'Cien años de soledad','Genero':'Novela','Autor':'Gabriel García Márquez'},
{'idLibro':2,'nombre': 'Don Quijote de la Mancha','Genero':'Aburrido','Autor':'Miguel de Cervantes'},
{'idLibro':3,'nombre': 'Hamlet','Genero':'Teatro','Autor':'William Shakespeare'},
{'idLibro':4,'nombre': 'El Principito','Genero':'Fantasía','Autor':' Antoine de Saint Exupéry'},
{'idLibro':5,'nombre': 'Orgullo y Prejuicio','Genero':'Romantico','Autor':'Jane Austen '},
{'idLibro':6,'nombre': '1984','Genero':'Misterio','Autor':'George Orwell '},
{'idLibro':7,'nombre': 'La Odisea','Genero':'Poesía','Autor':'Homero'},
{'idLibro':8,'nombre': 'El retrato de Dorian Grey','Genero':'Fantasía','Autor':'Oscar Wilde'},
{'idLibro':9,'nombre': 'Lo que el viento se llevó','Genero':'Drama','Autor':'Margaret Mitchell'},
{'idLibro':10,'nombre': 'Moby-Dick','Genero':'Fantasía','Autor':'Herman Melville'}
]

LibrosPrestados = []

    
def ImprimirLista():
    print(Libros)
 
def BuscarLibro():
    print ("Que quiere buscar: ")
    texto = str (input ())
    l = 0
    while (l < len(Libros)):
        
        if(Libros[l]["nombre"].find(texto) >= 0):
            print(Libros[l])
        l = l + 1
        
def PrestarLibro():    
    ImprimirLista()
    print(" ")
    print("Que Libro es el que va a Prestar")
    Libro = int(input())
    Personas.ImprimirLista()
    print(" ")
    print("A que Persona se lo va a Prestar")
    Persona = int(input())
    LibrosPrestados.append([{'IdLibro':Libro,'IdPersona':Persona}])
   
    
def ImprimirPrestados():
    print(LibrosPrestados)
    print(" ")
    print(" ")
