import numpy as np

class Solver:

    def __init__(self, model, delta_t):
        self.current_distribution = model.initial_distribution
        self.nx = model.nx
        self.ny = model.ny
        self.delta_t = delta_t


    def solve(self):
        print('hi')