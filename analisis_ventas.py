import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos del CSV
df = pd.read_csv('ventas_productos.csv')

# Calcular el precio total por producto
df['Precio Total'] = df['Cantidad'] * df['Precio']

# Mostrar el DataFrame actualizado
print("Datos de ventas:")
print(df)

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(df['Producto'], df['Precio Total'], color='skyblue')
plt.title('Precio Total por Producto')
plt.xlabel('Producto')
plt.ylabel('Precio Total')
plt.xticks(rotation=45)

# Guardar el gráfico como PNG
plt.savefig('precio_total_productos.png')
plt.show()