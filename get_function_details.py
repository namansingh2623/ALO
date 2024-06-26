
import numpy as np

def get_functions_details(F):
    """
    Returns the details of the selected benchmark function.
    
    Parameters:
        F (str): Name of the test function (e.g., 'F1', 'F2', ..., 'F23').
        
    Returns:
        lb (float or list): Lower bound(s) of the function's variables.
        ub (float or list): Upper bound(s) of the function's variables.
        dim (int): Number of variables.
        fobj (function): Handle to the objective function.
    """
    fobj = None
    lb = None
    ub = None
    dim = None
    
    if F == 'F1':
        fobj = F1
        lb = -100
        ub = 100
        dim = 10
    elif F == 'F2':

        fobj = F2
        lb = -10
        ub = 10
        dim = 10
    elif F == 'F3':
        fobj = F3
        lb = -100
        ub = 100
        dim = 10
    elif F == 'F4':

        fobj = F4
        lb = -100
        ub = 100
        dim = 10
    elif F == 'F5':

        fobj = F5
        lb = -30
        ub = 30
        dim = 10
    elif F == 'F6':

        fobj = F6
        lb = -100
        ub = 100
        dim = 10
    elif F == 'F7':

        fobj = F7
        lb = -1.28
        ub = 1.28
        dim = 10
    elif F == 'F8':

        fobj = F8
        lb = -500
        ub = 500
        dim = 10
    elif F == 'F9':

        fobj = F9
        lb = -5.12
        ub = 5.12
        dim = 10
    elif F == 'F10':

        fobj = F10
        lb = -32
        ub = 32
        dim = 10
    elif F == 'F11':
       
        fobj = F11
        lb = -600
        ub = 600
        dim = 10
    elif F == 'F12':
        
        fobj = F12
        lb = -50
        ub = 50
        dim = 10
    elif F == 'F13':
        
        fobj = F13
        lb = -50
        ub = 50
        dim = 10
    elif F == 'F14':
        
        fobj = F14
        lb = -65.536
        ub = 65.536
        dim = 2
    elif F == 'F15':
        
        fobj = F15
        lb = -5
        ub = 5
        dim = 4
    elif F == 'F16':
        
        fobj = F16
        lb = -5
        ub = 5
        dim = 2
    elif F == 'F17':
        
        fobj = F17
        lb = [-5, 0]
        ub = [10, 15]
        dim = 2
    elif F == 'F18':
        
        fobj = F18
        lb = -2
        ub = 2
        dim = 2
    elif F == 'F19':
        
        fobj = F19
        lb = 0
        ub = 1
        dim = 3
    elif F == 'F20':
        
        fobj = F20
        lb = 0
        ub = 1
        dim = 6
    elif F == 'F21':
        
        fobj = F21
        lb = 0
        ub = 10
        dim = 4
    elif F == 'F22':
        
        fobj = F22
        lb = 0
        ub = 10
        dim = 4
    elif F == 'F23':
        
        fobj = F23
        lb = 0
        ub = 10
        dim = 4
    else:
        raise ValueError("Invalid function name.")
    
    lb = [lb] if not isinstance(lb, list) else lb
    ub = [ub] if not isinstance(ub, list) else ub
    
    return lb, ub, dim, fobj

# Example usage:
# lb, ub, dim, fobj = get_functions_details('F1')

# F1
def F1(x):
    return np.sum(x**2)

# F2
def F2(x):
    return np.sum(np.abs(x)) + np.prod(np.abs(x))

# F3
def F3(x):
    dim = len(x)
    total = 0
    for i in range(dim):
        total += np.power(np.sum(x[:i+1]),2)
    return total

# F4
def F4(x):
    return np.max(np.abs(x))

# F5
def F5(x):
    dim = len(x)
    return np.sum(100*(x[1:dim] - x[:dim-1]**2)**2 + (x[:dim-1] - 1)**2)

# F6
def F6(x):
    return np.sum(np.abs(x + 0.5)**2)

# F7
def F7(x):
    dim = len(x)
    return np.sum([(i+1) * x[i]**4 for i in range(dim)]) + np.random.rand()

# F8
def F8(x):
    return np.sum(-x * np.sin(np.sqrt(np.abs(x))))

# F9
def F9(x):
    dim = len(x)
    return np.sum(np.power(x, 2) - 10 * np.cos(2 * np.pi * np.array(x))) + 10 * dim

# F10
def F10(x):
    dim = len(x)
    return -20 * np.exp(-0.2 * np.sqrt(np.sum(x**2) / dim)) - np.exp(np.sum(np.cos(2 * np.pi * x)) / dim) + 20 + np.exp(1)

# F11
def F11(x):
    dim = len(x)
    return np.sum(x**2) / 4000 - np.prod(np.cos(x / np.sqrt(np.arange(1, dim+1)))) + 1

# F12
def F12(x):
    dim = len(x)
    return (np.pi / dim) * (10 * ((np.sin(np.pi * (1 + (x[0] + 1) / 4)))**2) + np.sum((((x[:dim-1] + 1) / 4)**2) * (1 + 10 * ((np.sin(np.pi * (1 + (x[1:dim] + 1) / 4)))**2))) + ((x[dim-1] + 1) / 4)**2 + np.sum(Ufun(x, 10, 100, 4)))

# F13
def F13(x):
    dim = len(x)
    return 0.1 * ((np.sin(3 * np.pi * x[0]))**2 + np.sum((x[:dim-1] - 1)**2 * (1 + (np.sin(3 * np.pi * x[1:dim]))**2)) + ((x[dim-1] - 1)**2) * (1 + (np.sin(2 * np.pi * x[dim-1]))**2)) + np.sum(Ufun(x, 5, 100, 4))

# F14
def F14(x):
    aS = np.array([[-32, -16, 0, 16, 32, -32, -16, 0, 16, 32, -32, -16, 0, 16, 32, -32, -16, 0, 16, 32, -32, -16, 0, 16, 32],
                   [-32, -32, -32, -32, -32, -16, -16, -16, -16, -16, 0, 0, 0, 0, 0, 16, 16, 16, 16, 16, 32, 32, 32, 32, 32]])
    bS = []
    for j in range(25):
        bS.append(np.sum((x - aS[:,j])**6))
    return (1/500 + np.sum(1 / (np.arange(1, 26) + np.array(bS))))**(-1)

# F15
def F15(x):
    aK = np.array([0.1957, 0.1947, 0.1735, 0.16, 0.0844, 0.0627, 0.0456, 0.0342, 0.0323, 0.0235, 0.0246])
    bK = np.array([0.25, 0.5, 1, 2, 4, 6, 8, 10, 12, 14, 16])
    bK = 1 / bK
    return np.sum((aK - (x[0] * (bK**2 + x[1] * bK)) / (bK**2 + x[2] * bK + x[3]))**2)

# F16
def F16(x):
    return 4 * x[0]**2 - 2.1 * x[0]**4 + x[0]**6 / 3 + x[0] * x[1] - 4 * x[1]**2 + 4 * x[1]**4

# F17
def F17(x):
    return (x[1] - (x[0]**2) * 5.1 / (4 * (np.pi**2)) + 5 / np.pi * x[0] - 6)**2 + 10 * (1 - 1 / (8 * np.pi)) * np.cos(x[0]) + 10

# F18
def F18(x):
    return (1 + (x[0] + x[1] + 1)**2 * (19 - 14 * x[0] + 3 * x[0]**2 - 14 * x[1] + 6 * x[0] * x[1] + 3 * x[1]**2)) * (30 + (2 * x[0] - 3 * x[1])**2 * (18 - 32 * x[0] + 12 * x[0]**2 + 48 * x[1] - 36 * x[0] * x[1] + 27 * x[1]**2))

# F19
def F19(x):
    aH = np.array([[3, 10, 30], [0.1, 10, 35], [3, 10, 30], [0.1, 10, 35]])
    cH = np.array([1, 1.2, 3, 3.2])
    pH = np.array([[0.3689, 0.117, 0.2673], [0.4699, 0.4387, 0.747], [0.1091, 0.8732, 0.5547], [0.03815, 0.5743, 0.8828]])
    o = 0
    for i in range(4):
        o -= cH[i] * np.exp(-np.sum(aH[i] * ((x - pH[i])**2)))
    return o

# F20
def F20(x):
    aH = np.array([[10, 3, 17, 3.5, 1.7, 8], [0.05, 10, 17, 0.1, 8, 14], [3, 3.5, 1.7, 10, 17, 8], [17, 8, 0.05, 10, 0.1, 14]])
    cH = np.array([1, 1.2, 3, 3.2])
    pH = np.array([[0.1312, 0.1696, 0.5569, 0.0124, 0.8283, 0.5886], [0.2329, 0.4135, 0.8307, 0.3736, 0.1004, 0.9991], [0.2348, 0.1415, 0.3522, 0.2883, 0.3047, 0.6650], [0.4047, 0.8828, 0.8732, 0.5743, 0.1091, 0.0381]])
    o = 0
    for i in range(4):
        o -= cH[i] * np.exp(-np.sum(aH[i] * ((x - pH[i])**2)))
    return o

# F21
def F21(x):
    aSH = np.array([[4, 4, 4, 4], [1, 1, 1, 1], [8, 8, 8, 8], [6, 6, 6, 6], [3, 7, 3, 7], [2, 9, 2, 9], [5, 5, 3, 3], [8, 1, 8, 1], [6, 2, 6, 2], [7, 3.6, 7, 3.6]])
    cSH = np.array([0.1, 0.2, 0.2, 0.4, 0.4, 0.6, 0.3, 0.7, 0.5, 0.5])
    o = 0
    for i in range(5):
        o -= (np.dot((x - aSH[i]), (x - aSH[i])) + cSH[i])**(-1)
    return o

# F22
def F22(x):
    aSH = np.array([[4, 4, 4, 4], [1, 1, 1, 1], [8, 8, 8, 8], [6, 6, 6, 6], [3, 7, 3, 7], [2, 9, 2, 9], [5, 5, 3, 3], [8, 1, 8, 1], [6, 2, 6, 2], [7, 3.6, 7, 3.6]])
    cSH = np.array([0.1, 0.2, 0.2, 0.4, 0.4, 0.6, 0.3, 0.7, 0.5, 0.5])
    o = 0
    for i in range(7):
        o -= (np.dot((x - aSH[i]), (x - aSH[i])) + cSH[i])**(-1)
    return o

# F23
def F23(x):
    aSH = np.array([[4, 4, 4, 4], [1, 1, 1, 1], [8, 8, 8, 8], [6, 6, 6, 6], [3, 7, 3, 7], [2, 9, 2, 9], [5, 5, 3, 3], [8, 1, 8, 1], [6, 2, 6, 2], [7, 3.6, 7, 3.6]])
    cSH = np.array([0.1, 0.2, 0.2, 0.4, 0.4, 0.6, 0.3, 0.7, 0.5, 0.5])
    o = 0
    for i in range(10):
        o -= (np.dot((x - aSH[i]), (x - aSH[i])) + cSH[i])**(-1)
    return o

def Ufun(x, a, k, m):
    return k * ((x - a)**m) * (x > a) + k * ((-x - a)**m) * (x < -a)



