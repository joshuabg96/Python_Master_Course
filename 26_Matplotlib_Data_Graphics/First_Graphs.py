import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

saves = [52,104,32,65,15,76]

plt.plot(saves)
plt.show()


saves = np.random.randint(100, size=[6])
plt.plot(saves)
plt.show()

#Using Data Frames
df = pd.DataFrame(saves, index=['Enero','Febrero','Marzo','Abril','Mayo','Junio'])
plt.plot(df)
plt.show()

#0100293082