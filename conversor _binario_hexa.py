print("""\t\tBienvenido al programa de conversión 
\t\t\tBinaria y Hexadecimal""")

while(True):
    print("""Seleccione la acción que desee:
    1) Entero a Binario
    2) Entero a Hexadecimal
    3) Binario a Entero
    4) Hexadecimal a Entero
    5) Salir""")
    opcion = input()
    if opcion == '1':
        binario()
    elif opcion == '2':
        hexadecimal()
    elif opcion == '3':
        entero_binario()
    elif opcion == '4':
        entero_hexadecimal()
    elif opcion == '5':
        print("¡Hasta luego! Ha sido un placer ayudarte")
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")


def binario():
    binario = int(input("Introduce el número a convertir: "))
    print(bin(binario))

def hexadecimal():
    hexadecimal = int(input("Introduce el número a convertir: "))
    print(hex(hexadecimal))

def entero_binario():
    ent_bi = input("Introduce el número a convertir: ")
    print(int(ent_bi,2))

def entero_hexadecimal():
    ent_hexa = input("Introduce el número a convertir: ")
    print(int(ent_hexa,16))
