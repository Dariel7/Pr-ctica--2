class Empleado:

    def __init__(self):
        self.nombre = input("Ingrese el nombre del empleado: ")
        self.apellidos = input("Ingrese los apellidos del empleado: ")
        self.edad = int(input("Ingrese la edad del empleado: "))
        self.sexo = input("Ingrese el sexo del empleado: ")
        self.direccion = input("Ingrese la dirección del empleado: ")
        self.email = input("Ingrese el email del empleado: ")
        self.sueldo = float(input("Ingrese el sueldo del empleado: "))

    def asignar_sueldo(self, nuevo_sueldo):
        self.sueldo = nuevo_sueldo
        print(f"Sueldo asignado: ${self.sueldo}")

    def calcular_afp(self):
        afp = self.sueldo * 0.0287
        return afp

    def calcular_sfs(self):
        sfs = self.sueldo * 0.0304
        return sfs

    def calcular_irs(self):
        

        ingresos_brutos = self.sueldo

        if ingresos_brutos <= 416220.00:
            irs = 0.00
        elif ingresos_brutos <= 624329.00:
            irs = ingresos_brutos * 0.15 - 6243.29
        elif ingresos_brutos <= 867123.00:
            irs = 31216.00 + ingresos_brutos * 0.20
        else:
            irs = 31216.00 + 21076.00 + ingresos_brutos * 0.25

        return irs

    def calcular_total_deducciones(self):
        total_deducciones = self.calcular_afp() + self.calcular_sfs() + self.calcular_irs()
        return total_deducciones

    def calcular_sueldo_neto(self):
        sueldo_neto = self.sueldo - self.calcular_total_deducciones()
        return sueldo_neto

    def imprimir_informacion(self):
        print("Nombre:", self.nombre)
        print("Apellidos:", self.apellidos)
        print("Edad:", self.edad)
        print("Sexo:", self.sexo)
        print("Dirección:", self.direccion)
        print("Email:", self.email)
        print("Sueldo: ${}".format(self.sueldo))


empleado = Empleado()
empleado.imprimir_informacion()


nuevo_sueldo = float(input("Ingrese el nuevo sueldo: "))
empleado.asignar_sueldo(nuevo_sueldo)

# Calcular y mostrar deducciones
afp = empleado.calcular_afp()
sfs = empleado.calcular_sfs()
irs = empleado.calcular_irs()

print("Deducciones:")
print("AFP: ${}".format(afp))
print("SFS: ${}".format(sfs))
print("IRS: ${}".format(irs))

# Calcular y mostrar sueldo neto
sueldo_neto = empleado.calcular_sueldo_neto()
print("Sueldo neto: ${}".format(sueldo_neto))
