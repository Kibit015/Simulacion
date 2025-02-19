import random

def generar_numeros_aleatorios(cantidad, minimo, maximo):
    if cantidad <= 0:
        return [], 0
    numeros = random.choices(range(minimo, maximo + 1), k=cantidad)
    return numeros, sum(numeros) / cantidad

def solicitar_datos():
    while True:
        try:
            cantidad = int(input("\n¿Cuántos números aleatorios deseas generar? "))
            minimo = int(input("Ingresa el número mínimo permitido: "))
            maximo = int(input("Ingresa el número máximo permitido: "))

            if minimo > maximo:
                print("⚠️ Error: El valor mínimo no puede ser mayor que el máximo. Intenta nuevamente.")
                continue

            return cantidad, minimo, maximo

        except ValueError:
            print("⚠️ Entrada inválida. Asegúrate de ingresar solo números enteros.")

def mostrar_resultados(numeros, promedio):
    print("\n🔹 Números generados:", numeros[:10], "..." if len(numeros) > 10 else "")
    print(f"📊 Promedio de los números: {promedio:.2f}")

def main():
    cantidad, minimo, maximo = solicitar_datos()
    numeros, promedio = generar_numeros_aleatorios(cantidad, minimo, maximo)
    mostrar_resultados(numeros, promedio)

if __name__ == "__main__":
    main()
