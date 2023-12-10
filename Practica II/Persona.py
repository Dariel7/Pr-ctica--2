class Persona:

    def __init__(self):
        self.nombre = input("Ingrese su nombre: ")
        self.apellido = input("Ingrese su apellido: ")
        self.edad = input("Ingrese su edad: ")
        self.sexo = input("Ingrese su sexo: ")
        self.direccion = input("Ingrese su dirección: ")

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Apellido: ", self.apellido)
        print("Edad: ", self.edad)
        print("Sexo: ", self.sexo)
        print("Dirección: ", self.direccion)

persona = Persona()
persona.imprimir()