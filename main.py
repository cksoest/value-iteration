from grid import Grid
import numpy as np


rewards = np.array([
            [-1, -1, -1, 40],
            [-1, -1, -10, -10],
            [-1, -1, -1, -1],
            [10, -2, -1, -1]
        ])
terminal_states = [(0, 3), (3, 0)]
gamma = 0.9

grid = Grid(rewards, terminal_states, gamma)
grid.run(10, verbose=True)
