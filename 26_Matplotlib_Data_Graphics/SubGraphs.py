import numpy as np
import matplotlib.pyplot as plt

ahorros = np.random.randint(100, size=[6])
meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio']
mapeado = range(len(meses))

arr_pedro = np.random.randint(100, size=[6])
arr_marta = np.random.randint(100, size=[6])
arr_ana = np.random.randint(100, size=[6])

# Make the dimension of the window in inches
plt.rcParams["figure.figsize"] = (15,5) # Before start ploting

# Create the table 1 x 3 and plot at celd 1
plt.subplot(1, 3, 1)  
plt.plot(arr_pedro, label="Pedro", color="red", ls="-", lw="2", 
         marker="o", markersize="10", markeredgewidth="2", markerfacecolor="yellow", markeredgecolor="red")
plt.xticks(mapeado, meses)
plt.legend()


# Create the table 1 x 3 and plot at celd 2
plt.subplot(1, 3, 2)  
plt.plot(arr_marta, label="Marta", color="#0000ff", ls="--", lw="2", 
         marker="*", markersize="15", markeredgewidth="2", markerfacecolor="cyan", markeredgecolor="#0000ff")
plt.xticks(mapeado, meses)
plt.legend()


# Create the table 1 x 3 and plot at celd 3
plt.subplot(1, 3, 3)  
plt.plot(arr_ana, label="Ana", color="green", ls="-.", lw="2", 
         marker="D", markersize="10", markeredgewidth="2", markerfacecolor="lime", markeredgecolor="green")
plt.xticks(mapeado, meses)
plt.legend()

# Show the plot
plt.show()  



# Change the size
plt.rcParams["figure.figsize"] = (9,9)

# ploting 9 subgraphs
plt.suptitle('Subgráficos', size=15)
for i in range(9):
    plt.subplot(3, 3, i+1)  
    plt.plot(np.random.randint(100, size=[6]))
    plt.plot(np.random.randint(100, size=[6]))
    plt.ylim(0, 100)

plt.show()