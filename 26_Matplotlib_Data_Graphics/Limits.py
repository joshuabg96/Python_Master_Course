import numpy as np
import matplotlib.pyplot as plt

saves = np.random.randint(50,100, size=[6])
meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']
mapeado = range(len(meses))

plt.plot(saves)             # Add The graph
plt.xticks(mapeado, meses)  # Map the x axis
plt.show()                  # Show

# Vertical limits
plt.plot(saves)
plt.xticks(mapeado, meses)  # Map the x axis
plt.ylim(0,100)             # Configurate the vertical limit ylimit(start,end)
plt.show()                  # Show

# Horizontal limits
plt.plot(saves)
plt.xticks(mapeado, meses)  # Map the x axis
plt.ylim(0,100)             # Configurate the vertical limit ylimit(start,end)
plt.xlim(1,4)               # Configurate the x limit xlimit(start, end)
plt.show()                  # Show