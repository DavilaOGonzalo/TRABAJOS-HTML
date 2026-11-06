class Mascota:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

    def saludar(self):
        print(f"Hola, soy {self.nombre} y soy un {self.tipo}.")

class Veterinaria:
    def __init__(self):
        self.lista_mascotas = []

    def registrar_mascota(self, mascota):
        self.lista_mascotas.append(mascota)
        print(f"{mascota.nombre} ha sido registrada en la veterinaria.")

    def mostrar_mascotas(self):
        print("\nMascotas registradas:")
        for mascota in self.lista_mascotas:
            print(f"- {mascota.nombre}, {mascota.edad} años, {mascota.tipo}")

# Programa interactivo
veterinaria = Veterinaria()

while True:
    print("\n--- Registro de Mascotas ---")
    nombre = input("Nombre de la mascota: ")
    edad = int(input("Edad de la mascota: "))
    tipo = input("Tipo de mascota (perro, gato, etc): ")

    nueva_mascota = Mascota(nombre, edad, tipo)
    veterinaria.registrar_mascota(nueva_mascota)

    continuar = input("¿Deseas registrar otra mascota? (s/n): ")
    if continuar.lower() != 's':
        break

# Mostrar resultados
veterinaria.mostrar_mascotas()

# Saludos
print("\n--- Saludos de las mascotas ---")
for mascota in veterinaria.lista_mascotas:
    mascota.saludar()