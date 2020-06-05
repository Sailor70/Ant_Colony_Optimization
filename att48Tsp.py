import acopy
import tsplib95

colony = acopy.ant.Colony(alpha=1, beta=3)
problem = tsplib95.load_problem('./data/att48.tsp')

G = problem.get_graph()
solution = tsplib95.load_solution('./data/att48.opt.tour')

print(problem.trace_tours(solution))

ants = 25
iterations = 100
deviation1 = []
solver = acopy.solvers.Solver(rho=0.2, q=1)

for i in range(0, 9):
    G = problem.get_graph()
    colony = acopy.ant.Colony(alpha=1, beta=2)
    tour = solver.solve(G, colony, ants, iterations)
    print(tour.cost)
    deviation1.append(abs(33522-tour.cost))

result1 = sum(deviation1) / len(deviation1)
print("Ants: ", ants, "Iterations: ", iterations)
print("Averave deviation: ", result1)
print("nodes: ", tour.nodes)
print("\n")

################################################################################

ants = 25
iterations = 100
deviation1 = []
solver = acopy.solvers.Solver(rho=0.2, q=5)

for i in range(0, 9):
    G = problem.get_graph()
    colony = acopy.ant.Colony(alpha=1, beta=3)
    tour = solver.solve(G, colony, ants, iterations)
    print(tour.cost)
    deviation1.append(abs(33522-tour.cost))

result1 = sum(deviation1) / len(deviation1)
print("Ants: ", ants, "Iterations: ", iterations)
print("Averave deviation: ", result1)
print("nodes: ", tour.nodes)
print("\n")

################################################################################

ants = 25
iterations = 100
deviation1 = []
solver = acopy.solvers.Solver(rho=0.4, q=1)

for i in range(0, 9):
    G = problem.get_graph()
    colony = acopy.ant.Colony(alpha=1, beta=2)
    tour = solver.solve(G, colony, ants, iterations)
    print(tour.cost)
    deviation1.append(abs(33522-tour.cost))

result1 = sum(deviation1) / len(deviation1)
print("Ants: ", ants, "Iterations: ", iterations)
print("Averave deviation: ", result1)
print("nodes: ", tour.nodes)
print("\n")

################################################################################

ants = 100
iterations = 100
deviation1 = []
solver = acopy.solvers.Solver(rho=0.2, q=1)

for i in range(0, 9):
    G = problem.get_graph()
    colony = acopy.ant.Colony(alpha=1, beta=2)
    tour = solver.solve(G, colony, ants, iterations)
    print(tour.cost)
    deviation1.append(abs(33522-tour.cost))

result1 = sum(deviation1) / len(deviation1)
print("Ants: ", ants, "Iterations: ", iterations)
print("Averave deviation: ", result1)
print("nodes: ", tour.nodes)
print("\n")

################################################################################

ants = 50
iterations = 100
deviation1 = []
solver = acopy.solvers.Solver(rho=0.2, q=1)

for i in range(0, 9):
    G = problem.get_graph()
    colony = acopy.ant.Colony(alpha=1, beta=1)
    tour = solver.solve(G, colony, ants, iterations)
    print(tour.cost)
    deviation1.append(abs(33522-tour.cost))

result1 = sum(deviation1) / len(deviation1)
print("Ants: ", ants, "Iterations: ", iterations)
print("Averave deviation: ", result1)
print("nodes: ", tour.nodes)
print("\n")

################################################################################

ants = 30
iterations = 100
deviation1 = []
solver = acopy.solvers.Solver(rho=0.1, q=1)

for i in range(0, 9):
    G = problem.get_graph()
    colony = acopy.ant.Colony(alpha=1, beta=2)
    tour = solver.solve(G, colony, ants, iterations)
    print(tour.cost)
    deviation1.append(abs(33522-tour.cost))

result1 = sum(deviation1) / len(deviation1)
print("Ants: ", ants, "Iterations: ", iterations)
print("Averave deviation: ", result1)
print("nodes: ", tour.nodes)
print("\n")

################################################################################

ants = 40
iterations = 100
deviation1 = []
solver = acopy.solvers.Solver(rho=0.5, q=1)

for i in range(0, 9):
    G = problem.get_graph()
    colony = acopy.ant.Colony(alpha=1, beta=2)
    tour = solver.solve(G, colony, ants, iterations)
    print(tour.cost)
    deviation1.append(abs(33522-tour.cost))

result1 = sum(deviation1) / len(deviation1)
print("Ants: ", ants, "Iterations: ", iterations)
print("Averave deviation: ", result1)
print("nodes: ", tour.nodes)
print("\n")

################################################################################

ants = 25
iterations = 100
deviation1 = []
solver = acopy.solvers.Solver(rho=0.2, q=5)

for i in range(0, 9):
    G = problem.get_graph()
    colony = acopy.ant.Colony(alpha=1, beta=2)
    tour = solver.solve(G, colony, ants, iterations)
    print(tour.cost)
    deviation1.append(abs(33522-tour.cost))

result1 = sum(deviation1) / len(deviation1)
print("Ants: ", ants, "Iterations: ", iterations)
print("Averave deviation: ", result1)
print("nodes: ", tour.nodes)
print("\n")

################################################################################

# print("ulysses16 external solution: ", problem.trace_tours(solution)) # 33522
# print("ulysses16 cost: ", tour.cost)
# print("ulysses16 nodes: ", tour.nodes)
