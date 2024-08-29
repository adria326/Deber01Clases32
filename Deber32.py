usuarios = ["Ana", "Luis", "Carlos"]
cuentas = [1000.0, 500.0, 750.0]

# Variable global para el PIN
pin = "1234"  # PIN inicial predeterminado


def cambiar_pin():
    global pin
    pin_actual = input("Introduce tu PIN actual: ")
    
    if pin_actual == pin:
        nuevo_pin = input("Introduce tu nuevo PIN: ")
        confirmar_pin = input("Confirma tu nuevo PIN: ")
        
        if nuevo_pin == confirmar_pin:
            pin = nuevo_pin
            print("Tu PIN ha sido cambiado exitosamente.")
        else:
            print("Los PINs no coinciden. Intenta de nuevo.")
    else:
        print("El PIN actual es incorrecto.")

def consultar_saldo():
    nombre = input("Introduce tu nombre de usuario: ")
    
    if nombre in usuarios:
        indice = usuarios.index(nombre)
        saldo = cuentas[indice]
        print(f"El saldo de {nombre} es: {saldo}")
    else:
        print("Usuario no encontrado.")


def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Consultar saldo")
        print("2. Retirar dinero")
        print("3. Cambiar PIN")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            consultar_saldo()
        elif opcion == "2":
            # Lógica para retirar dinero
            pass
        elif opcion == "3":
            cambiar_pin()
        elif opcion == "4":
            print("Gracias por usar el cajero automático.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


menu()