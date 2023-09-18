import csv
import os


def merge_csv_files(input_folder, output_file):
    print("Iniciando la fusión de archivos CSV...")

    # Obtiene una lista de todos los archivos CSV en la carpeta
    csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]

    print(f"Se encontraron {len(csv_files)} archivos CSV para fusionar.")

    # Abre el archivo de salida para escritura
    with open(output_file, 'w', newline='', encoding='utf-8') as out_file:
        writer = csv.writer(out_file)

        print("Escribiendo cabeceras...")

        # Procesa el primer archivo para escribir las cabeceras
        first_file = True
        for index, csv_file in enumerate(csv_files):
            print(f"Procesando archivo {index + 1} de {len(csv_files)}: {csv_file}")

            with open(os.path.join(input_folder, csv_file), 'r', encoding='utf-8') as in_file:
                reader = csv.reader(in_file)

                # Escribe la cabecera solo del primer archivo
                if first_file:
                    writer.writerow(next(reader))
                    first_file = False
                else:
                    # Omite la cabecera de los archivos subsiguientes
                    next(reader)

                print(f"Escribiendo datos de {csv_file} al archivo de salida...")

                # Escribe las filas del archivo CSV al archivo de salida
                for row in reader:
                    writer.writerow(row)

    print("Fusión de archivos CSV completada.")


# Directorio donde se encuentran los archivos CSV a fusionar
input_folder = 'C:\\Users\\Javier Blanco\\Desktop\\excels'

# Nombre del archivo CSV de salida
output_file = 'C:\\Users\\Javier Blanco\\Desktop\\excels\\merged_file.csv'

# Llama a la función para realizar la fusión
merge_csv_files(input_folder, output_file)
