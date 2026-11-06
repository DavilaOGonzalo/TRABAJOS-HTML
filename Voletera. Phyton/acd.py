# Clase Curso
class Curso:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

# Clase Estudiante
class Estudiante:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        self.cursos = []

    def inscribirse(self, curso):
        self.cursos.append(curso)
        print(f"{self.nombre} se ha inscrito en {curso.nombre}.")

    def mostrar_cursos(self):
        print(f"\nCursos de {self.nombre}:")
        if not self.cursos:
            print("No está inscrito en ningún curso.")
        else:
            for curso in self.cursos:
                print(f"- {curso.nombre} ({curso.codigo})")

# Lista para almacenar cursos
cursos_disponibles = []

# Crear cursos
cantidad_cursos = int(input("¿Cuántos cursos deseas registrar?: "))
for i in range(cantidad_cursos):
    print(f"\nCurso #{i+1}")
    nombre = input("Nombre del curso: ")
    codigo = input("Código del curso: ")
    nuevo_curso = Curso(nombre, codigo)
    cursos_disponibles.append(nuevo_curso)

# Crear estudiante
nombre_est = input("\nNombre del estudiante: ")
dni_est = input("DNI del estudiante: ")
estudiante = Estudiante(nombre_est, dni_est)

# Mostrar cursos disponibles
print("\nCursos disponibles:")
for i, curso in enumerate(cursos_disponibles):
    print(f"{i+1}. {curso.nombre} ({curso.codigo})")

# Inscripción a cursos
while True:
    seleccion = input("Escribe el número del curso al que te quieres inscribir (o 'fin' para terminar): ")
    if seleccion.lower() == 'fin':
        break
    try:
        indice = int(seleccion) - 1
        if 0 <= indice < len(cursos_disponibles):
            estudiante.inscribirse(cursos_disponibles[indice])
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, escribe un número válido o 'fin'.")

# Mostrar los cursos inscritos
estudiante.mostrar_cursos()