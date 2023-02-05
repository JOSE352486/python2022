print("EJERCICIO 2: ")
biblio= "Biblioteca\n"
biblio+= "1.OBTENER LISTA DE CATEGORIAS\n "
biblio+= "2. OBTENER NOMBRES DE LIBRO Y AUTOR\n "
biblio+= "3. CAMBIAR TIPO DE ESTADO DEL LIBRO(L:Libre/P:Prestado)\n "
biblio+= "4. LISTA DE USUARIOS DE LA BIBLIOTECA\n "
biblio+= "5. SALIR\n "
biblio+= "OPCION: "
biblioteca = {
    'categoria': ["Generalidades", 
      "Filosofía y psicología", 
      "Religión", "Lengua"," Matemática", 
      "Artes","Literatura", "Historia y geografía"],
    'nombres':[["La Batalla Cultural","Agustín Laje"],
        ["El mundo de Sofia","Jostein Gaarder" ],
        ["El sentido y el fin de la religion","Wilfred Cantwell Smith"],
        ["El pequeño libro del Lenguaje","David Crystal"],
        ["Matematica Basica", "Ricardo Figueroa"],
        ["El libro del arte","Cennino Cennini"],
        ["Harry Pooter","J.K.Rowling"],
        ["La historia secreta del mundo","Jonathan Black"]
         ],
     'estado': "libre",    
     'usuarios':["Jose","Maria","Alondra","Luis","Rosario","Debora",
        "Sergio","Leonardo"],   
}
cod= 0
while(cod!=5):
     cod=int(input(biblio))
     print(cod)
     if(cod==1):
         print("LISTA DE CATEGORIAS DE LA BIBLIOTECA\n")
         print(biblioteca["categoria"])
         print("\n")  
     if(cod==2):
         print("LISTA DE NOMBRE - AUTOR\n")
         print(biblioteca["nombres"]) 
         print("\n")   
     if(cod==3):
            datoAcambiar= input("EL ESTADO DEL LIBRO ES: " + biblioteca["estado"] + " ¿Que valor quieres cambiar?: ")
            valorNuevo= input("¿A que valor desea cambiarlo?: ")
            biblioteca[datoAcambiar] = valorNuevo 
            print("EL ESTADO DEL LIBRO ES: ", valorNuevo)
            print("\n")
     if(cod ==4):
        print("LA LISTA DE USUARIOS DE LA BIBLIOTECA ES: ")
        print(biblioteca["usuarios"])
        print("\n")
print("Salió! ")