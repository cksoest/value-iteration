import numpy as np
import copy
from itertools import product


class Grid:
    def __init__(self):
        self.rewards = np.array([
            [-1, -1, -1, 40],
            [-1, -1, -10, -10],
            [-1, -1, -1, -1],
            [10, -2, -1, -1]
        ])
        self.values = np.zeros(self.rewards.shape)
        self.terminal_states = [(0, 3), (3, 0)]
        self.gamma = 1

    def value_iteration(self):
        old_values = copy.deepcopy(self.values)
        for i, j in product(range(self.rewards.shape[0]), range(self.rewards.shape[1])):
            if (i, j) in self.terminal_states:
                continue
            current_reward = self.rewards[i][j]
            current_value = old_values[i][j]
            u = (i-1, j)
            r = (i, j+1)
            d = (i+1, j)
            l = (i, j-1)

            v = []
            for direction in [u, r, d, l]:
                if direction[0] not in np.arange(self.rewards.shape[0]) or direction[1] not in np.arange(self.rewards.shape[1]):
                    v.append(1*(current_reward+(self.gamma*current_value)))
                else:
                    v.append(1*(self.rewards[direction[0]][direction[1]]+(self.gamma*old_values[direction[0]][direction[1]])))
            self.values[i][j] = max(v)

    def __repr__(self):
        grid = self.values
        return str(grid)


a = Grid()
for _ in range(10):
    a.value_iteration()

print(a)