#!/bin/bash
echo "Iniciando el pipeline ELT..."

# Ejecutar cada script en secuencia
python /app/scripts/extract_data.py
echo "Extracción completada."

python /app/scripts/load_data.py
echo "Carga completada."

python /app/scripts/transform_data.py
echo "Transformación completada."

echo "Pipeline finalizado exitosamente."