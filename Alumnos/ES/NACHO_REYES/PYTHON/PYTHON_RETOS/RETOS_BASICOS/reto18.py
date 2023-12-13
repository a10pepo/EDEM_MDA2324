def eliminar (str, n):
  index = n
  liststr = list(str)
  liststr.pop(index)
  str = ''.join(liststr)
  print(str)

eliminar('Madrid',0)
eliminar('Madrid',1)
eliminar('Madrid',2)