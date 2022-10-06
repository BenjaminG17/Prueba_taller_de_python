## Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y 
# devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, 
# deberá aplicar un 19%.

def main():
    
    factura=int(input("Ingrese la cantidad de la factura: "))
    iva=input("Ingrese el porcentaje de iva a aplicar: ")

    calcular_iva(factura,iva)

def calcular_iva(factura,iva):

    if iva == "":
        iva=0
        iva=int(iva)
        factura_con_iva=(factura*0.19)+ factura
        factura_con_iva=int(factura_con_iva)
        print (factura_con_iva)
    else:
        iva=int(iva)
        factura_con_iva=(factura*(iva/100)) + factura

        factura_con_iva=int(factura_con_iva)
        print (factura_con_iva)

    # if iva== 0:
    #     print("El total de la factura con el iva predeterminado es: ",iva)
    # else:
    #     print("El total de la factura con un iva de ",int(iva*100),"%","es de: ",int(factura_con_iva))
if __name__ == "__main__":
    main()