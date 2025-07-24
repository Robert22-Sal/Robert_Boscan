#crear un juego interactivo,con historia en la que cada decision me lleve a un escenario diferente 

print("")
print("\t BAJO LA LLUVIA") 
print("")

print("puedo saber cuál es tu nombre jugador?")
nombre = input("Escribe tu nombre: ")
print("")
print(f"bienvenido {nombre}, estás a punto de ponerte en los zapatos de un niño")
print("en la que cada decisión te llevará a un final distinto.")


while True:
    print("")
    print(f"Entonces {nombre}, estas listo para volver a ser un niño de nuevo?")
    print("S / N")
    entrar = input("").lower()
    
    if entrar == "s":
     print("Muy bien, Disfruta tu aventura!")
     break
    
    elif entrar == "n":
     print("estas seguro de que no quieres vivir esta aventura?")
     print("volveré a preguntarlo...")
     
    else:
        print("esa respuesta no es válida, volveré a preguntarlo...")
     
print("")
print("Eres un  niño que se levantó tarde para ir a la escuela y perdiste el autobus,")
print("vas corriendo pero el cielo está nublado y parece que va a llover, piensas:")
print("'espero que me de tiempo de llegar'")
print("pero empieza a llover y tienes que decidir si SEGUIR corriendo o RESGUARDARTE bajo un techo.")
print("")

while True:
    print("")
    
    accion1 = input("Qué harás? :").lower()
     
    if accion1 == "seguir":
        print("")
        print("Empiezas a correr más rapido pero la lluvia está empeorando,")
        print("te cansas y dejas de correr, estas empapado y te das cuenta que")
        print("así no es buena idea ir a la escuela, así que te rindes y regresas a casa.")
        print("En el camino de regreso ves un autobus y piensas si es buena idea")
        print("seguir a PIE o irte en el BUS.")      
        while True:
         print("")
         accion2 = input("Cómo te irás? :").lower()
         
         if accion2 == "pie":
             print("")
             print("Sigues el camino a pie y notas que está parando la lluvia,")
             print("empiezas a sentir frío y te falta mucho para llegar a casa,")
             print("piensas en llamar a tu mamá para que vaya a buscarte pero te das cuenta")
             print("que dejaste tu celular y tu cartera en tu habitación,")
             print("entonces ves una señora a lo lejos y piensas en si pedirle su CELULAR o SEGUIR.")
             while True:
                 print("")
                 accion2_1 = input("Qué harás? :").lower()
                 
                 if accion2_1 == "celular":
                     print("")
                     print("le pides el celular a la señora y amablemente te lo presta para que puedas llamar a tu mamá.")
                     print("Tu mamá te va a buscar y te pregunta qué paso, tu piensas")
                     print("si es mejor MENTIR o CONFESAR")
                     while True:
                         print("")
                         accion2_1_2 = input("Qué le dirás a tu mamá? :").lower()
                         
                         if accion2_1_2 == "mentir":
                             print("")
                             print("inventas una muy mala excusa y tu mamá no te cree, se molesta")
                             print("y al llegar a casa te castiga.")
                             print("Al menos ya estas en casa... pero ahora resfriado y castigado")
                             print("")
                             print("Fin :<")
                             print("")
                             import sys
                             sys.exit()
                             
                         elif accion2_1_2 == "confesar":
                             print("")
                             print("le confiesas a tu mamá, mientras le cuentas intenta ocultarlo pero se nota que ")
                             print("le hace algo de gracia, ambos ríen y bromean un poco, al llegar")
                             print("a casa te tomas una bebida caliente y descansas.")
                             print("")
                             print("Fin :>")
                             print("")
                             import sys
                             sys.exit()
                             
                         else: 
                             print("Tienes que elegir que le dirás a tu mamá.") 
                
                 elif accion2_1 == "seguir":
                     print("")
                     print("Decides no molestar y seguir caminando, la lluvia vuelve y empiezas a temblar")
                     print("del frío, luego de varios minutos ves tu casa a lo lejos y corres con todas tus fuerzas,")
                     print("al llegar a casa tu mamá te recibe preocupada y tu solo sonríes.")
                     print("te preparas una bebida caliente y te acuestas en tu cama, vas a estar resfriado por unos días")
                     print("")
                     print("Fin :/")
                     print("")
                     import sys
                     sys.exit()
                     
                 else:
                     print("Tienes que elegir lo que harás.")
             
        
         elif accion2 == "bus":
             print("")
             print("Subes al autobus y el conductor te mira mal porque estas todo mojado, pero te deja subir")
             print("te sientas y buscas tu cartera para pagar pero te das cuenta que la dejaste en")
             print("tu habitación junto con tu celular, te asutas porque no tienes como pagar")
             print("y cuando el señor pasa a cobrar tu pasaje piensas ")
             print("en si deberías decir la VERDAD o MENTIR.")
             while True:
                 print("")
                 accion2_2 = input("Qué le diras? :").lower()
                 
                 if accion2_2 == "verdad":
                     print("")
                     print("Le dices la verdad al señor y acepta solo por esta vez llevarte gratis.")
                     print("Te sientes más tranquilo y con menos frío, llegas a casa y le cuentas a tu mamá")
                     print("lo que pasó, ambos ríen y aunque posiblemente tendrás un resfriado, tienes también")
                     print("una buena historia que contar a tus amigos.")
                     print("")
                     print("Fin :)")
                     print("")
                     import sys
                     sys.exit()
                     
                 elif accion2_2 == "mentir":
                     print("")
                     print("investas una mala excusa pero el señor no te cree y se molesta,")
                     print("con un gesto serio,te dice que no puede dejarte viajar sin pagar")
                     print("y te pide que te bajes en la siguiente parada.")
                     print("Ahora no tienes más que caminar con frío y un poco de lluvia hasta llegar a casa,")
                     print("te sientes muy mal por haber mentido y al llegar a casa tu mamá se molesta y te castiga.")
                     print("")
                     print("Fin :(")
                     print("")
                     import sys
                     sys.exit()
                     
                 else:
                     print("Tienes que elegir qué le dirás al señor.")
         else:
            print("tienes que elegir si te vas a PIE o en el BUS")
        
        
    elif accion1 == "resguardarte":
        print("")
        print("Haz entrado en una tienda para resguardarte de la lluvia,")
        print("el dueño de la tienda te pregunta: Tú no deberías estar en la escuela?")
        print("te da un poco de pena pero le cuentas lo que pasó y el señor te ofrece un paraguas.")
        print("Piensas en si ACEPTARLO, RECHAZARLO o ESPERAR a que deje de llover.")
        while True:
            print("")
            accion3 = input("Qué le dirás al dueño de la tienda? :").lower()
            
            if accion3 == "aceptarlo":
                print("")
                print("Lo aceptas y le agradeces, el dueño de la tienda te da un consejo y")
                print("te desea buena suerte. Usas el paraguas para cubrirte de la lluvia y")
                print("llegas en la escuela tarde pero seco, cuando estás a punto de entrar te")
                print("encuentras con el director el cual te pregunta por qué el retraso, entonces no sabes")
                print("si decirle la VERDAD o MENTIRLE.")
                while True:
                    print("")
                    accion3_1 = input("Qué le dirás al direcor? :").lower()
                    
                    if accion3_1 == "verdad": 
                        print("")
                        print("El director te cree pero no te deja pasar y te castiga.")
                        print("Estás en el área de castigo, aburrido y sin mucho que hacer, entonces piensas")
                        print("en tres opciones: sacar el cuaderno para ESTUDIAR, ESCAPAR o intentar DORMIR")
                        while True:
                            print("")
                            accion3_1_2 = input("Qué haces en el castigo? :").lower()
                            
                            if accion3_1_2 == "estudiar":
                                print("")
                                print("Cuando el director entra de nuevo y te ve estudiando, perdona")
                                print("tu castigo y te deja entrar al salón, aunque de igual forma es tarde.")
                                print("")
                                print("Fin B)")
                                print("")
                                import sys
                                sys.exit()
                                
                            elif accion3_1_2 == "escapar":
                                print("")
                                print("El profesor te atrapa y llama a tu mamá, ella va a buscarte, se")
                                print("molesta contigo, al llegar a casa te castiga y quedas suspendido")
                                print("de la escuela por una semana.")
                                print("")
                                print("Fin >:v")
                                print("")
                                import sys
                                sys.exit()
                                
                            elif accion3_1_2 == "dormir":
                                print("")
                                print("Te quedas dormido toda la hora debido a que el profesor no te desperó,")
                                print("cuendo despiertas ves que es tarde y ya no tienes nada que hacer")
                                print("más que regresarte a casa y contarle a tu mamá lo que ocurrió.")
                                print("")
                                print("Fin B(")
                                print("")
                                import sys
                                sys.exit()
                            else:
                                print("Tienes que hacer algo para que no")
                                print("mueras de aburrimiento.")
                                
                    elif accion3_1 == "mentirle":
                        print("")
                        print("Inventas una excusa terrible y el director no te cree, te castiga y")
                        print("llama a tu mamá para que vaya a busarte, tu mamá se molesta mucho contigo")
                        print("pero te dice que si le prometes que no volverá a ocurrir te perdonará")
                        print("(Aunque sabes que te despiertas tarde por defecto).")
                        print("")
                        print("Fin B<")
                        print("")
                        import sys
                        sys.exit()
                        
                    else:
                        print("Tienes que darle una respuesta rápida al director!!")
                        
            elif accion3 == "rechazarlo":
                print("")
                print("El dueño de la tienda entiende, pero te da el consejo de que lo tomes, aún así no lo haces, decides")
                print("salir a esperar el próximo autobus que paasará pronto, vas a la parada pero")
                print("te empapas ya que todavía está lloviendo. Caundo estás en la parada recuerdas que dejaste")
                print("tu celular y tu cartera en tu habiación y te das cuenta de que no puedes subir al autobus.")
                print("El autobus pasa y ya es tarde, no tienes otra opción más que esperar en la tienda a que")
                print("deje de llover para regresar a casa.")
                print("")
                print("Fin :c")
                print("")
                #el peor final la verdad, pero me quedé sin ideas :v
                import sys
                sys.exit()
                
                        
            elif accion3 == "esperar":
                print("")
                print("Le dices al dueño que esperarás a que deje de llover ya que no crees que durará mucho.")
                print("Decides comprar algo para comer, pero te das cuenta que dejaste tu celular")
                print("y cartera en tu habitación así que le preguntas al dueño de la tienda si puedes pagar luego")
                print("lo que hace que se ofenda y se moleste, piensas en si deberías pedirle DISCULPAS,")
                print("DECIRLE que deje de gritarte o ignorarlo y ROBAR algo de comer.")
                while True:
                  print("")
                  accion3_2 = input("Qué harás ahora? :").lower() #recomiendo arreglar la situación...
                  
                  if accion3_2 == "disculpas":
                      print("")
                      print("Le pides perdón al dueño, el se calma y alegra, te dice que puedes comer algo")
                      print("gratis, le agradeces. Aunque dejó de llover ya es tarde para ir a la escuela,")
                      print("pero al menos tienes un nuevo amigo.")
                      print("")
                      print("Fin :D")
                      print("")
                      import sys
                      sys.exit()   
                          
                  elif accion3_2 == "decirle":  
                      print("")
                      print("El dueño de la tienda se molesta más contigo y te pide que te vayas,")
                      print("ahora estas mojado por la lluvia, es tarde para ir a la escuela y no queda más que irte")
                      print("a casa de nuevo... pero ahora con hambre.")  
                      print("")
                      print("Fin -_-")
                      print("")
                      import sys
                      sys.exit()
                  
                  elif accion3_2 == "robar":    #eso está un poco feo :v
                      print("") 
                      print("Agarras unos doritos y sales corriendo de la tienda, sigue lloviendo así que te")
                      print("empapas todo. El dueño de la tienda ha llamado a la policía, los cuales te")
                      print("arrestán, tu mamá te va a buscar y se molesta MUCHO.")
                      print("Terminas castigado y tu mamá tuvo que pagar una multa.")
                      print("")
                      print("Fin...")
                      print("")
                      import sys
                      sys.exit() 
                  else:
                      print("Tienes que arregla la situación!!")   
                
            else:
                print("Tienes que responderle al dueño.")
    
    else:
        print("tienes que elegir entre SEGUIR o RESGUARDARTE")  