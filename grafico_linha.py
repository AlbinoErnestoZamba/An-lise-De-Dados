import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 5, 20, 25, 30]
 
plt.plot(x,y)
plt.title("Gráfico de linha")
plt.xlabel("Dias")
plt.ylabel("Vendas")
plt.grid(True)
plt.show()