import os
import logging

# Configuración del logging
logging.basicConfig(filename='log.txt', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def recorrer_arbol_directorios(directory):
    try:
        content = os.listdir(directory)
        for element in content:
            rute_element = os.path.join(directory, element)
            if not os.path.islink(rute_element):
                if os.path.isdir(rute_element):
                    print("Directory:", rute_element)
                    recorrer_arbol_directorios(rute_element)
                else:
                    print("File:", rute_element)
    except PermissionError:
        error_message = f"No tienes permisos para acceder a la carpeta: {directory}"
        print(error_message)
        logging.error(error_message)
    except OSError as e:
        error_message = f"Error de E/S: {e}"
        print(error_message)
        logging.error(error_message)
    except RecursionError:
        error_message = f"Error: Recursión infinita detectada en la carpeta: {directory}"
        print(error_message)
        logging.error(error_message)
    except Exception as e:
        error_message = f"Error inesperado: {e}"
        print(error_message)
        logging.error(error_message)

def main():
    directorio_inicial = input("Introduce la ruta del directorio inicial: ")
    if not os.path.isdir(directorio_inicial):
        print("El directorio especificado no existe.")
    else:
        print("\nRecorrido del árbol de directorios:")
        recorrer_arbol_directorios(directorio_inicial)

if __name__ == "__main__":
    main()