peliculas = ["Spider-Man", "Avatar 2", "Intensamente 2", "Godzilla vs Kong", "Puka"]
print("Bienvenido a mi cine espectacular")
print("Cartelera: ")



for i in range(4):
    print(f"{i+1}. {peliculas[i]}")
opcion = int(input("Elige el número de la película: "))
if 1 <= opcion <= len(peliculas):
    pelicula_seleccionada = peliculas[opcion - 1]
    print(f"Has seleccionado: {pelicula_seleccionada}")
    cantidad = int(input("¿Cuántos boletos deseas comprar? "))
    precio_por_boleto = 5  
    total = cantidad*precio_por_boleto
    print("RESUMEN DE COMPRA")
    print(f"Pelicula: {pelicula_seleccionada}")
    print(f"Cantidad de boletos: {cantidad}")
    print(f"Precio por boleto: ${precio_por_boleto}")
    print(f"Total a pagar: ${total}")
    print("¡Gracias por tu compra!")
else:
    print("Opción inválida. Por favor, intenta de nuevo.")