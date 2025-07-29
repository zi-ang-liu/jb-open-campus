import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import font_manager

import matplotlib.font_manager as fm

fonts = fm.findSystemFonts()
print([[str(font), fm.FontProperties(fname=font).get_name()] for font in fonts[:10]])

font_path = "demo/font/NotoSansJP-Regular.ttf"
plt.rcParams["font.family"] = font_manager.FontProperties(fname=font_path).get_name()

# try to plot a simple figure with Japanese characters
jp_font = font_manager.FontProperties(fname=font_path)
plt.text(0.5, 0.5, "こんにちは", fontproperties=jp_font, fontsize=20, ha="center")
plt.title("日本語のタイトル", fontproperties=jp_font, fontsize=16)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.axis("off")
plt.show()
