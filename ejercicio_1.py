#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo 
# es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
#  Escribir un programa que pregunte por un número de teléfono con este formato en la consola y
#  muestre por pantalla el número de teléfono sin el prefijo y la extensión.

def main():

    telefono_completo = input("Ingrese un numero de telefono con el siguiente formato (prefijo-número-extensión, por ejemplo: +34-913724710-56): ")
    numero_telefono = telefono_completo[4:-3]
    
    print(numero_telefono)

    return numero_telefono

if __name__ == '__main__':
    main()