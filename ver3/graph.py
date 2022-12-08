import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from PIL import Image
import csv


node_labels = []
for i in range(38):#ラベル付け
    node_labels.append(str(i))
E = ["21", "32", "15"]#提案ルート

G = nx.Graph()
G2 = nx.DiGraph()
G.add_nodes_from(node_labels)
G2.add_nodes_from(E)
G2.add_edge(E[0],E[1])
G2.add_edge(E[1],E[2])

pos={}#すべて
pos2={} #edgeでつなげるもの
with open('map2.csv') as f:
    reader = csv.reader(f)
    m = [row for row in reader]
with open('time.csv') as f:
    reader = csv.reader(f)
    t = [row for row in reader]
with open('time2.csv') as f:
    reader = csv.reader(f)
    t2 = [row for row in reader]

for i in range(len(m[0])-1):#座標読み込み
    d = {m[0][i+1]: (int(m[2][i+1]), int(m[3][i+1]))}
    pos.update(d)
    if E[0]==m[0][i+1] or E[1]==m[0][i+1] or E[2]==m[0][i+1]:
        e = {m[0][i + 1]: (int(m[2][i + 1]), int(m[3][i + 1]))}
        pos2.update(e)
print(pos2)


now="15:45"#時間を取得

x = t[0].index(now)
crowded = []
crowded[:] = t2[x][1:]
#print(crowded)




s = "deepskyblue"
g = "lightgreen"
y = "yellow"
c = "coral"
r = "red"
v = "darkviolet"
colors = []
colors2 = []
for i in range(38):#色判定
    if int(crowded[i])>90:
        colors.append(v)
    elif int(crowded[i])<90 and int(crowded[i])>=60:
        colors.append(r)
    elif int(crowded[i])<60 and int(crowded[i])>=40:
        colors.append(c)
    elif int(crowded[i])<40 and int(crowded[i])>=20:
        colors.append(y)
    elif int(crowded[i])<20 and int(crowded[i])>=10:
        colors.append(g)
    else:
        colors.append(s)
for i in range(3):#色判定
    colors2.append(colors[int(E[i])])

fig = plt.figure(figsize=(8, 7))
ax = fig.add_subplot(1, 1, 1)

nx.draw_networkx(G, pos=pos, node_color=colors)
nx.draw_networkx(G2, pos=pos2,node_color=colors2)

im = Image.open("map.jpg")
plt.imshow(im, aspect='auto', alpha=0.8)
plt.show()
