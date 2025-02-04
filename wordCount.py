import sys
import time
import re
from PyQt6.QtWidgets import QApplication, QMessageBox

def read_file(filename):
    """Lee el contenido de un archivo y devuelve sus líneas."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.readlines()
    except Exception as e:
        print(f"Error al leer el archivo {filename}: {e}")
        return []

def process_text(lines):
    """Procesa las líneas de texto y cuenta la ocurrencia de cada palabra."""
    word_count = {}
    for line in lines:
        words = re.findall(r'\b\w+\b', line.lower())  # Extrae palabras, ignorando puntuación
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count

def write_results(word_count, elapsed_time):
    """Escribe los resultados de la frecuencia de palabras y el tiempo de ejecución en un archivo."""
    try:
        with open("WordCountResults.txt", "w", encoding='utf-8') as file:
            for word, count in sorted(word_count.items()):
                file.write(f"{word}: {count}\n")
            file.write(f"Tiempo de ejecución: {elapsed_time:.4f} segundos\n")
    except Exception as e:
        print(f"Error al escribir el archivo de resultados: {e}")

def display_results(word_count, elapsed_time):
    """Muestra los resultados de la frecuencia de palabras en una ventana gráfica."""
    app = QApplication(sys.argv)
    msg = QMessageBox()
    msg.setWindowTitle("Resultados del Conteo de Palabras")
    result_text = "\n".join([f"{word}: {count}" for word, count in sorted(word_count.items())])
    result_text += f"\nTiempo de ejecución: {elapsed_time:.4f} segundos"
    msg.setText(result_text)
    msg.exec()

def main():
    """Función principal para ejecutar el programa de conteo de palabras."""
    if len(sys.argv) != 2:
        print("Uso: python wordCount.py archivoDeDatos.txt")
        sys.exit(1)
    
    filename = sys.argv[1]
    start_time = time.time()
    lines = read_file(filename)
    word_count = process_text(lines)
    elapsed_time = time.time() - start_time
    
    print("Frecuencia de palabras:")
    for word, count in sorted(word_count.items()):
        print(f"{word}: {count}")
    print(f"Tiempo de ejecución: {elapsed_time:.4f} segundos")
    
    write_results(word_count, elapsed_time)
    display_results(word_count, elapsed_time)
    
if __name__ == "__main__":
    main()
