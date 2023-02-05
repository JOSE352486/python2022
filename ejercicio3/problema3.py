def mayor(numero1:int,numero2:int):
    if(numero1 >numero2):
       print("EL NUMERO 1 ES MAYOR AL NUMERO 2"),
    if( numero1 == numero2 ):
      print("EL NUMERO 1 ES IGUAL AL NUMERO 2"),
    if(numero1 < numero2 ):
       print("EL NUMERO 2 ES MAYOR AL NUMERO 1")  
num1= int(input("Agregar el primero numero: "))
num2=  int(input("Agregar el segundo numero: "))
resultado = mayor(num1, num2)
