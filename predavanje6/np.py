import numpy as np


v = np.array([1, 2, 3, 4, 5, 6, 7, 8])
m = np.array([[1, 2, 3], [4, 5, 6]])

print(v)
print(m.ndim, m.shape, m.size, m.dtype)

s = np.array([2**64 - 1])
print(s)
print(s + 1)

a = np.arange(0, 100, 0.5)
print(a)

b = np.linspace(0, 100, 1000)
print(b)

c = np.eye(10)
d = np.zeros((5, 6))
print(c, d)

vv = np.reshape(v, (2, 2, 2))
print(vv)

print(np.transpose(m))

print(np.vstack([v, v, v]))
print(np.hstack([v, v, v]))

m = np.loadtxt("matrika.csv", skiprows=1, delimiter=",")
print(m)

np.savetxt(
    "neki_podatki.csv",
    c,
    delimiter=",",
    fmt="%i",
)

print(v + 1)
print(v == 1)
print(v * v)

print(np.sum(v))
print(np.dot(v, v))
print(np.matmul(m, m.transpose()))
print(m @ m.transpose())

# m[1][2]
# m[1, 2]

print((v % 2) == 0)

print(v[(v % 2) == 0])
