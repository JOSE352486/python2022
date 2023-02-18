def nameFile():
  print(__file__,'=>',"EJERCICIO 2")
  def bar(x):
    x = x * 2
    return x
  x = int(input("DIGITAR UN VALOR PARA LA VARIABLE X: ")) 
  bar(x)
  x=bar(x)
  print(x)
nameFile() 

