import numpy as np
import matplotlib.pyplot as plt
from ALO import ALO  
from get_function_details import get_functions_details
from func_plot import func_plot

SearchAgents_no = 40 
Function_name = 'F8' 
Max_iteration = 500  
get_functions_details

lb, ub, dim, fobj = get_functions_details(Function_name)


Best_score, Best_pos, cg_curve = ALO(SearchAgents_no, Max_iteration, lb, ub, dim, fobj)

