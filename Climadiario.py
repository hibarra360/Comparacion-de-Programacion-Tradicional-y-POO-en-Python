class ClimaDiario:
    def __init__(self, dia, temperatura):
        self.dia = dia
        self.temperatura = temperatura

    def __str__(self):
        return f"Día {self.dia}: {self.temperatura}°C"

class SemanaClimatica:
    def __init__(self):
        self.dias = []

    def agregar_dia(self, clima_diario):
        self.dias.append(clima_diario)

    def calcular_promedio(self):
        total_temperatura = sum(dia.temperatura for dia in self.dias)
        return total_temperatura / len(self.dias)

    def mostrar_temperaturas(self):
        for dia in self.dias:
            print(dia)

def main():
    semana = SemanaClimatica()
    DIAS_SEMANA = 7

    for i in range(DIAS_SEMANA):
        temperatura = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        clima_diario = ClimaDiario(i + 1, temperatura)
        semana.agregar_dia(clima_diario)

    semana.mostrar_temperaturas()
    promedio = semana.calcular_promedio()
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
