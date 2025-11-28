import numpy as np

dat = open("bunny.off")

dat.readline()
vrstica = dat.readline()
parametri = vrstica.split(" ")
stevilo_tock = int(parametri[0])
stevilo_ploskev = int(parametri[1])

tocke = np.loadtxt(dat, max_rows=stevilo_tock)
ploskve = np.loadtxt(dat, max_rows=stevilo_ploskev)

dat.close()

print(tocke)

ploskve = ploskve[:, 1:].astype(int)
print(ploskve)

trikotniki = tocke[ploskve]
print(trikotniki)

v1 = trikotniki[:, 1] - trikotniki[:, 0]
v2 = trikotniki[:, 2] - trikotniki[:, 0]

povrsina = np.sum(np.linalg.norm(np.cross(v1, v2), axis=1) / 2)
print(povrsina)
