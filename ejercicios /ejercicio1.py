diccionario = {1:1, 2:2 , 3:3}
for x in diccionario:
    del diccionario[x]
    diccionario[x]= x
print (diccionario)