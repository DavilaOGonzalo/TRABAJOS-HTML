class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: S/ {self.saldo}")
        else:
            print("El monto debe ser positivo.")

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: S/ {self.saldo}")
        else:
            print("Fondos insuficientes.")

    def mostrar_saldo(self):
        print(f"{self.titular}, tu saldo actual es: S/ {self.saldo}")

# Interacción
nombre = input("Ingrese el nombre del titular: ")
cuenta = CuentaBancaria(nombre)

while True:
    print("\nOpciones:")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Mostrar saldo")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        monto = float(input("Monto a depositar: "))
        cuenta.depositar(monto)
    elif opcion == "2":
        monto = float(input("Monto a retirar: "))
        cuenta.retirar(monto)
    elif opcion == "3":
        cuenta.mostrar_saldo()
    elif opcion == "4":
        print("Gracias por usar el sistema bancario.")
        break
    else:
        print("Opción inválida.")