from recetas import receta_pasta
#Aquí se irán importando más recetas a medida que se agreguen

def mostrar_menu():
	print("Recetario disponible:")
	print("1. Pasta de ajo")
	#Agrega aquí tu receta con un número nuevo

	opcion = input("Elige una receta (número): ")

	if opcion == "1":
		receta_pasta()
	else:
		print("Opción no válida. Intenta de nuevo. ")

if __name__ == "__main__":
	mostrar_menu()

---

### recetas.py

# Aquí van las recetas de todos los participantes

def receta_pasta():
    print(" Receta: Pasta al ajo")
    print("Ingredientes: pasta, tomate, ajo, aceite de oliva")
    print("Pasos:")
    print("1. Hervir la pasta.")
    print("2. Freír el ajo y tomate en aceite.")
    print("3. Mezclar todo y servir caliente.")

# Agrega tu receta debajo de esta línea
# Ejemplo:
# def receta_tacos():
#     print(" Receta: Tacos de pollo")
#     print("Ingredientes: tortillas, pollo, cebolla, cilantro")
#     print("Pasos: Cocinar el pollo, calentar las tortillas, armar los tacos.")
