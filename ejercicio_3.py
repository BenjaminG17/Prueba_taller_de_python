# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
# Aclaración: El programa debe imprimir por la consola el mismo texto que el usuario introduce hasta que éste escriba la palabra "salir".

def main():

    estado=True

    while (estado):
        texto=input("Ingrese palabras: ")
        if (texto == "salir"):
            print("FIN")
            estado=False
        else:
            print(texto)

if __name__== '__main__':
    main()