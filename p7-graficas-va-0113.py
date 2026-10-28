import numpy as np
import matplotlib.pyplot as plt

# Santiago Pacheco NC = 0113
no_lista = [1, 2, 3, 17, 48]
califa_ML = [20, 30, 80, 100, 90]
califa_VA = [70.90, 60, 90, 100, 90]

plt.plot(no_lista, califa_ML, label="Califa ML")
plt.plot(no_lista, califa_VA, label="Califa VA")

plt.title("Calificación materiales 0113")
plt.xlabel("Número de lista")
plt.ylabel("Calificación")
plt.legend()
plt.show()