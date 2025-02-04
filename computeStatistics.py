import sys
import time
from PyQt6.QtWidgets import QApplication, QMessageBox

if len(sys.argv) != 2:
    print("Uso: python estadisticas.py archivo.txt")
    sys.exit(1)

inicio = time.time()
archivo_entrada = sys.argv[1]

try:
    with open(archivo_entrada, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
except FileNotFoundError:
    print("Error: Archivo no encontrado.")
    sys.exit(1)

numeros = []
for linea in lineas:
    try:
        numeros.append(float(linea.strip()))
    except ValueError:
        continue

if not numeros:
    print("No se pudieron calcular las estadísticas. Verifica el archivo de entrada")
    sys.exit(1)

# Cálculo de la media
suma_total = sum(numeros)
conteo = len(numeros)
media = suma_total / conteo

# Cálculo de la mediana
numeros_ordenados = sorted(numeros)
mitad = conteo // 2
if conteo % 2 == 0:
    mediana = (numeros_ordenados[mitad - 1] + numeros_ordenados[mitad]) / 2
else:
    mediana = numeros_ordenados[mitad]

# Cálculo de la moda
frecuencias = {}
for num in numeros:
    if num in frecuencias:
        frecuencias[num] += 1
    else:
        frecuencias[num] = 1

max_frecuencia = max(frecuencias.values())
moda = [num for num, freq in frecuencias.items() if freq == max_frecuencia]
moda = moda[0] if len(moda) == 1 else "No hay moda única"

# Cálculo de la varianza
suma_cuadrados = sum((x - media) ** 2 for x in numeros)
varianza = suma_cuadrados / conteo if conteo > 1 else 0

# Cálculo de la desviación estándar
desviacion_estandar = varianza ** 0.5

with open('StatisticsResults.txt', 'a', encoding='utf-8') as archivo:
    archivo.write(f"Media: {media:.2f}\n")
    archivo.write(f"Mediana: {mediana:.2f}\n")
    archivo.write(f"Moda: {moda}\n")
    archivo.write(f"Varianza: {varianza:.2f}\n")
    archivo.write(f"Desviación estándar: {desviacion_estandar:.2f}\n")
    archivo.write("============================\n")

fin = time.time()
tiempo_ejecucion = fin - inicio

resultado_texto = (
    f"Media: {media:.2f}\n"
    f"Mediana: {mediana:.2f}\n"
    f"Moda: {moda}\n"
    f"Varianza: {varianza:.2f}\n"
    f"Desviación estándar: {desviacion_estandar:.2f}\n"
    f"Tiempo de ejecución: {tiempo_ejecucion:.6f} segundos"
)

app = QApplication(sys.argv)
mensaje = QMessageBox()
mensaje.setWindowTitle("Resultados")
mensaje.setText(resultado_texto)
mensaje.exec()