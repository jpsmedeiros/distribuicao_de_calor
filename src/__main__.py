from model import Model
from solver import Solver

def main():
    dimensionality = (2, 2)
    nx = 0.5
    ny = 0.5
    delta_t = 0.1
    model = Model(nx, ny, dimensionality)
    solver = Solver(model, delta_t)
    solver.solve()

if __name__ == "__main__":
    main()
