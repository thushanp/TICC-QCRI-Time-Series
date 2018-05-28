import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import csv


with open("mergedate.csv") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    data = [r for r in reader]


def column(matrix, i):
    return [row[i] for row in matrix]



x = column(data, 0)

y = column(data, 1)


# x = [float(alpha) for alpha in x]
# y = [float(alpha) for alpha in y]


# create some fake data
x = y = np.arange(-4.0, 4.0, 0.02)
# here are the x,y and respective z values
X, Y = np.meshgrid(x, y)

Z = column(data, 2)

Z = [float(alpha) for alpha in Z]
# Z = np.sinc(np.sqrt(X*X+Y*Y))
# this is the value to use for the color
V = column(data, 3)
V = [float(alpha) for alpha in V]

# create the figure, add a 3d axis, set the viewing angle
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.view_init(45,60)


print(Z)
print(X)
print(Y)
print(V)
# here we create the surface plot, but pass V through a colormap
# to create a different color for each patch
fig = ax.plot_surface(Z, X, Y, facecolors=cm.Oranges(V))		

# fig.savefig('test.png')

plt.savefig('myfig')
