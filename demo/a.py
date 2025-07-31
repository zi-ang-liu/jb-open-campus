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
fig, ax = plt.subplots(figsize=(10, 10), dpi=300, facecolor="black")

# Shrink the data area by plotting in a smaller inset box
inset_ax = fig.add_axes([0.2, 0.2, 0.6, 0.6])  # [left, bottom, width, height]
inset_ax.set_facecolor("black")
cs = inset_ax.contourf(
    X, Y, z, locator=ticker.LogLocator(), cmap=cm.plasma, norm=LogNorm()
)

# Minimalist: no ticks or spines
inset_ax.set_xticks([])
inset_ax.set_yticks([])
for spine in inset_ax.spines.values():
    spine.set_visible(False)

# Add title on main figure (not inset)
fig.suptitle(
    "Contours of Optimization\nOperations Research",
    fontsize=24,
    color="white",
    weight="bold",
    y=0.95,
)

plt.show()
# Save the figure
fig.savefig("demo/contour_plot.png", bbox_inches="tight", facecolor="black", dpi=300)
print("Figure saved as 'demo/contour_plot.png'")
