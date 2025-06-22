import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

saves = np.random.randint(50,100, size=[6])
meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']
mapeado = range(len(meses))

plt.plot(saves)                             # Add The graph
plt.xticks(mapeado, meses)                  # Horizontal values
plt.xlim(1, 4)                              # x limits
plt.title("Ahorros del primer semestre")    # Title
plt.xlabel("Meses")                         # x label
plt.ylabel("Cantidad en €")                 # y label
plt.show()                                  # Show


# Legends
"""
0:best
1: upper right
2: upper left
3: lower left
4: lower right
5: right
6: center left
7: center right
8: lower center
9: upper center
10: center
"""
plt.plot(saves, label="Legend")             # Add The graph the legend can be added here
plt.xticks(mapeado, meses)                  # Horizontal values
plt.xlim(1, 4)                              # x limits
plt.title("Ahorros del primer semestre")    # Title
plt.xlabel("Meses")                         # x label
plt.ylabel("Cantidad en €")                 # y label
plt.legend(["Legend2"], loc=4)              # WE can add a legen here with the loc
plt.show()                                  # Show


# With data frames


df = pd.DataFrame(
    data=[
        np.random.randint(100, size=[6]), 
        np.random.randint(100, size=[6]), 
        np.random.randint(100, size=[6])],
    index=['Pedro','Marta','Ana'], 
    columns=['Enero','Febrero','Marzo','Abril','Mayo','Junio'])

plt.plot(df.T)
plt.xlim(1, 4)
plt.title("Ahorros del primer semestre")
plt.xlabel("Meses")
plt.ylabel("Cantidad en €")
plt.legend(['Pedro','Marta','Ana'])
plt.show()

# Smart Graphs (dinamic graph)
for t in range(1, 11):
    plt.plot(
        range(1, 11),                   # X axos
        [t * n for n in range(1, 11)],  # Y axis
        label=f"Tabla del {t}")         # legend for every serie
    
plt.title('Tablas')
plt.xlabel('Número')
plt.ylabel('Resultado')
plt.legend()
plt.show()