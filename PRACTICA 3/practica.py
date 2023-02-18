def nameFile():
  print(__file__,'=>',"EJERCICIO 1")
  texto= "Lorem Ipsum"
  print(texto)
  while True: 

   print("DIGITE LA OPCION A SELECCIONAR: ")
   print(""" 1.FUNCION split
   2.FUNCION join
   3. FUNCION count
   4. FUNCION find
   5. FUNCION upper
   6. FUNCION lower """)
   r= int(input())
   if r==1:
    n= texto.split()
    print(n)
   elif r==2: 
     print(",".join(texto))
   elif r==3: 
     h= input("DIGITE UNA FRASE O LETRA DEL TEXTO: ")
     print(texto.count(h))
   elif r==4: 
     i= input("DIGITE UNA FRASE O LETRA DEL TEXTO: ")
     print (texto.find(i))
   elif r==5:
     print(texto.upper())
   elif r==6:
     print(texto.lower())
nameFile() 
