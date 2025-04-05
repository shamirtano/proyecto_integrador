import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

st.title("Dashboard de Olist")

conn = sqlite3.connect("../olist.db")
# Muestra por consola la conexión a la base de datos
print("Conectado a la base de datos SQLite", conn)

# Ejecutar los quieries de la carpeta queries
cur = conn.cursor()
# Crear un objeto DataFrame para almacenar los resultados de las consultas
df = pd.DataFrame()

# Invocar las consultas SQL desde la carpeta queries
def execute_query(query):
    cur.execute(query)
    return cur.fetchall()

# Función para mostrar los resultados de la consulta en un DataFrame
def show_query_results(query):
    global df
    df = pd.DataFrame(execute_query(query))
    st.write(df)

# Función para mostrar un gráfico de barras
def show_bar_chart(query, x_col, y_col):
    global df
    df = pd.DataFrame(execute_query(query))
    df.plot(kind='bar', x=x_col, y=y_col)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"{y_col} vs {x_col}")
    st.pyplot(plt)

# Función para mostrar un gráfico de líneas
def show_line_chart(query, x_col, y_col):
    global df
    df = pd.DataFrame(execute_query(query))
    df.plot(kind='line', x=x_col, y=y_col)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"{y_col} vs {x_col}")
    st.pyplot(plt)

# Función para mostrar un gráfico de dispersión
def show_scatter_chart(query, x_col, y_col):
    global df
    df = pd.DataFrame(execute_query(query))
    df.plot(kind='scatter', x=x_col, y=y_col)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"{y_col} vs {x_col}")
    st.pyplot(plt)

# Función para mostrar un gráfico de pastel
def show_pie_chart(query, col):
    global df
    df = pd.DataFrame(execute_query(query))
    df[col].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title(f"Distribución de {col}")
    st.pyplot(plt)

# Función para mostrar un gráfico de histograma
def show_histogram(query, col):
    global df
    df = pd.DataFrame(execute_query(query))
    df[col].plot(kind='hist', bins=20)
    plt.xlabel(col)
    plt.ylabel('Frecuencia')
    plt.title(f"Histograma de {col}")
    st.pyplot(plt)

# Función para mostrar un gráfico de caja
def show_box_chart(query, col):
    global df
    df = pd.DataFrame(execute_query(query))
    df[col].plot(kind='box')
    plt.ylabel(col)
    plt.title(f"Boxplot de {col}")
    st.pyplot(plt)

# Función para mostrar un gráfico de violín
def show_violin_chart(query, col):
    global df
    df = pd.DataFrame(execute_query(query))
    df[col].plot(kind='violin')
    plt.ylabel(col)
    plt.title(f"Violin plot de {col}")
    st.pyplot(plt)

# Función para mostrar un gráfico de área
def show_area_chart(query, x_col, y_col):
    global df
    df = pd.DataFrame(execute_query(query))
    df.plot(kind='area', x=x_col, y=y_col)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"{y_col} vs {x_col}")
    st.pyplot(plt)

# Función para mostrar un gráfico de burbujas
def show_bubble_chart(query, x_col, y_col, size_col):
    global df
    df = pd.DataFrame(execute_query(query))
    plt.scatter(df[x_col], df[y_col], s=df[size_col])
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"{y_col} vs {x_col} (tamaño por {size_col})")
    st.pyplot(plt)

# Función para mostrar un gráfico de radar
def show_radar_chart(query, cols):
    global df
    df = pd.DataFrame(execute_query(query))
    num_vars = len(cols)

    angles = [n / float(num_vars) * 2 * 3.141592653589793 for n in range(num_vars)]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    plt.xticks(angles[:-1], cols)
    ax.plot(angles, df.loc[0].values.tolist() + df.loc[0].values.tolist()[:1])
    ax.fill(angles, df.loc[0].values.tolist() + df.loc[0].values.tolist()[:1], alpha=0.1)
    plt.title("Radar Chart")
    st.pyplot(fig)

# Función para mostrar un gráfico de densidad
def show_density_chart(query, col):
    global df
    df = pd.DataFrame(execute_query(query))
    df[col].plot(kind='density')
    plt.xlabel(col)
    plt.ylabel('Densidad')
    plt.title(f"Densidad de {col}")
    st.pyplot(plt)

# Función para mostrar un gráfico de matriz de correlación
def show_correlation_matrix(query):
    global df
    df = pd.DataFrame(execute_query(query))
    corr = df.corr()
    plt.matshow(corr, cmap='coolwarm')
    plt.colorbar()
    plt.title("Matriz de Correlación")
    st.pyplot(plt)

# Mostrar varios graficos en una sola página
st.sidebar.title("Seleccionar gráfico")
chart_type = st.sidebar.selectbox("Tipo de gráfico", [
    "Barra",
    "Línea",
    "Dispersión",
    "Pastel",
    "Histograma",
    "Caja",
    "Violin",
    "Área",
    "Burbujas",
    "Radar",
    "Densidad",
    "Matriz de Correlación"
])

# Ejecutar una consulta de prueba para un gráfico de barras
query = "SELECT * FROM olist_orders LIMIT 10"
x_col = "order_id"
y_col = "customer_id"
size_col = "order_status"
cols = ["order_status", "payment_type", "shipping_limit_date"]
density_col = "price"
correlation_query = "SELECT * FROM olist_orders LIMIT 10"

# Mostrar el gráfico seleccionado
if chart_type == "Barra":
    show_bar_chart(query, x_col, y_col)