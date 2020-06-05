import tsplib95

from functions import distance_on_unit_sphere
from plotSprawko import plot


problem = tsplib95.load_problem('./data/ulysses16.tsp', distance_on_unit_sphere)
problem.special=distance_on_unit_sphere
G = problem.get_graph()

points: list = []
for i in range(1, G.number_of_nodes()+1):
    points.append(G.nodes[i].get('coord'))

path = [3, 2, 4, 8, 1, 16, 14, 13, 12, 7, 6, 15, 5, 11, 9, 10]

plot(points, path)

############################################################

problem = tsplib95.load_problem('./data/att48.tsp')
G = problem.get_graph()

points: list = []
for i in range(1, G.number_of_nodes()+1):
    points.append(G.nodes[i].get('coord'))

path = [17, 19, 37, 6, 27, 43, 30, 28, 7, 18, 36, 44, 31, 38, 9, 1, 8, 40, 15, 33, 46, 12, 11, 23, 13, 25, 14, 34, 3, 22, 16, 41, 29, 2, 26, 4, 35, 45, 24, 10, 42, 48, 5, 39, 32, 21, 47, 20]

plot(points, path)

#######################################################

problem = tsplib95.load_problem('./data/eil51.tsp')
G = problem.get_graph()

points: list = []
for i in range(1, G.number_of_nodes()+1):
    points.append(G.nodes[i].get('coord'))

path = [47, 18, 4, 17, 37, 5, 49, 10, 30, 34, 50, 16, 29, 21, 2, 20, 35, 36, 3, 28, 31, 26, 8, 48, 23, 7, 43, 24, 14, 25, 13, 41, 19, 40, 42, 44, 15, 45, 33, 39, 9, 38, 11, 32, 1, 22, 27, 6, 51, 46, 12]

plot(points, path)