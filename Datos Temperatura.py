# Definición de funciones
def ingresar_temperaturas(dias):
    temperaturas = []
    for i in range(dias):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas


def calcular_promedio(temperaturas):
    suma = sum(temperaturas)
    return suma / len(temperaturas)


def main():
    DIAS_SEMANA = 7
    # Ingresar temperaturas diarias
    temperaturas = ingresar_temperaturas(DIAS_SEMANA)

    # Calcular y mostrar el promedio semanal
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}")


if __name__ == "__main__":
    main()
