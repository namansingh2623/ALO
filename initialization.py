import numpy as np

def initialization(SearchAgents_no, dim, ub, lb):
    Boundary_no = len(ub)  # Number of boundaries

    # If the boundaries of all variables are equal
    if Boundary_no == 1:
        X = np.random.rand(SearchAgents_no, dim) * (ub - lb) + lb
    # If each variable has a different lb and ub
    elif Boundary_no > 1:
        X = np.zeros((SearchAgents_no, dim))
        for i in range(dim):
            ub_i = ub[i]
            lb_i = lb[i]
            X[:, i] = np.random.rand(SearchAgents_no) * (ub_i - lb_i) + lb_i

    return X

# Example usage:
SearchAgents_no = 50
dim = 10
ub = np.array([10] * dim)  # Example upper bounds
lb = np.array([-10] * dim)  # Example lower bounds

X = initialization(SearchAgents_no, dim, ub, lb)
print(X)
