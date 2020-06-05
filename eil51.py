import acopy
import tsplib95

colony = acopy.ant.Colony(alpha=1, beta=3)
problem = tsplib95.load_problem('./data/eil51.tsp')

G = problem.get_graph()
solution = tsplib95.load_solution('./data/eil101.opt.tour')

# print(problem.trace_tours(solution))

# optimal : 426

ants = 200
iterations = 100
deviation1 = []
solver = acopy.solvers.Solver(rho=0.2, q=1)

for i in range(0, 9):
    G = problem.get_graph()
    colony = acopy.ant.Colony(alpha=1, beta=2)
    tour = solver.solve(G, colony, ants, iterations)
    print(tour.cost)
    deviation1.append(abs(426-tour.cost))

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
    deviation1.append(abs(426-tour.cost))

result1 = sum(deviation1) / len(deviation1)
print("Ants: ", ants, "Iterations: ", iterations)
print("Averave deviation: ", result1)
print("nodes: ", tour.nodes)
print("\n")

################################################################################

ants = 100
iterations = 100
deviation1 = []
solver = acopy.solvers.Solver(rho=0.4, q=1)

for i in range(0, 9):
    G = problem.get_graph()
    colony = acopy.ant.Colony(alpha=1, beta=2)
    tour = solver.solve(G, colony, ants, iterations)
    print(tour.cost)
    deviation1.append(abs(426-tour.cost))

result1 = sum(deviation1) / len(deviation1)
print("Ants: ", ants, "Iterations: ", iterations)
print("Averave deviation: ", result1)
print("nodes: ", tour.nodes)
print("\n")

################################################################################

ants = 200
iterations = 100
deviation1 = []
solver = acopy.solvers.Solver(rho=0.2, q=3)

for i in range(0, 9):
    G = problem.get_graph()
    colony = acopy.ant.Colony(alpha=1, beta=2)
    tour = solver.solve(G, colony, ants, iterations)
    print(tour.cost)
    deviation1.append(abs(426-tour.cost))

result1 = sum(deviation1) / len(deviation1)
print("Ants: ", ants, "Iterations: ", iterations)
print("Averave deviation: ", result1)
print("nodes: ", tour.nodes)
print("\n")

################################################################################

ants = 200
iterations = 100
deviation1 = []
solver = acopy.solvers.Solver(rho=0.2, q=1)

for i in range(0, 9):
    G = problem.get_graph()
    colony = acopy.ant.Colony(alpha=1, beta=1)
    tour = solver.solve(G, colony, ants, iterations)
    print(tour.cost)
    deviation1.append(abs(426-tour.cost))

result1 = sum(deviation1) / len(deviation1)
print("Ants: ", ants, "Iterations: ", iterations)
print("Averave deviation: ", result1)
print("nodes: ", tour.nodes)
print("\n")

################################################################################

ants = 200
iterations = 200
deviation1 = []
solver = acopy.solvers.Solver(rho=0.2, q=1)

for i in range(0, 9):
    G = problem.get_graph()
    colony = acopy.ant.Colony(alpha=1, beta=2)
    tour = solver.solve(G, colony, ants, iterations)
    print(tour.cost)
    deviation1.append(abs(426-tour.cost))

result1 = sum(deviation1) / len(deviation1)
print("Ants: ", ants, "Iterations: ", iterations)
print("Averave deviation: ", result1)
print("nodes: ", tour.nodes)
print("\n")

################################################################################

ants = 100
iterations = 100
deviation1 = []
solver = acopy.solvers.Solver(rho=0.3, q=1)

for i in range(0, 9):
    G = problem.get_graph()
    colony = acopy.ant.Colony(alpha=2, beta=2)
    tour = solver.solve(G, colony, ants, iterations)
    print(tour.cost)
    deviation1.append(abs(426-tour.cost))

result1 = sum(deviation1) / len(deviation1)
print("Ants: ", ants, "Iterations: ", iterations)
print("Averave deviation: ", result1)
print("nodes: ", tour.nodes)
print("\n")

################################################################################

ants = 200
iterations = 100
deviation1 = []
solver = acopy.solvers.Solver(rho=0.2, q=5)

for i in range(0, 9):
    G = problem.get_graph()
    colony = acopy.ant.Colony(alpha=1, beta=5)
    tour = solver.solve(G, colony, ants, iterations)
    print(tour.cost)
    deviation1.append(abs(426-tour.cost))

result1 = sum(deviation1) / len(deviation1)
print("Ants: ", ants, "Iterations: ", iterations)
print("Averave deviation: ", result1)
print("nodes: ", tour.nodes)
print("\n")

################################################################################

# print("ulysses16 external solution: ", problem.trace_tours(solution)) # 426
# print("ulysses16 cost: ", tour.cost)
# print("ulysses16 nodes: ", tour.nodes)
