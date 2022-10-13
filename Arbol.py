from Nodo import *


class Arbol:
    # Metodo constructor de la clase
    def __init__(self, persona):
        self.raiz = Nodo(persona)

    # Metodo de ayuda para poder ingresar una nueva persona
    def insertar(self, persona, descendiente):
        self.insertar_recursivo(self.raiz, persona, descendiente)

    # Metodo para insertar a una nueva persona
    def insertar_recursivo(self, nodo, persona, descendiente):
        if nodo is not None:
            # Nos movemos hacia el nodo mas a la izquierda del arbol
            self.insertar_recursivo(nodo.izquierda, persona, descendiente)
            if (nodo.persona.nombre == descendiente):
                print(f"El genero de {persona.nombre} es {persona.genero}")
                if (persona.genero == 'F' or persona.genero == 'f'):
                    print("Entramos en femenino")
                    if nodo.izquierda is None:
                        print("Creamos el nodo a la izquierda")
                        # Creamos el nuevo nodo con la informacion de persona
                        nodo.izquierda = Nodo(persona)
                    else:
                        print(
                            f"{nodo.persona.nombre} ya tiene una madre asignada")
                else:
                    print("Entramos en masculino")
                    if nodo.derecha is None:
                        print("Creamos el nodo a la derecha")
                        # Creamos el nuevo nodo con la informacion de persona
                        nodo.derecha = Nodo(persona)
                    else:
                        print(f"{nodo.persona.nombre} ya tiene un padre asignado")
            # Nos movemos por los nodos de la derecha
            self.insertar_recursivo(nodo.derecha, persona, descendiente)

    # Metodo de ayuda para el recorrido inorden
    def inorden(self):
        print("Imprimiendo inorden: ")
        self.inorden_recursivo(self.raiz)
        print("")

    # Recorrido inorden del arbol generado
    def inorden_recursivo(self, nodo):
        if nodo is not None:
            self.inorden_recursivo(nodo.izquierda)
            print(nodo.persona.nombre, end=", ")
            self.inorden_recursivo(nodo.derecha)
