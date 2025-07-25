import matplotlib.pyplot as plt

dados = [22, 45, 22, 30, 27, 45, 28, 30, 27, 22, 45, 30, 30]

plt.hist(dados, bins=5, color="black", edgecolor="red")
plt.title("Gráfico de Histograma")
plt.xlabel("Faixa")
plt.ylabel("Frequência")
plt.show()