import numpy as np
import copy
from itertools import product


class Grid:
    def __init__(self, rewards, terminal_states, gamma):
        self.rewards = rewards
        self.terminal_states = terminal_states
        self.gamma = gamma
        self.values = np.zeros(self.rewards.shape)
        self.greedy_policy = np.zeros(self.rewards.shape)
        self.greedy_policy = self.greedy_policy.tolist()

    def value_iteration(self, greedy=False):
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
                wrong_dirs = [u, r, d, l]
                wrong_dirs.remove(direction)
                v_sum = 0

                for wrong_dir in wrong_dirs:
                    if wrong_dir[0] not in np.arange(self.rewards.shape[0]) or wrong_dir[1] not in np.arange(self.rewards.shape[1]):
                        v_sum += 0.1 * (current_reward + (self.gamma * current_value))
                    else:
                        v_sum += 0.1 * (self.rewards[wrong_dir[0]][wrong_dir[1]] + (self.gamma * old_values[wrong_dir[0]][wrong_dir[1]]))

                if direction[0] not in np.arange(self.rewards.shape[0]) or direction[1] not in np.arange(self.rewards.shape[1]):
                    v_sum += 0.7*(current_reward+(self.gamma*current_value))
                else:
                    v_sum += 0.7*(self.rewards[direction[0]][direction[1]]+(self.gamma*old_values[direction[0]][direction[1]]))
                v.append(v_sum)

            if greedy:
                actions = ["U", "R", "D", "L"]
                max_v = max(v)
                max_index = v.index(max_v)
                self.greedy_policy[i][j] = actions[max_index]
            else:
                self.values[i][j] = max(v)

    def print_values(self):
        for row in self.values:
            values = "|"
            for v in row:
                values += str(round(v, 1))
                values += "|"
            print(values)
        print("\n")

    def print_greedy_policy(self):
        for row in self.greedy_policy:
            actions = "|"
            for a in row:
                if type(a) == float:
                    a = "X"
                actions += a
                actions += "|"
            print(actions)
        print("\n")

    def run(self, amount_iterations, verbose=False):
        for _ in range(amount_iterations):
            self.value_iteration()
            if verbose:
                self.print_values()
        self.value_iteration(greedy=True)
        if verbose:
            self.print_greedy_policy()
