import sys
def argumento():
  nombre= sys.argv[0]
  cantidad = len(sys.argv)
  argumentos = str(sys.argv)
  print("NOMBRE: {}".format(nombre))
  print("CANTIDAD DE ARGUMENTOS: {}".format(cantidad))
  print("LISTA DE ARGUMENTOS: {}".format(argumentos))

print (argumento())