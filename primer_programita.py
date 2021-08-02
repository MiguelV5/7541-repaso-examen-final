#Hola mundo
def hola_mundo():
    print("hola mundo :)")

def sumar_enteros(a, b):
    return a+b

def suma_sarasa(a,b):
    print("Bienvenido al sumatron.\n")
    resultado = sumar_enteros(a,b)
    print("Impresion de suma con format: {} + {} = {}".format(a,b,resultado))
    print("Impresion de suma con str(): " + str(a) + " + " + str(b) + " = " + str(resultado))

def factorial(numero):
    if numero <= 0:
        return 1
    return numero*factorial(numero-1)

def factorial_iterativo(numero):
    acumulador = 1
    for i in range(1, numero+1):
        acumulador *= i
    return acumulador

def imprimir_lista(lista):
    print("\nCon un for item in lista:\n")
    for item in lista:
        print(item)
    print("\nCon un for x in range(len(lista)):\n")
    for x in range(len(lista)):
        print(lista[x])
    print("\nCon un for x in range(len(lista), -1, -1)   (o sea imprimir la lista al reves):\n")
    for x in range(len(lista)-1, -1, -1):
        print(lista[x])

def leer_archivo_e_imprimir(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    for linea in archivo:
        print(linea.split(";"))
    archivo.close()

def desafio_de_algo1_masomenos_hecho(string):
    lista_str_aux = []
    for i in range(0, len(string)-1):
        if string[i].isupper() and string[i+1].islower():
            lista_str_aux.append(string[i+1])
            lista_str_aux.append(string[i])
            lista_str_aux.append('#')
