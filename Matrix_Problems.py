
# Solving Matrices

import numpy as np

# 3x+y+2z=31, x+y+2z=19, x+3y+2z=25
E = np.array([[3, 1, 2], [1, 1, 2], [1, 3, 2]])
print(E)
d = np.array([31, 19, 25])
print(d)
f = np.linalg.solve(E, d)
print(f"\n{f}")
print(f"x={f[0]}, y={f[1]}, z={f[2]}")

G = np.array([[2, 1, 3, -1], [1, -1, 2, -2], [1, -1, -1, 1], [-1, 2, -2, -1]])
print(f"\n{G}")
g = np.array([6, -1, -4, -7])
print(g)
h = np.linalg.solve(G, g)
print(f"\n{h}")
print(f"w={h[0]}, x={h[1]}, y={h[2]}, z{h[3]}")
