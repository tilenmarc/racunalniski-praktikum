import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np

obrazi = []
for i in range(1000):
    s = img.imread(f"faces/{10000 + i}.png")
    obrazi.append(s)

obrazi = np.array(obrazi)

skupen_obraz = np.average(obrazi, axis=0)

plt.imshow(skupen_obraz)
plt.show()
