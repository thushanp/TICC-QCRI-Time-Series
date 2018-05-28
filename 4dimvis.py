
# coding: utf-8

# In[21]:

import matplotlib.cm as cmx
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

def scatter3d(x,y,z, cs, colorsMap='jet'):
    cm = plt.get_cmap(colorsMap)
    cNorm = matplotlib.colors.Normalize(vmin=min(cs), vmax=max(cs))
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(x, y, z, c=scalarMap.to_rgba(cs))
    scalarMap.set_array(cs)
    fig.colorbar(scalarMap,label='Test')
    plt.show()

x = np.random.uniform(0,1,50)
y = np.random.uniform(0,1,50)
z = np.random.uniform(0,1,50)


# In[22]:

scatter3d(x,y,z,x+y)


# In[23]:

print(y)


# In[24]:

import csv 

with open("myres.csv") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    data = [r for r in reader]

newlist = []
for i in range(0,len(data)):
    try:
        print(float(data[i][0]))
        if float(data[i][0]) == 3.0:
            newlist.append(data[i])
    except IndexError:
        continue

print(data)
print(newlist)
# data = newlist
def column(matrix, i):
    return [row[i] for row in matrix]



x = column(data, 0)

y = column(data, 1)
Z = column(data, 2)
V = column(data, 3)
V = [float(alpha) for alpha in V]

Z = [float(alpha) for alpha in Z]

x = [float(alpha) for alpha in x]
y = [float(alpha) for alpha in y]


# In[25]:

print(x)


# In[26]:

scatter3d(y, x, Z, V)


# In[27]:

for i in data:
    i.reverse()
    i[0] = float(i[0])
    
data = sorted(data)
print(data)


# In[28]:

optimal = (data[0])
print(optimal)


# In[29]:

data = newlist
def column(matrix, i):
    return [row[i] for row in matrix]



x = column(data, 0)

y = column(data, 1)
Z = column(data, 2)
V = column(data, 3)
V = [float(alpha) for alpha in V]

Z = [float(alpha) for alpha in Z]

x = [float(alpha) for alpha in x]
y = [float(alpha) for alpha in y]

scatter3d(y, x, Z, V)

