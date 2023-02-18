def nameFile():
  print(__file__,'=>',"EJERCICIO 4")
  while True: 
   print("""MENU DE OPCIONES
  1. SUMA DE UN NUMERO 
  2. DIVISION DE 2 NUMEROS""")
   opcion = int (input("DIGITE LA OPCION A UTILIZAR: "))
   if opcion == 1: 
    import pc4
    x= int(input("DIGITE HASTA QUE NUMERO SE SUMARA: "))
    print("LA SUMA ES:", pc4.recursiva(x))
   if opcion==2:
    import pc4
    print("Digite los dos numeros a dividir: ")
    x= int(input())
    y= int(input())
    print("LA DIVISION ES:", pc4.division(x,y))
nameFile() 
