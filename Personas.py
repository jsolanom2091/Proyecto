ListaPersonas = [{'ID':0,'Identificación': '302600403','Nombre':'Daniel Fernando','Primer Apellido':'Ballestero','Segundo Apellido':'Umaña','Correo Electrónico':'daniel.ballestero.umana@mep.go.cr'},
{'ID':1,'Identificación': '106540419','Nombre':'Milton Eliseo De SanMartin','Primer Apellido':'Lobo','Segundo Apellido':'Nuñez','Correo Electrónico':'miltonelobo@gmail.com'},
{'ID':2,'Identificación': '502890635','Nombre':'Emilce Liseth','Primer Apellido':'Vargas','Segundo Apellido':'Campos','Correo Electrónico':'liseth.vargas.campos@fod.ac.cr'},
{'ID':3,'Identificación': '502850756','Nombre':'Roberto Elias','Primer Apellido':'Molina','Segundo Apellido':'Rosales','Correo Electrónico':'roberto.molina.rosales@mep.go.cr'},
{'ID':4,'Identificación': '108290982','Nombre':'Carlos Manuel','Primer Apellido':'Zapata','Segundo Apellido':'Cerdas','Correo Electrónico':'carlos.zapata.cerdas@mep.go.cr'},
{'ID':5,'Identificación': '107570905','Nombre':'Jose Yamil','Primer Apellido':'Alvarez','Segundo Apellido':'Cabalceta','Correo Electrónico':'yamil.alvarez.cabalceta@mep.go.cr'},
{'ID':6,'Identificación': '112160596','Nombre':'Cinthya Yesenia','Primer Apellido':'Corrales','Segundo Apellido':'Alvarado','Correo Electrónico':'112160596@nomail.com'},
{'ID':7,'Identificación': '105960154','Nombre':'Gladys Lorena','Primer Apellido':'Jimenez','Segundo Apellido':'Solano','Correo Electrónico':'esc.puertonuevo@mep.go.cr'},
{'ID':8,'Identificación': '502820232','Nombre':'Seidy','Primer Apellido':'Lopez','Segundo Apellido':'Medina','Correo Electrónico':'seidy.lopez.medina@mep.go.cr'},
{'ID':9,'Identificación': '107980545','Nombre':'Alexis','Primer Apellido':'Vargas','Segundo Apellido':'Calderon','Correo Electrónico':'107980545@nomail.com'},
{'ID':10,'Identificación': '105210055','Nombre':'Hector Miguel Del Carmen','Primer Apellido':'Segura','Segundo Apellido':'Prado','Correo Electrónico':'105210055@nomail.com'},
{'ID':11,'Identificación': '104850674','Nombre':'Miguel Angel','Primer Apellido':'Fuentes','Segundo Apellido':'Fuentes','Correo Electrónico':'miguel.fuentes.fuentes@mep.go.cr'},
{'ID':12,'Identificación': '107640438','Nombre':'Herminia Maria','Primer Apellido':'Baldivia','Segundo Apellido':'Hernandez','Correo Electrónico':'107640438@nomail.com'},
{'ID':13,'Identificación': '104920381','Nombre':'Manuel Antonio','Primer Apellido':'Vila','Segundo Apellido':'Vargas','Correo Electrónico':'104920381@nomail.com'},
{'ID':14,'Identificación': '105960915','Nombre':'Maria Gabriela','Primer Apellido':'Matamoros','Segundo Apellido':'Landazuri','Correo Electrónico':'105960915@nomail.com'},
{'ID':15,'Identificación': '800720668','Nombre':'Janina Ruth','Primer Apellido':'Castillo','Segundo Apellido':'Pasos','Correo Electrónico':'800720668@nomail.com'},
{'ID':16,'Identificación': '107130829','Nombre':'Jorge Enrique','Primer Apellido':'Flores','Segundo Apellido':'Nuñez','Correo Electrónico':'107130829@nomail.com'},
{'ID':17,'Identificación': '701410305','Nombre':'Jhovan Martin','Primer Apellido':'Perez','Segundo Apellido':'Navarrete','Correo Electrónico':'jhovan.perez.navarrete@mep.go.cr'},
{'ID':18,'Identificación': '701120963','Nombre':'Erika Ester','Primer Apellido':'Reyes','Segundo Apellido':'Aleman','Correo Electrónico':'701120963@nomail.com'},
{'ID':19,'Identificación': '205130061','Nombre':'Emidey Gerarda','Primer Apellido':'Arias','Segundo Apellido':'Hernandez','Correo Electrónico':'emidey.arias.hernandez@mep.go.cr'},
{'ID':20,'Identificación': '501870378','Nombre':'Nubia Lides','Primer Apellido':'Marchena','Segundo Apellido':'Viales','Correo Electrónico':'501870378@nomail.com'},
{'ID':21,'Identificación': '111090452','Nombre':'Jessica Perlina','Primer Apellido':'Bent','Segundo Apellido':'Morales','Correo Electrónico':'111090452@nomail.com'},
{'ID':22,'Identificación': '110590870','Nombre':'Karla Vanessa','Primer Apellido':'Mora','Segundo Apellido':'Sanchez','Correo Electrónico':'kmora20@yahoo.com'},
{'ID':23,'Identificación': '111820374','Nombre':'Flor De Maria','Primer Apellido':'Corella','Segundo Apellido':'Monge','Correo Electrónico':'flor.corella.monge@mep.go.cr'},
{'ID':24,'Identificación': '502820103','Nombre':'Yessenia','Primer Apellido':'Ruiz','Segundo Apellido':'Contreras','Correo Electrónico':'yessenia.ruiz.contreras@mep.go.cr'},
{'ID':25,'Identificación': '503420096','Nombre':'Jennifer Marcela','Primer Apellido':'Gutierrez','Segundo Apellido':'Vargas','Correo Electrónico':'esc.camposdeoro@mep.go.cr'},
{'ID':26,'Identificación': '110300227','Nombre':'Juan Carlos','Primer Apellido':'Valverde','Segundo Apellido':'Rivera','Correo Electrónico':'juan.valverde.rivera@mep.go.cr'},
{'ID':27,'Identificación': '603490324','Nombre':'Andrea Merceditas','Primer Apellido':'Mejias','Segundo Apellido':'Gomez','Correo Electrónico':'Amejias_g@hotmail.com'},
{'ID':28,'Identificación': '107310409','Nombre':'Luis Alejandro','Primer Apellido':'Aponte','Segundo Apellido':'Quiros','Correo Electrónico':'esc.canoblanco@mep.go.cr'},
{'ID':29,'Identificación': '113100411','Nombre':'Andrea Carolina','Primer Apellido':'Castillo','Segundo Apellido':'Villalobos','Correo Electrónico':'ancarcavi27@gmail.com'}
]

def ImprimirLista():
    print(ListaPersonas)
    print("")
    print("")
    
def OrdenarLista():
    Llave = str(input("Por que Valor desea ordenar el Listado de Personas: "))   
    print(sorted(ListaPersonas, key= lambda user: (user[Llave])))
    
def RegistroPersona():
    Valor = int(input("El ID de la Persona Registrada: "))
    print(ListaPersonas[Valor])
    print(" ")
    print(" ")


