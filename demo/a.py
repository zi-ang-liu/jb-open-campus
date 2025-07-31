import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import random

# Parameters
max_depth = 10
min_branch_prob = 0.3
max_branch_prob = 0.9
branch_factor = 4
length_decay = 0.7
curve_points = 100

# Colormap
cmap = mpl.colormaps["plasma"]
colors = cmap(np.linspace(0, 1, 100))

# Figure setup
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect("equal")
ax.set_axis_off()

color_index = 0


def draw_branch(x0, y0, length, angle, depth):
    global color_index
    if depth == 0:
        return

    # Random number of children (0 to branch_factor)
    num_children = random.randint(0, branch_factor)
    if num_children == 0:
        return

    for i in range(num_children):
        # Random angle offset
        angle_offset = np.random.uniform(-np.pi / 6, np.pi / 6)  # narrower spread
        new_angle = angle + angle_offset

        # Random length decay
        new_length = length * np.random.uniform(0.6, length_decay)

        # End point
        x1 = x0 + new_length * np.cos(new_angle)
        y1 = y0 + new_length * np.sin(new_angle)

        # Less pronounced curve — small offset
        t = np.linspace(0, 1, curve_points)
        cx = (x0 + x1) / 2 + np.random.uniform(-0.05, 0.05)
        cy = (y0 + y1) / 2 + np.random.uniform(0.02, 0.06)
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * cx + t**2 * x1
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * cy + t**2 * y1

        # Draw the branch
        ax.plot(x, y, color=colors[color_index % len(colors)], linewidth=1.5, alpha=0.9)
        color_index += 1

        # Random branching probability
        if random.random() < np.interp(
            depth, [1, max_depth], [min_branch_prob, max_branch_prob]
        ):
            draw_branch(x1, y1, new_length, new_angle, depth - 1)


# Start from the bottom center
draw_branch(0, -1, 2.0, np.pi / 2, max_depth)

plt.title("Random Tree with Gentle Curves", fontsize=14, weight="bold")
plt.show()
