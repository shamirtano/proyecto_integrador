# Imagen base de Python
FROM python:3.9-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar requirements.txt desde la raíz del proyecto
COPY ../requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el proyecto
COPY .. .

# Copiar el script de orquestación
COPY ./orchestrate.sh .

# Hacer el script ejecutable
RUN chmod +x orchestrate.sh

# Comando por defecto para ejecutar el pipeline
CMD ["./orchestrate.sh"]