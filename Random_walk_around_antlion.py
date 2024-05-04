import numpy as np


def random_walk_around_antlion(Dim, max_iter, lb, ub, antlion, current_iter):
    lb = np.array(lb, dtype=float)  # Ensure lb is float array
    ub = np.array(ub, dtype=float)  # Ensure ub is float array
    
    if len(lb.shape) > 1:  # Check if boundary vectors are horizontal or vertical
        lb = lb.flatten()
        ub = ub.flatten()

    I = 1  # I is the ratio in Equations (2.10) and (2.11)

    if current_iter > max_iter / 10:
        I = 1 + 100 * (current_iter / max_iter)

    if current_iter > max_iter / 2:
        I = 1 + 1000 * (current_iter / max_iter)

    if current_iter > max_iter * (3 / 4):
        I = 1 + 10000 * (current_iter / max_iter)

    if current_iter > max_iter * 0.9:
        I = 1 + 100000 * (current_iter / max_iter)

    if current_iter > max_iter * 0.95:
        I = 1 + 1000000 * (current_iter / max_iter)

    # Decrease boundaries to converge towards antlion
    lb /= I  # Equation (2.10) in the paper
    ub /= I  # Equation (2.11) in the paper

    # Move the interval of [lb ub] around the antlion [lb+anlion ub+antlion]
    if np.random.rand() < 0.5:
        lb_new = lb + antlion  # Equation (2.8) in the paper
    else:
        lb_new = -lb + antlion

    if np.random.rand() >= 0.5:
        ub_new = ub + antlion  # Equation (2.9) in the paper
    else:
        ub_new = -ub + antlion

    # This function creates Dim random walks and normalize according to lb and ub vectors
    RWs = np.zeros((max_iter, Dim))
    for i in range(Dim):
        X = np.concatenate([[0], np.cumsum(2 * (np.random.rand(max_iter) > 0.5) - 1)])  # Equation (2.1) in the paper
        a, b = np.min(X), np.max(X)
        c, d = lb_new[i], ub_new[i]
        X_norm = ((X - a) * (d - c)) / (b - a) + c  # Equation (2.7) in the paper
        RWs[:, i] = X_norm[:max_iter]

    return RWs
# def random_walk_around_antlion(Dim, max_iter, lb, ub, antlion, current_iter):
    lb = np.array(lb, dtype=float)  # Ensure lb is float array
    ub = np.array(ub, dtype=float)  # Ensure ub is float array
    
    if len(lb.shape) > 1:  # Check if boundary vectors are horizontal or vertical
        lb = lb.flatten()
        ub = ub.flatten()

    I = 1  # I is the ratio in Equations (2.10) and (2.11)

    if current_iter > max_iter / 10:
        I = 1 + 100 * (current_iter / max_iter)

    if current_iter > max_iter / 2:
        I = 1 + 1000 * (current_iter / max_iter)

    if current_iter > max_iter * (3 / 4):
        I = 1 + 10000 * (current_iter / max_iter)

    if current_iter > max_iter * 0.9:
        I = 1 + 100000 * (current_iter / max_iter)

    if current_iter > max_iter * 0.95:
        I = 1 + 1000000 * (current_iter / max_iter)

    # Decrease boundaries to converge towards antlion
    lb /= I  # Equation (2.10) in the paper
    ub /= I  # Equation (2.11) in the paper

    # Move the interval of [lb ub] around the antlion [lb+anlion ub+antlion]
    if np.random.rand() < 0.5:
        lb += antlion  # Equation (2.8) in the paper
    else:
        lb = -lb + antlion

    if np.random.rand() >= 0.5:
        ub += antlion  # Equation (2.9) in the paper
    else:
        ub = -ub + antlion

    # This function creates Dim random walks and normalize according to lb and ub vectors
    RWs = np.zeros((max_iter, Dim))
    for i in range(Dim):
        X = np.concatenate([[0], np.cumsum(2 * (np.random.rand(max_iter) > 0.5) - 1)])  # Equation (2.1) in the paper
        a, b = np.min(X), np.max(X)
        c, d = lb[i], ub[i]
        X_norm = ((X - a) * (d - c)) / (b - a) + c  # Equation (2.7) in the paper
        RWs[:, i] = X_norm[:max_iter]

    return RWs

# def random_walk_around_antlion(Dim, max_iter, lb, ub, antlion, current_iter):
    if isinstance(lb, (int, float)):  # Check if the bounds are scalar
        lb = np.ones(Dim) * lb
        ub = np.ones(Dim) * ub

    if len(lb.shape) > 1:  # Check if boundary vectors are horizontal or vertical
        lb = lb.flatten()
        ub = ub.flatten()

    I = 1  # I is the ratio in Equations (2.10) and (2.11)

    if current_iter > max_iter / 10:
        I = 1 + 100 * (current_iter / max_iter)

    if current_iter > max_iter / 2:
        I = 1 + 1000 * (current_iter / max_iter)

    if current_iter > max_iter * (3 / 4):
        I = 1 + 10000 * (current_iter / max_iter)

    if current_iter > max_iter * 0.9:
        I = 1 + 100000 * (current_iter / max_iter)

    if current_iter > max_iter * 0.95:
        I = 1 + 1000000 * (current_iter / max_iter)

    # Decrease boundaries to converge towards antlion
    lb /= I  # Equation (2.10) in the paper
    ub /= I  # Equation (2.11) in the paper

    # Move the interval of [lb ub] around the antlion [lb+anlion ub+antlion]
    if np.random.rand() < 0.5:
        lb += antlion  # Equation (2.8) in the paper
    else:
        lb = -lb + antlion

    if np.random.rand() >= 0.5:
        ub += antlion  # Equation (2.9) in the paper
    else:
        ub = -ub + antlion

    # This function creates Dim random walks and normalize according to lb and ub vectors
    RWs = np.zeros((max_iter, Dim))
    for i in range(Dim):
        X = np.concatenate([[0], np.cumsum(2 * (np.random.rand(max_iter) > 0.5) - 1)])  # Equation (2.1) in the paper
        a, b = np.min(X), np.max(X)
        c, d = lb[i], ub[i]
        X_norm = ((X - a) * (d - c)) / (b - a) + c  # Equation (2.7) in the paper
        RWs[:, i] = X_norm[:max_iter]

    return RWs

# Example usage:
# Dim = 5
# max_iter = 100
# lb = -10
# ub = 10
# antlion = np.zeros(Dim)
# current_iter = 50

# RWs = random_walk_around_antlion(Dim, max_iter, lb, ub, antlion, current_iter)
# print(RWs)
