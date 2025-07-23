---
kernelspec:
  name: python3
  display_name: 'Python 3'
---

# 探索による問題解決

:::{important} Objective 
- コンピューターを使って問題を解決する方法を理解する。
- アルゴリズムの考え方を理解する。
- 幅優先探索（BFS）を迷路問題に適用できる。
- さまざまな問題を探索アルゴリズムで解決できることを理解する。
:::


## 考えてみよう

1. Google Mapsでは、横浜駅から東小金井駅までの最短経路をどうやって見つけるのか？
2. [15パズル](https://ja.wikipedia.org/wiki/15パズル)では、どのようにして最短手数で目的の配置に到達するのか？
3. [迷路](https://ja.wikipedia.org/wiki/%E8%BF%B7%E8%B7%AF)では、どのようにしてゴールに到達するのか？
4. ...

これらの問題は、今日の紹介する簡単な探索アルゴリズムを使うことで解決できます。

:::{note}
ここでの**解決**とは、小規模な問題に対しては、現実的な時間内に解を見つけることを意味します。
ただし、問題の規模が大きくなると、解を現実的な時間内に見つけることが難しくなる場合があります。例えば、何十年もかかることもあります。
:::

## 最短路問題

```{code-cell} python
:tags: [hide-cell]
# Install necessary libraries
!pip install networkx
import networkx as nx
import matplotlib.pyplot as plt
```

```{code-cell} python
:tags: [hide-cell]
!pip install networkx
import networkx as nx
import matplotlib.pyplot as plt

# Create a graph with nodes and edges
G = nx.Graph()
G.add_nodes_from(["A", "B", "C", "D", "E", "F", "G", "H"])
G.add_edge("A", "B", weight=4)
G.add_edge("A", "H", weight=8)
G.add_edge("B", "C", weight=8)
G.add_edge("B", "H", weight=11)
G.add_edge("C", "D", weight=7)
G.add_edge("C", "F", weight=4)
G.add_edge("C", "I", weight=2)
G.add_edge("D", "E", weight=9)
G.add_edge("D", "F", weight=14)
G.add_edge("E", "F", weight=10)
G.add_edge("F", "G", weight=2)
G.add_edge("G", "H", weight=1)
G.add_edge("G", "I", weight=6)
G.add_edge("H", "I", weight=7)

# Find the shortest path from node A to node E
path = nx.shortest_path(G, "A", "E", weight="weight")
print(path)

# Create a list of edges in the shortest path
path_edges = list(zip(path, path[1:]))

# Create a list of all edges, and assign colors based on whether they are in the shortest path or not
edge_colors = [
    "red" if edge in path_edges or tuple(reversed(edge)) in path_edges else "black"
    for edge in G.edges()
]

# Visualize the graph
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos, edge_color=edge_colors)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edge_labels(
    G, pos, edge_labels={(u, v): d["weight"] for u, v, d in G.edges(data=True)}
)

plt.show()
```