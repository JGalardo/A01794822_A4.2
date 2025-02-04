import sys
import time
from PyQt6.QtWidgets import QApplication, QMessageBox

def to_binary(n):
    """Convierte un número a binario usando un algoritmo básico."""
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

def to_hexadecimal(n):
    """Convierte un número a hexadecimal usando un algoritmo básico."""
    hex_chars = "0123456789ABCDEF"
    if n == 0:
        return "0"
    hexadecimal = ""
    while n > 0:
        hexadecimal = hex_chars[n % 16] + hexadecimal
        n //= 16
    return hexadecimal

def process_file(file_path):
    """Procesa el archivo, convirtiendo números a binario y hexadecimal."""
    output_file = "ConvertionResults.txt"
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: Archivo '{file_path}' no encontrado.")
        return
    
    results = []
    errors = []
    start_time = time.time()
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        try:
            num = int(line)
            binary = to_binary(num)
            hexadecimal = to_hexadecimal(num)
            result = f"{num} -> Binario: {binary}, Hexadecimal: {hexadecimal}"
            results.append(result)
        except ValueError:
            error_msg = f"Dato inválido: '{line}' no es un número."
            errors.append(error_msg)
            print(error_msg)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    results.append(f"Tiempo de ejecución: {elapsed_time:.5f} segundos")
    
    # Guardar resultados en un archivo
    with open(output_file, "w", encoding="utf-8") as file:
        for res in results:
            file.write(res + "\n")
    
    for res in results:
        print(res)
    
    # Mostrar resultados en un cuadro de diálogo
    app = QApplication(sys.argv)
    msg = QMessageBox()
    msg.setWindowTitle("Resultados de Conversión")
    msg.setText("\n".join(results))
    msg.setIcon(QMessageBox.Icon.Information)
    msg.exec()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python convertNumbers.py fileWithData.txt")
    else:
        process_file(sys.argv[1])
