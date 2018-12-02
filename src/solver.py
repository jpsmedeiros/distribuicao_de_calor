import numpy as np
import fatoracao_lu as lu
import math
import heat_map
from scipy.sparse import csr_matrix

class Solver:

    def __init__(self, model, delta_t):
        self.current_distribution = model.initial_distribution
        self.nx = model.nx
        self.ny = model.ny
        self.delta_t = delta_t
        self.shape = model.shape

    def solve(self):
        max_difference = 1.0
        heat_map.draw(self.current_distribution)
        while max_difference > 0 and math.log(max_difference, 10) > -7:
            linearized_distribution = self.get_array_from_distribution(self.current_distribution)
            system_to_solve = self.get_system()
            result = np.array(lu.resolve_lu(system_to_solve, linearized_distribution))
            max_difference = self.calculate_max_difference(linearized_distribution, result)
            self.current_distribution = result.reshape(self.shape[0], self.shape[1])
            heat_map.draw(self.current_distribution)

    def calculate_max_difference(self, initial, final):
        return np.max(np.abs(initial-final))


    def get_system(self):
        system_dimension = self.shape[0] * self.shape[1]
        system_to_solve = []
        for i in range(system_dimension):
            current_row = [0] * system_dimension

            if self.is_boundary(i):
                current_row[i] = 1
            else:
                # i,j term
                current_row[i] = 2 * (self.nx * self.ny + self.nx * self.delta_t + self.ny * self.delta_t) / (
                            self.nx * self.ny)
                # i-1,j term
                current_row[i - self.shape[0]] = -self.delta_t / self.nx
                # i+1,j term
                current_row[i + self.shape[0]] = -self.delta_t / self.nx
                # i,j-1 term
                current_row[i - 1] = -self.delta_t / self.ny
                # i,j+1 term
                current_row[i + 1] = -self.delta_t / self.ny
            sparse_row = csr_matrix(current_row)
            system_to_solve.append(sparse_row)
        return system_to_solve


    def get_array_from_distribution(self, matrix):
        return matrix.reshape((self.shape[0]*self.shape[1]))


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