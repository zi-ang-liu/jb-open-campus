import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import font_manager

font_path = "demo/font/NotoSansJP-Regular.ttf"
jp_font = font_manager.FontProperties(fname=font_path)

plt.rcParams["font.family"] = jp_font.get_name()
