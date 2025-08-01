# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df = pd.read_csv("dataset_ingenieria_civil.csv")

# Mostrar las primeras filas
print("🔹 Primeras 5 filas:")
print(df.head())

# Información general del dataset
print("\n🔹 Información general:")
print(df.info())

# Estadísticas descriptivas
print("\n🔹 Estadísticas descriptivas:")
print(df.describe())

# Verificar valores nulos
print("\n🔹 Valores nulos:")
print(df.isnull().sum())

# Distribución de tipos de proyecto
print("\n🔹 Distribución por tipo de proyecto:")
print(df['tipo_proyecto'].value_counts())

# Histograma de costos
plt.figure(figsize=(8, 5))
sns.histplot(df['costo_estimado_millones'], bins=30, kde=True)
plt.title("Distribución del Costo Estimado (millones)")
plt.xlabel("Costo en millones")
plt.ylabel("Frecuencia")
plt.show()

# Gráfico de barras para tipos de proyecto
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='tipo_proyecto', palette='Set2')
plt.title("Cantidad de Proyectos por Tipo")
plt.ylabel("Cantidad")
plt.xlabel("Tipo de Proyecto")
plt.show()