#Cree un diccionario con "nombre" y "carrera" e imprime la carrera

diccionario1 = {"nombre" : "Ana",
               "carrera" : "Ingeniería"}

print (diccionario1 ["carrera"]) 
print("")

#numero2: crea un diccionario que cuente cuántas veces aparece la letra
 
palabra = "banana"
letras = {}
for letra in palabra:
  
  if letra in letras: 
   letras[letra] += 1   
   
  else:
    letras[letra] = 1
    
print(letras)
print("")

#numero3: cambia el precio de la banana  0.4

precios = {"manzana" : 0.5,
           "banana" : 0.3}

precios["banana"] = 0.4
print(precios)
print("")
#numero4

capitales = {"Francia" : "parís",
             "Italia" : "Roma",
             "España" : "Madrid"}

for clave, valor in capitales.items():

 print(f"La capital de {clave} es {valor}")
print("")

 #numero5
 
alumnos = { "Luis": {"matemáticas", "historia", "biología"},
           "Ana" : {"matemáticas", "física", "química"},
           "Carlos" : {"historia", "arte", "biología"}}


materias_unicas = set.union(*alumnos.values())  
print(materias_unicas)
print("")

materias_repetidas = alumnos["Luis"].intersection(alumnos["Ana"])
print(materias_repetidas)
print("")

alumnos["Carlos"].add("física")
print(alumnos["Carlos"])
print("")

alumnos["Carlos"].discard("arte")
print(alumnos["Carlos"])
print("")

for alumnos, materias in alumnos.items():
    print(f"{alumnos}: {len(materias)}")
