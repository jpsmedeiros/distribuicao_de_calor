from model import Model
from solver import Solver

def main():
    dimensionality = (3, 3)
    nx = 1
    ny = 1
    model = Model(nx, ny, dimensionality)
    solver = Solver(model)
    solver.solve()

if __name__ == "__main__":
    main()
