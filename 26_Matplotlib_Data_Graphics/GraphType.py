import numpy as np
import matplotlib.pyplot as plt

# Common graph
x = np.arange(1, 11)
y = np.random.randint(10, size=10)

plt.plot(x, y)
plt.show()

# Stem graph
plt.stem(x, y)
plt.show()

# Compared series
for t in range(1, 11)[::-1]:
    plt.fill_between(
        range(1, 11),
        [t * n for n in range(1, 11)],
        label=f"Tabla del {t}"
    )
    
plt.title("Tablas de multiplicar")
plt.legend(loc='upper left')
plt.show()

#cake 
turistas = [86.9, 81.8, 75.9, 60.7, 58.2, 39.3, 37.7, 37.6, 37.5, 35.4]
paises = ['Francia', 'España', 'EEUU', 'China', 'Italia', 
          'México', 'Reino Unido', 'Turquía', 'Alemania', 'Tailandia']

explode = [0, 0.2, 0, 0, 0, 0.5, 0, 0, 0, 0]  # Destacar algunos

plt.title('TOP 10 DESTINOS TURÍSTICOS EN 2017')
plt.pie(turistas, labels=paises, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90)
plt.show()


# Box
jap = np.random.uniform(160, 170, 100)
hol = np.random.uniform(171, 180, 100)
ale = np.random.uniform(168, 176, 100)

# Cambio los colores para que se vea bien en VSC con tema oscura
plt.boxplot([jap, hol, ale], notch=True, patch_artist=True)
plt.xticks([1, 2, 3], ['Japón', 'Países Bajos', 'Alemania'])
plt.ylabel('Estatura media (cm)')
plt.show()


#hist
alturas = np.random.uniform(170, 180, 1000)

plt.hist(alturas, bins=10, edgecolor='black')

plt.title("Distribución de 1000 alturas")
plt.xlabel("Altura media (cm)")
plt.ylabel("Muestras")
plt.show()


#bar

fechas = ['25/06/2022', '27/06/2022', '28/06/2022', '29/06/2022', '30/06/2022']
primas = [111, 111, 109, 107, 108]

plt.bar(range(5), primas, edgecolor='black')

plt.xticks(range(5), fechas, rotation=60)
plt.title("PRIMA DE RIESGO EN ESPAÑA")
plt.ylim(min(primas)-1, max(primas)+1)
plt.show()


# Horizontal bar
fechas = ['25/06/2022', '27/06/2022', '28/06/2022', '29/06/2022', '30/06/2022']
primas = [111, 111, 109, 107, 108]

plt.barh(range(5), primas, edgecolor='black')

plt.yticks(range(5), fechas, rotation=60)
plt.title("PRIMA DE RIESGO EN ESPAÑA")
plt.xlim(min(primas)-1, max(primas)+1)
plt.show()


# step
x = np.arange(1, 11)
y = np.random.randint(10, size=10)

plt.step(x, y)
plt.show()