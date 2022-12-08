import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from PIL import Image
import csv


node_labels = []
for i in range(38):#ラベル付け
    node_labels.append(str(i))

G = nx.Graph()
G.add_nodes_from(node_labels)

pos={}
with open('map2.csv') as f:
    reader = csv.reader(f)
    l = [row for row in reader]

for i in range(len(l[0])-1):#座標読み込み
    d = {l[0][i+1]: (int(l[2][i+1]), int(l[3][i+1]))}
    pos.update(d)
#print(pos)
c = "cyan"
g = "lightgreen"
y = "yellow"
r = "red"
colors = []
for i in range(38):#色判定
    if i==12 or i==35 or i==15:
        colors.append(r)
    elif i==7 or i==36:
        colors.append(y)
    elif i == 2 or i == 11:
        colors.append(g)
    else:
        colors.append(c)

fig = plt.figure(figsize=(8, 7))
ax = fig.add_subplot(1, 1, 1)

nx.draw_networkx(G, pos=pos, node_color=colors)

im = Image.open("map.jpg")
plt.imshow(im, aspect='auto', alpha=0.8)
plt.show()
