#Introduce una frase y cuenta las vocales que tiene - Israel

frase = str(input("Ingrese una frase y contare las vocales por ti: "))
numVocal = 0
vocales = "aeiouáéíóú"

for caracter in frase.lower():
    if caracter in vocales:
        numVocal += 1
        
print("El numero total de vocales en tu frase son: ", numVocal)