notas=""
cantidadnotas=int(input("Cuántas notas? "))
dec=int(input("Introduce los decimales: "))


for i in range (cantidadnotas):
    nota=float(input("Introduce la nota: "))
    nota=round(nota, dec)
    notas= str(notas) + " " + str(nota)

print(notas[1:])