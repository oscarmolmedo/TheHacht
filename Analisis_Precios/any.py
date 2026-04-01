import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración visual
sns.set_theme(style="whitegrid")

# Carga de datos
df = pd.read_csv('housing.csv')

# Inspección rápida
print("--- Estructura del Dataset ---")
#print(df.info())
print("\n--- Estadísticos Descriptivos ---")
display = df.describe()
print(display)

nulos = df.isnull().sum()
print(f"Valres faltantes por columna:\n{nulos}")