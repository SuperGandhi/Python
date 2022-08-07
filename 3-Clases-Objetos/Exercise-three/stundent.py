# inicializamos la clase
class Alumno:
    # inicializamos los atributos
    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    # función para imprimir los datos
    def imprimir(self):
            print("Nombre: ",self.nombre)
            print("Nota: ",self.nota)

    # función para obtener el resultado
    def resultado(self):
            if self.nota >= 12:
                    print("El alumno está aprobado")
            else:
                    print("El alumno está desaprobado")



# bloque principal
# creamos los nuevos objetos
alumno1=Alumno()
alumno2=Alumno()

# inicializamos los atributos
alumno1.inicializar("ivan",8)
alumno2.inicializar("juan",4)

# imprimimos los datos y resultados de cada alumno
alumno1.imprimir()
alumno1.resultado()
alumno2.imprimir()
alumno2.resultado()