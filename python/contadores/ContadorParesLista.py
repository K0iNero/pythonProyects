#Ingresas una lista de numeros (2,3,5,6,1,2) y el programa cuenta los numeros pares y te los devuelve en una nueva lista

input = input("Introduce una lista de numeros separados por coma (2,3,5,6,1,2): ").strip()
lista = input.split(",")
pares = []

for num in lista:
    try:
        num = int(num.strip())
        if num % 2 == 0:
            pares.append(num)
    except ValueError:
        print("Introduce un valor valido.")

print(pares)
