import numpy as np
import matplotlib.pyplot as plt
from ALO import ALO  # Assuming you have implemented ALO algorithm
from get_function_details import get_functions_details
from func_plot import func_plot

SearchAgents_no = 40  # Number of search agents
Function_name = 'F8'  # Name of the test function
Max_iteration = 500  # Maximum number of iterations
get_functions_details
# Load details of the selected benchmark function
lb, ub, dim, fobj = get_functions_details(Function_name)

# Run ALO
Best_score, Best_pos, cg_curve = ALO(SearchAgents_no, Max_iteration, lb, ub, dim, fobj)

# # Plot results
# fig = plt.figure(figsize=(10, 5))

# # Draw search space
# ax1 = fig.add_subplot(121, projection='3d')
# func_plot(Function_name)
# ax1.set_title('Test function')
# ax1.set_xlabel('x_1')
# ax1.set_ylabel('x_2')
# ax1.set_zlabel(Function_name + '( x_1 , x_2 )')
# ax1.grid(False)

# # Draw objective space
# ax2 = fig.add_subplot(122)
# ax2.semilogy(cg_curve, color='r')
# ax2.set_title('Convergence curve')
# ax2.set_xlabel('Iteration')
# ax2.set_ylabel('Best score obtained so far')
# ax2.grid(False)

# plt.tight_layout()
# plt.show()

# print('The best solution obtained by ALO is:', Best_pos)
# print('The best optimal value of the objective function found by ALO is:', Best_score)
