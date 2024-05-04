import numpy as np

def roulette_wheel_selection(weights):
    accumulation = np.cumsum(weights)
    p = np.random.rand() * accumulation[-1]
    chosen_index = -1
    for index in range(len(accumulation)):
        if accumulation[index] > p:
            chosen_index = index
            break
    return chosen_index

# Example usage:
# weights = [1, 5, 3, 15, 8, 1]
# choice = roulette_wheel_selection(weights)
# print("Most probable result is", choice + 1, "(weights", weights[choice], ")")
