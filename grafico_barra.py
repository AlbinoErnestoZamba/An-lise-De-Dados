import matplotlib.pyplot as plt

categorias = ["A", "B", "C", "D"]
valores = [40, 70, 30 ,85]

colors = ["red", "blue", "green", "orange"]

plt.bar(categorias,valores, color=colors)
plt.title("Gráfico de Barra")
plt.xlabel("Categoria")
plt.ylabel("Valores")
plt.show()