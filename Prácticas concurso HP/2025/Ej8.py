x = float(input("De qué número quieres saber la raíz cuadrada?: "))
n = int(input("Itinerations: "))
aprox=x

for i in range (n):
    siguiente = (aprox + x / aprox)/2
    aprox=siguiente

print(round(siguiente, 6))
