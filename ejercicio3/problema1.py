print("EJERCICIO 1: ")
print("Bienvenido al menú interactivo")
while True:
    print("""¿Qué quieres hacer? Escribe una opción
    1) DIBUJAR UN CUADRADO
    2) IDENTIFICAR LOS NUMEROS MULTIPLOS DE 2
    3) IMPRIMIR MAYORES DE EDAD""")
    opcion = input() 
    if opcion == '1':
         m=int(input("Numero de filas: "))
         n=int(input("Numero de columnas: "))
         for i in range(1,m+1):
            for j in range(1,n+1):
               print("*",end="")
            print(" ")
    elif opcion == '2':
        lista=[1,2,18,19,24,25]
        print("LOS NUMEROS MULTIPLOS DE 2 SON:")
        for i in range(1,6):
            if(lista[i]%2==0):
               print (lista[i])
    elif opcion =='3':
        print("Los nombres mayores de edad son: ")
        mi=[["ISMAEL",18],
          ["ALONDRA",17],
          ["ROSARIO",19],
          ["GABRIELA",45],
          ["AZUCENA",16]]
        for i in range(0,5):
           if(mi[i][1] >= 18):
             print(mi[i][0])
        break       
    else:
        print("Comando desconocido, vuelve a intentarlo")

print ("\n")