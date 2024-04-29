import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def func_plot(func_name):
    lb, ub, dim, fobj = get_functions_details(func_name)
    
    x = np.linspace(lb, ub, 100)
    y = np.linspace(lb, ub, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.zeros_like(X)
    
    for i in range(len(x)):
        for j in range(len(y)):
            Z[i,j] = fobj([x[i], y[j]])
    
    fig = plt.figure()
    ax = fig.add_subplot(121, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_title('Test function')
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel(f'{func_name}(x1, x2)')
    ax.grid(False)
    
    ax2 = fig.add_subplot(122)
    ax2.semilogy(cg_curve, color='r')
    ax2.set_title('Convergence curve')
    ax2.set_xlabel('Iteration')
    ax2.set_ylabel('Best score obtained so far')
    ax2.grid(True)
    
    plt.tight_layout()
    plt.show()

def get_functions_details(func_name):
    lb, ub, dim, fobj = None, None, None, None
    
    if func_name == 'F1':
        lb, ub, dim = -100, 100, 2
        fobj = F1
    # Add other function details here...

    return lb, ub, dim, fobj

def ALO(SearchAgents_no, Max_iteration, lb, ub, dim, fobj):
    # Implementation of ALO algorithm
    pass

# Define your benchmark functions here:
def F1(x):
    return sum(x**2)

# Define other benchmark functions here...

# Main code
SearchAgents_no = 40
Function_name = 'F1'
Max_iteration = 500

# Load details of the selected benchmark function
lb, ub, dim, fobj = get_functions_details(Function_name)

# Run ALO
Best_score, Best_pos, cg_curve = ALO(SearchAgents_no, Max_iteration, lb, ub, dim, fobj)

# Plot results
func_plot(Function_name)

print('The best solution obtained by ALO is:', Best_pos)
print('The best optimal value of the objective function found by ALO is:', Best_score)
