## Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes: (IMAGEN ADJUNTA). 
## Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla lo que tiene que pagar.

def main():
    renta_anual = int(input("Ingrese su renta anual: "))

    if (renta_anual < 10000):
        renta_anual_total = (float(renta_anual) * 0.05) 
    elif (renta_anual > 10000 and renta_anual < 20000):
        renta_anual_total = (float(renta_anual) * 0.15)
    elif (renta_anual > 20000 and renta_anual < 35000):
        renta_anual_total = (float(renta_anual) * 0.20)
    elif (renta_anual > 35000 and renta_anual < 60000):
        renta_anual_total = (float(renta_anual) * 0.30)
    else:
        renta_anual_total = (float(renta_anual) * 0.45)

    renta_anual_total=int(renta_anual_total)
    
    print("El monto que le toca pagar es de: "+str(renta_anual_total))

if __name__ == '__main__':
    main()