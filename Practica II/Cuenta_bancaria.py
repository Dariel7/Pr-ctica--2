class CuentaBancaria:
    def __init__(self):
        self.numero_cuenta = input("Ingrese el número de cuenta: ")
        self.titular = input("Ingrese el titular de la cuenta: ")
        self.saldo = 10000  # Inicializamos el saldo en cero

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito de ${monto} realizado. Nuevo saldo: ${self.saldo}")
        else:
            print("El monto debe ser mayor que cero.")

    def retirar(self, monto):
        if monto > 0 and monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro de ${monto} realizado. Nuevo saldo: ${self.saldo}")
        else:
            print("Monto inválido o insuficiente saldo.")

    def calcular_interes(self, tasa_interes):
        interes = (self.saldo * tasa_interes) / 100
        return interes

    def imprimir_informacion(self):
        print("Número de Cuenta:", self.numero_cuenta)
        print("Titular:", self.titular)
        print("Saldo actual: ${}".format(self.saldo))

# Ejemplo de uso
cuenta = CuentaBancaria()
cuenta.imprimir_informacion()

opcion = input("¿Desea realizar un depósito (D) o un retiro (R)? ").upper()

if opcion == "D":
    monto = float(input("Ingrese la cantidad a depositar: "))
    cuenta.depositar(monto)
elif opcion == "R":
    monto = float(input("Ingrese la cantidad a retirar: "))
    cuenta.retirar(monto)
else:
    print("Opción no válida.")

tasa_interes = 2.5  # Porcentaje de interés
interes = cuenta.calcular_interes(tasa_interes)
print("Interés acumulado: ${}".format(interes))
