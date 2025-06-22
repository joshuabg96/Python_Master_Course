import numpy as np
import matplotlib.pyplot as plt

# The figure create a space where we can draw the graph
fig = plt.figure()

# Add the limits to create an object in every axis where we can draw
rect = (0, 0, 1, 1)
axes = fig.add_axes(rect)

# In every axis we can draw through plt
axes.plot(np.random.randint(100,size=[6]), label="Pedro")
axes.plot(np.random.randint(100,size=[6]), label="Marta")
axes.plot(np.random.randint(100,size=[6]), label="Ana")

# Personalice the graph
axes.set_ylim(0, 100)
axes.set_xlabel("Meses")
axes.set_ylabel("Cantidad en €")
axes.set_title("Ahorros del primer semestre")

#Mapping
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
mapeado = range(len(meses))
axes.set_xticks(mapeado)
axes.set_xticklabels(meses)

fig.set_size_inches(2, 2)
fig.set_dpi(100)
#fig.savefig('grafico.png', bbox_inches='tight', dpi=100)

fig.show()

#SubGraphs of figures

# Creamos una figura para almacenar varios subgráficos
fig, axes = plt.subplots(3,3)
fig.suptitle('Subgráficos en figuras', size=15)

# Dibujando 3x3=9 subgráficos
for i in range(3):
    for j in range(3):
        axes[i, j].plot(np.random.randint(100, size=6))
        axes[i, j].plot(np.random.randint(100, size=6))
        axes[i, j].plot(np.random.randint(100, size=6))
        axes[i, j].set_ylim(0, 100)
        axes[i, j].set_title(f'Ejes [{i}, {j}]')

fig.set_size_inches(12, 12)
fig.show()
fig.savefig('subgraficos.png', bbox_inches='tight', dpi=100)