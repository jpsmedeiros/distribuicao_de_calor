from model import Model
from solver import Solver
import time

def main():
    dimensionality = (2,2)
    nx = 0.15
    ny = 0.15
    delta_t = 0.1
    start_time = time.time()
    model = Model(nx, ny, dimensionality)
    solver = Solver(model, delta_t)
    solver.solve()
    end_time = time.time()
    print(end_time - start_time)

if __name__ == "__main__":
    main()
