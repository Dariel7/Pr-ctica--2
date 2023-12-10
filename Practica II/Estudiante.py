class Estudiante:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del estudiante: ")
        self.apellido = input("Ingrese el apellido del estudiante: ")
        self.edad = input("Ingrese la edad del estudiante: ")
        self.sexo = input("Ingrese el sexo del estudiante: ")
        self.direccion = input("Ingrese la dirección del estudiante: ")
        self.carrera = input("Ingrese la carrera del estudiante: ")
        self.email = input("Ingrese el email del estudiante: ")
        self.telefono = input("Ingrese el teléfono del estudiante: ")

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Apellido: ", self.apellido)
        print("Edad: ", self.edad)
        print("Sexo: ", self.sexo)
        print("Dirección: ", self.direccion)
        print("Carrera: ", self.carrera)
        print("Email: ", self.email)
        print("Teléfono: ", self.telefono)


estudiante = Estudiante()
estudiante.imprimir()