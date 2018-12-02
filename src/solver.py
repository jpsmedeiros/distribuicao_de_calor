import numpy as np
import fatoracao_lu as lu

class Solver:

    def __init__(self, model, delta_t):
        self.current_distribution = model.initial_distribution
        self.nx = model.nx
        self.ny = model.ny
        self.delta_t = delta_t
        self.shape = model.shape

    def solve(self):
        print(self.current_distribution)
        linearized_distribution = self.get_array_from_distribution(self.current_distribution)
        system_dimension = self.shape[0]*self.shape[1]
        system_to_solve = np.zeros((system_dimension, system_dimension))
        for i in range(len(system_to_solve)):
            if self.is_boundary(i):
                system_to_solve[i][i] = 1
            else:
                system_to_solve[i][i] = (2*self.nx*self.ny*self.delta_t + 2*self.nx + 2*self.ny)/(self.nx*self.ny)
                system_to_solve[i][i - self.shape[0]] = -1 / self.nx
                system_to_solve[i][i + self.shape[0]] = -1 / self.nx
                system_to_solve[i][i-1] = -1/self.ny
                system_to_solve[i][i+1] = -1/self.ny
        res = np.array(lu.resolve_lu(system_to_solve, linearized_distribution)).reshape(self.shape[0], self.shape[1])
        print(res)

    def get_array_from_distribution(self, matrix):
        return matrix.reshape((self.shape[0]*self.shape[1]))

    def two_dimension_to_one(self, x, y):
        return x*len()

    def is_boundary(self, i):
        x_size = self.shape[0]
        y_size = self.shape[1]
        #Case i is in first line
        if i // x_size == 0:
            return True

        #Case i in the first column
        if i % x_size == 0:
            return True

        #Case i is in the last column
        if (i+1) % x_size == 0:
            return True

        #Case i is in the last line
        if i // x_size == y_size-1:
            return True

        return False