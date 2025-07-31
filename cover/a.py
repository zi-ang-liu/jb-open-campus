import matplotlib.pyplot as plt
import numpy as np
from numpy import ma
from matplotlib import cm, ticker
from matplotlib.colors import LogNorm

# Create meshgrid
N = 400
x = np.linspace(-3.0, 3.0, N)
y = np.linspace(-3.0, 3.0, N)
X, Y = np.meshgrid(x, y)

# Data
Z1 = np.exp(-(X**2) - Y**2)
Z2 = np.exp(-((X * 10) ** 2) - (Y * 10) ** 2)
z = Z1 + 50 * Z2
z[:5, :5] = -1
z = ma.masked_where(z <= 0, z)

# Create the plot
fig, ax = plt.subplots(figsize=(10, 10), facecolor="black")
cs = ax.contourf(X, Y, z, locator=ticker.LogLocator(), cmap=cm.plasma, norm=LogNorm())

# Aesthetic tweaks
ax.set_facecolor("black")
ax.set_xticks([])
ax.set_yticks([])

# Remove spines
for spine in ax.spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()
