import networkx as nx
import matplotlib.pyplot as plt

# Create a simple tree (e.g., a binary tree)
T = nx.balanced_tree(r=2, h=3)  # binary tree with height 3

# Use graphviz_layout for tree-like layout
from networkx.drawing.nx_agraph import graphviz_layout

# Create position dictionary using graphviz
pos = graphviz_layout(T, prog="dot")  # 'dot' gives a vertical tree

# Draw the graph
nx.draw(T, pos, with_labels=True, arrows=False, node_size=500, node_color="lightblue")
plt.show()
