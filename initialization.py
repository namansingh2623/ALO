import numpy as np

def initialization(SearchAgents_no, dim, ub, lb):
    ub=np.array([ub] * dim)
    lb=np.array([lb] * dim)
    print(type(ub))
    Boundary_no = len(ub)  

    
    if Boundary_no == 1:
        X = np.random.rand(SearchAgents_no, dim) * (ub - lb) + lb
   
    elif Boundary_no > 1:
        X = np.zeros((SearchAgents_no, dim))
        for i in range(dim):
            ub_i = ub[i]
            lb_i = lb[i]
            X[:, i] = np.random.rand(SearchAgents_no) * (ub_i - lb_i) + lb_i

    return X

