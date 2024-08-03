import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 3, 6, 7])
y = np.array([1, 3, 6, 1])

fig, ax = plt.subplots()
ax.plot(x, y, color="orange")
ax.scatter(x, y, color="black", edgecolor="black", s=10)  # Add circles with scatter

plt.show()
