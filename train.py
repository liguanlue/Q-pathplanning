from collections import OrderedDict
from pprint import pprint
grid_size=(3,3)
bounds = (1, 1, grid_size[0], grid_size[1])
intersections = OrderedDict()
tij = OrderedDict()
Q_table = OrderedDict()
for x in range(bounds[0],bounds[2]+1):
    for y in range(bounds[1],bounds[3]+1):
        intersections[(x,y)] = x+y
print(intersections)
for d in intersections:
    for a in intersections:
        for b in intersections:
            if (abs(a[0] - b[0]) + abs(a[1] - b[1])) == 1:
                Q_table[d,a,b] = 0
                tij[a, b] = 500 / 50
            if a == d and (abs(b[0] - d[0]) + abs(b[1] - d[1])) == 1:
                Q_table[d,a,b] = 0
            if b == d and (abs(a[0] - d[0]) + abs(a[1] - d[1])) == 1:
                Q_table[d, a, b] = tij[a, b]

pprint(tij)
pprint(Q_table)
print("intersection key type")
print(intersections.)
print(type(intersections.keys()))