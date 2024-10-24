#Calculadora simple - Israel

operando = "1"
while operando!="0": 
    
    try:
        num1 = int(input("Introduce el primer número: "))
        num2 = int(input("Introduce el segundo número: "))
        
        operando = str(input("Ahora escoge la operación que deseas hacer (+, -, x, /): "))
        resultado = 0
        match operando:
            case "+":
                resultado = num1 + num2
                print("El resultado de tu operación es:", resultado)
            case "-":
                resultado = num1 - num2
                print("El resultado de tu operación es:", resultado)
            case "x":
                resultado = num1 * num2
                print("El resultado de tu operación es:", resultado)
            case "/":
                if num2!=0:
                    resultado = num1 / num2
                    print("El resultado de tu operación es:", resultado)
                else:
                    print("No se puede dividir entre cero.")
            case "0":
                print("Saliendo de la calculadora...")
                break
            case _:
                print("Operación no valida. Introduce una de las propuestas.")
    except ValueError:
        print("Introduce numeros validos.")
