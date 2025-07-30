#crearemos una cesta de compras 

lista = [] 
precios = []
print("")
agregar_a_la_lista = input("Qué deseas agregar a la cesta?").lower().strip()
precio1 = float(input("Cuál es el precio de eso?"))
precios.append(precio1)
lista.append(agregar_a_la_lista)
print()
print(F"Haz añadido {agregar_a_la_lista} a la cesta.")
print(f"Con un costo de {precio1}$.")

def opciones():
    print()
    print("Qué deseas hacer ahora?")
    print("1-AGREGAR")
    print("2-MOSTRAR")
    print("3-SACAR")
    print("4-CALCULAR")
    print("5-SALIR")
    print()
def comprando():
 while True:
    opciones()
    pregunta = input("").strip().lower()
    
    if pregunta in ["agregar", "1"]:
          print()  
          agregar_a_la_lista = input("Qué deseas agregar a la cesta?").lower().strip()
          precio = float(input("Cuál es el precio de eso?"))
          precios.append(precio)
          lista.append(agregar_a_la_lista)
          print(f"haz añadido {agregar_a_la_lista} a la cesta")
          print(f"Con un costo de {precio:.2f}$")
          
    elif pregunta in ["mostrar", "2"]:
        print()
        print(f"tu cesta tiene {lista}")
        
    elif pregunta in ["sacar", "3"]:
            print()
            print ("Qué deseas sacar de la cesta?")
            print (lista)
            eliminar = input("").lower().strip()
            if eliminar not in lista:
                    print("Ese producto no esta en la cesta.")
                    continue
            lista.remove(eliminar)
            print (f"Haz sacado {eliminar} de la cesta.")
            
            
    elif pregunta in ["calcular", "4"]:
            
            print()
            print("el precio de tus productos es de:")
            precio_total = sum(precios)  
            print(F"{precio_total:.2f}")
            
            
    elif pregunta in ["salir", "5"]:
          print()
          print("Gracias por su compra!")   
          break
    
    else:
        print()
        print("No es reconocida esa opción, vuelva a intentarlo.")
comprando()