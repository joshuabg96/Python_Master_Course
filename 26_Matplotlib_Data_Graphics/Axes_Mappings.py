import numpy as np
import matplotlib.pyplot as plt

# Generate an array with random saves
saves = np.random.randint(100, size=6)
plt.plot(saves)
plt.show()

# Adding layer to axis
# Defie the months for x axis
meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']
#add The axis
plt.plot(saves)
plt.xticks([0,1,2,3,4,5], meses)
plt.show()

# Create a plot with a random axis
y = np.random.randint(20, size=[6])
plt.plot(y)
plt.show()

# Add the x axis to the plot
x = ["A", "B", "C", "D", "E", "F"]
plt.plot(x, y)
plt.show()


# inverter plot
plt.plot(y, x)
plt.show()

# Create random arrays
x = np.random.randint(20, size=[6])
y = np.random.randint(20, size=[6])

plt.plot(x, y)
plt.show()