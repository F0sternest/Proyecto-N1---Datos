import time
import networkx as nx
import math
from os import system
from Arbol import *
from Persona import *
from pyvis.network import Network

# Declaramos las variables que utilizaremos en el proyecto
salir = False
opcion = 0
arreglo_arbol = []
raiz_existe = False

# Funcion para el reporte femenino

def reporteFem(Arreglo):
    for i in range(len(Arreglo)):
        if Arreglo[i].genero == 'F':
            print(Arreglo[i].nombre)

# Funcion para el reporte masculino

def reporteMas(Arreglo):
    for i in range(len(Arreglo)):
        if Arreglo[i].genero == 'M':
            print(Arreglo[i].nombre)

# Funcion para el reporte de los padres con su hijo

def reportePadresHijos(Arreglo):
    aux = Arreglo
    if aux.izquierda != None and aux.derecha != None:
        print("Hijo: ", aux.persona.nombre)
        print("Madre: ", aux.izquierda.persona.nombre)
        print("Padre: ", aux.derecha.persona.nombre)
        print()
        reportePadresHijos(aux.izquierda)
        reportePadresHijos(aux.derecha)

# Funcion para el reporte de la nacionalidad

def reporteNacionalidad(Arreglo):
    for i in range(len(Arreglo)):
        print("Nodo actual: ", Arreglo[i].nombre)
        print("Nacionalidad: ", Arreglo[i].nacionalidad)
        print()

# Funcion para el reporte del mayor edad

def reporteMayorEdad(Arreglo):
    mayor = 0
    for i in range(len(Arreglo)):
        if int(Arreglo[i].edad) >= mayor:
            mayor = int(Arreglo[i].edad)
            nombreMayor = Arreglo[i].nombre
    print(f"La persona con mayor edad es {nombreMayor} con {mayor} años")

# Funcion para el reporte del menor edad

def reporteMenorEdad(Arreglo):
    menor = 1000
    for i in range(len(Arreglo)):
        if int(Arreglo[i].edad) <= menor:
            menor = int(Arreglo[i].edad)
            nombreMenor = Arreglo[i].nombre
    print(f"La persona con menor edad es {nombreMenor} con {menor} años")

# Metodo que valida que la entrada del usuario sea un entero y regresa ese entero

def pedirOpcion():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input("Elige una opcion: "))
            correcto = True
        except ValueError:
            print('Error, introduce una de las opciones disponibles')

    return num


while not salir:
    system("cls")
    print("-----ARBOL GENEALOGICO-----")
    print("1. Hoja de Presentacion")
    print("2. Crear Arbol Genealogico")
    print("3. Insertar en Ascendientes")
    print("4. Imprimir el Arbol")
    print("5. Generar reportes")
    print("6. Salir")

    opcion = pedirOpcion()  # opcion guarda el numero ingresado por el usuario

    if opcion == 1:
        system("cls")
        print("                   UNIVERSIDAD TECNOLOGICA DE PANAMA")
        print("          FACULTAD DE INGENIERIA DE SISTEMAS COMPUTACIONALES")
        print("         DEPARTAMENTO DE COMPUTACION Y SIMULACION DE SISTEMAS")
        print("")
        print("                LIC. EN ING. SISTEMAS Y COMPUTACION")
        print("                      ESTRUCTURAS DE DATOS II")
        print("")
        print("                         ARBOL GENEALOGICO")
        print("")
        print("Prof. Yolanda de Miguelena                  Integrantes: Cesar Garzon")
        print("                                                         Kevin Rodriguez")
        print("                                                         Johan Pimentel")
        print("                                                         Gabriel Nunez")
        print("")
        print("                            Grupo: 1IL124")
        print("")
        print("                        FECHA: 30 / Sep / 2022")

        input()

    elif opcion == 2:
        if not raiz_existe:
            system("cls")
            print("CREACION DEL ARBOL GENEALOGICO")

            # Pedimos cada dato necesario para crear nuesto nodo
            print("Porfavor ingrese los siguientes datos para generar el primer integrante del arbol genealogico: \n")
            persona_raiz = Persona(
                input("Introduzca el nombre de la persona: "),
                int(input("Introduzca la edad de la persona: ")),
                input("Introduzca el genero de la persona(F / M): "),
                input("Introduzca el estado de la persona (Vivo/a, Fallecido/a): "),
                input("Introduzca la nacionalidad de la persona: ")
            )

            # Creamos el arbol genealogico con su raiz y añadimos la raiz al arreglo
            arbol_genealogico = Arbol(persona_raiz)
            arreglo_arbol.append(persona_raiz)

            print("\nARBOL CREADO CON EXITO")
            raiz_existe = True
        else:
            print("El arbol ya fue creado")

        time_duration = 2.5
        time.sleep(time_duration)

    elif opcion == 3:
        # Hacemos un chek para saber si la raiz del arbol ya fue creada
        ingresar_otro = False
        if raiz_existe:
            while not ingresar_otro:
                system("cls")
                print("INSERTAR ASCENDIENTES")
                print(
                    "Porfavor ingrese los siguientes datos para ingresar a la nueva persona: \n")

                # Creamos el objeto de persona ascendiente
                persona_ascendiente = Persona(
                    input("Introduzca el nombre de la persona: "),
                    int(input("Introduzca la edad de la persona: ")),
                    input("Introduzca el genero de la persona(F / M): "),
                    input("Introduzca el estado de la persona (Vivo/a, Fallecido/a): "),
                    input("Introduzca la nacionalidad de la persona: ")
                )

                # Insertando a una nueva persona a el arbol y al arreglo
                arbol_genealogico.insertar(
                    persona_ascendiente,
                    input(
                        "Ingrese el nombre de el hijo o descendinte de la persona que acaba de ingresar: ")
                )
                arreglo_arbol.append(persona_ascendiente)
                print("\nPERSONA INSERTADA CON EXITO")

                salir_ingresar = int(
                    input("\nDesea ingresar a otra persona?\n1. Si\n2. No\n"))
                if salir_ingresar == 2:
                    ingresar_otro = True
                    print("\nRegrsando al menu principal")
        else:
            print("Porfavor cree a la primera persona del arbol (opcion 2) \nantes de insertar nuevas personas al arbol")

        time_duration = 2.5
        time.sleep(time_duration)

    elif opcion == 4:
        if raiz_existe:
            # Creando la red para el arbol
            grafico_arbol = nx.balanced_tree(
                2, int(math.log(len(arreglo_arbol)+1, 2)-1))

            # Añadiendo los nodos al arbol
            for x in range(len(arreglo_arbol)):
                grafico_arbol.add_node(
                    x, label=arreglo_arbol[x].nombre, title=f"{arreglo_arbol[x].edad}\n{arreglo_arbol[x].genero}\n{arreglo_arbol[x].estado}\n{arreglo_arbol[x].nacionalidad}", size=20)

            # Creando y mostrando el canvas donde esta la red del arbol
            canvas = Network("650px", "650px")
            canvas.from_nx(grafico_arbol)
            canvas.show("Arbol Genealogico.html")
        else:
            print("Porfavor cree el arbol antes de imprimir el arbol")
            time_duration = 2.5
            time.sleep(time_duration)

    elif opcion == 5:
        if raiz_existe:
            print("Reportes")

            while True:
                print("1. Nombre de las progénitoras Femeninos.")
                print("2. Nombre de los progénitores Masculinos.")
                print("3. Todos los padres con sus hijos.")
                print("4. La nacionalidad de los descendientes.")
                print("5. El progenitor de mayor edad.")
                print("6. El Progenitor de menor edad")
                print("7. Salir")

                opcion = pedirOpcion()

                if opcion == 1:
                    system("cls")
                    print("El nombre las Progenitoras Femeninas son: ")
                    reporteFem(arreglo_arbol)
                    print()
                elif opcion == 2:
                    system("cls")
                    print("El nombre los Progenitoros Masculinos son: ")
                    reporteMas(arreglo_arbol)
                    print()
                elif opcion == 3:
                    system("cls")
                    reportePadresHijos(arbol_genealogico.raiz)
                elif opcion == 4:
                    system("cls")
                    reporteNacionalidad(arreglo_arbol)
                    print()
                elif opcion == 5:
                    system("cls")
                    reporteMayorEdad(arreglo_arbol)
                    print()
                elif opcion == 6:
                    system("cls")
                    reporteMenorEdad(arreglo_arbol)
                    print()
                elif opcion == 7:
                    break
        else:
            print("Porfavor cree el arbol antes de generar los reportes.")
        
        time_duration = 2.5
        time.sleep(time_duration)

    elif opcion == 6:
        salir = True
    else:
        system("cls")
        print("Introduce un numero entre 1 y 6")

print("Gracias")
