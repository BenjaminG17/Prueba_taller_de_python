# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
# Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

def main():
    lista = ["Matemáticas","Física","Lengua"]
    #largo = len(lista) + 1
    
    for i in range(len(lista)-1,-1,-1):
        nota = input("Ingrese su nota para "+lista[i] + ": ")
        nota = nota.replace('.','')
        nota = int(nota)
        # print("Su nota es "+ str(nota))

        if(nota >= 40):
            lista.pop(i)   
    
    print("El o los ramos que reprobo fueron los siguientes: "+str(lista))
        
if __name__ == "__main__":
    main()