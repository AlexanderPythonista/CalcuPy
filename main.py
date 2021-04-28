from time import sleep



print("                                                                                                                ")
print("░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██████╗░██╗░░░██╗")
print("██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██╔══██╗╚██╗░██╔╝")
print("██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██████╔╝░╚████╔╝░")
print("██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██╔═══╝░░░╚██╔╝░░")
print("╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝██║░░░░░░░░██║░░░")
print("░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚═╝░░░░░░░░╚═╝░░░")
sleep(3)
print("\nBienvenid@ soy CalcuPy, estoy hecho en python...... Que deseas hacer?\n")







sleep(2)

print("Opciones Disponibles:\n")
sleep(2)
print("* Presione 'Y' para empezar CalcuPy\n")
sleep(2)
print("* Presione 'N' para cancelar inicio  de CalcuPy   \n ")
sleep(2)
print("* Presione 'C' par ver los creditos de CalcuPy\n")
sleep(2)



yes = str(input("¿Que deseas hacer?:  "))
yes_lower = yes.lower()
        
sleep(1)       
print("Comenzamos con las operaciones a continuacion ingresa los numeros de tu preferencia")
sleep(1)        
def calculator():
    sleep(1)
    num_uno= int(input("\nIngrese el Primer Numero:  "))
    sleep(1)
    num_dos= int(input("\ningrese el Segundo Numero:  "))
    
    sleep(2)
    print("\n espere un momento CalcuPy esta cargando\n")
    sleep(2)

    print("    Elige una operacion matematica\n")
    sleep(1)
    print("1.- Suma\n")
    sleep(1)
    print("2.- Resta \n")
    sleep(1)
    print("3.- Multiplicacion\n")
    sleep(1)
    print("4.- Division            \n") 
    sleep(1)
    print("5.- Modulo o resto\n")
    sleep(1)
   
    
    global operacion 
    operacion = int(input("Eliga una de las anteriores opciones: ")) 
   
    try:
        
        if operacion == 1:
            sleep(3)
            print("\nHas elegido suma\n")
            sleep(1)
            complete=f"La operacion {num_uno} + {num_dos} da como resultado: "
            print(complete)
            print(num_uno + num_dos)
        elif operacion == 2:
            sleep(3)
            print("\nHas elegido Resta\n")
            complete=f"La operacion {num_uno} + {num_dos} da como resultado: "
            sleep(1)
            print(complete)
            print(num_uno - num_dos)
        elif operacion == 3:
            sleep(3)
            print("\nHas elegido Multiplicacion\n")
            complete=f"La operacion {num_uno}  {num_dos} da como resultado: "
            sleep(1)
            print(complete)
            print(num_uno * num_dos)
        elif operacion == 4:
            sleep(1)
            print("\nHas elegido Division\n")
            complete=f"La operacion {num_uno} / {num_dos} da como resultado: "
            sleep(3)
            print(complete)
            print(num_uno / num_dos)
        elif operacion == 5:
            sleep(1)
            print("\nHas elegido Modulo o exponte\n")
            complete=f"La operacion {num_uno} % {num_dos} da como resultado: "
            sleep(3)
            print(complete)
            print(complete , num_uno % num_dos)
        
        else:
            sleep(1)
            print("No hay opciones disponibles......\n")
            print("Bye see you later")
            sleep(2)
        print("Chao Gracias, ahora me siento usado XD. Si te gusto Felicita a Alexander")
            
            
        
        

        
    except:
        print("El valor debe ser int(numero)")
        num_uno= int(input("Ingrese el Primer numero"))
        print("Saliendo")
          









if yes_lower == "y" :
    sleep(5)
    calculator()
elif yes_lower =="c" :
    sleep(1)
    print("\nCreado por AlexanderG, el 28/04/21 para el reto de sendero tecnologico\n")
    sleep(1)
    print("Hecho con amor, en python\n")
    
else:
    print("Bye")
       





