FROM apache/airflow:2.9.0
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
COPY Project.ipynb /app/Project.ipynb
COPY data/ /app/data/
WORKDIR /app
# CMD ["airflow", "scheduler"]
# Ejecutar los los scripts de Project.ipynb y data/ en el contenedor
CMD ["python", "Project.ipynb"]