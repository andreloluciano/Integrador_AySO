# lista vacia
notas = []

# pedimos datos al usuario
for i in range (3):
	nota = float(input(f"Ingrese la nota {i + 1}: "))
	notas.append(nota)

# calcular promedio
promedio = sum(notas) / len(notas)

# mostrar resultado
print(f"Las notas son {notas}, y el promedio es {promedio}")
