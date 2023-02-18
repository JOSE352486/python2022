def nameFile():
  print(__file__,'=>',"EJERCICIO 3")
  class Catalogo: 
    def __init__(self, nom):
        self.nom= nom        
  i=0
  lista=[]
  def Mostrar ():
    k= 0
    while k<len(lista):
        print(lista[k].nom," ")
        k+=1
  while i==0:
    print("Menú de opciones de un producto")
    print("1. Registrar o agregar el producto")
    print("2. Lista de los productos")
    print("3. Salir: ")
    opcion=int(input())
    if opcion ==1:
        n=input("DESEA AÑADIR UN NUEVO PRODUCTO(S/N): ")
        if n =="S":
         print("REGISTRAR")
         h=input("Ingrese el nombre del nuevo producto: ")
         cat= Catalogo(h)
         lista.append(cat)
         print("Producto añadido")
        elif n =="N":
         print("PROCESO FINALIZADO") 
    if opcion ==2: 
        print("Mostrar")
        Mostrar()
nameFile() 
