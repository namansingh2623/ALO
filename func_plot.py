
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def func_plot(func_name):
    lb, ub, dim, fobj = get_functions_details(func_name)
    
    if func_name == 'F1':
        x = np.arange(-100, 101, 2)
        y = x
    elif func_name == 'F2':
        x = np.arange(-100, 101, 2)
        y = x
    elif func_name == 'F3':
        x = np.arange(-100, 101, 2)
        y = x
    elif func_name == 'F4':
        x = np.arange(-100, 101, 2)
        y = x
    elif func_name == 'F5':
        x = np.arange(-200, 201, 2)
        y = x
    elif func_name == 'F6':
        x = np.arange(-100, 101, 2)
        y = x
    elif func_name == 'F7':
        x = np.arange(-1, 1.01, 0.03)
        y = x
    elif func_name == 'F8':
        x = np.arange(-500, 501, 10)
        y = x
    elif func_name == 'F9':
        x = np.arange(-5, 5.1, 0.1)
        y = x
    elif func_name == 'F10':
        x = np.arange(-20, 20.5, 0.5)
        y = x
    elif func_name == 'F11':
        x = np.arange(-500, 501, 10)
        y = x
    elif func_name == 'F12':
        x = np.arange(-10, 10.1, 0.1)
        y = x
    elif func_name == 'F13':
        x = np.arange(-5, 5.08, 0.08)
        y = x
    elif func_name == 'F14':
        x = np.arange(-100, 101, 2)
        y = x
    elif func_name == 'F15':
        x = np.arange(-5, 5.1, 0.1)
        y = x
    elif func_name == 'F16':
        x = np.arange(-1, 1.01, 0.01)
        y = x
    elif func_name == 'F17':
        x = np.arange(-5, 5.1, 0.1)
        y = x
    elif func_name == 'F18':
        x = np.arange(-5, 5.06, 0.06)
        y = x
    elif func_name == 'F19':
        x = np.arange(-5, 5.1, 0.1)
        y = x
    elif func_name == 'F20':
        x = np.arange(-5, 5.1, 0.1)
        y = x
    elif func_name == 'F21':
        x = np.arange(-5, 5.1, 0.1)
        y = x
    elif func_name == 'F22':
        x = np.arange(-5, 5.1, 0.1)
        y = x
    elif func_name == 'F23':
        x = np.arange(-5, 5.1, 0.1)
        y = x
    
    X, Y = np.meshgrid(x, y)
    f = np.zeros_like(X)
    
    for i in range(len(x)):
        for j in range(len(y)):
            if func_name != 'F15' and func_name != 'F19' and func_name != 'F20' and func_name != 'F21' and func_name != 'F22' and func_name != 'F23':
                f[i,j] = fobj([x[i], y[j]])
            elif func_name == 'F15':
                f[i,j] = fobj([x[i], y[j], 0, 0])
            elif func_name == 'F19':
                f[i,j] = fobj([x[i], y[j], 0])
            elif func_name == 'F20':
                f[i,j] = fobj([x[i], y[j], 0, 0, 0, 0])
            elif func_name == 'F21' or func_name == 'F22' or func_name == 'F23':
                f[i,j] = fobj([x[i], y[j], 0, 0])
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, f, cmap='viridis')
    plt.show()

def get_functions_details(func_name):
    lb, ub, dim, fobj = None, None, None, None
    
    if func_name == 'F1':
        lb, ub, dim = -100, 100, 2
        fobj = F1
    elif func_name == 'F2':
        lb, ub, dim = -10, 10, 2
        fobj = F2
    elif func_name == 'F3':
        lb, ub, dim = -100, 100, 2
        fobj = F3
    elif func_name == 'F4':
        lb, ub, dim = -100, 100, 2
        fobj = F4
    elif func_name == 'F5':
        lb, ub, dim = -5, 5, 2
        fobj = F5
    elif func_name == 'F6':
        lb, ub, dim = -100, 100, 2
        fobj = F6
    elif func_name == 'F7':
        lb, ub, dim = -1, 1, 2
        fobj = F7
    elif func_name == 'F8':
        lb, ub, dim = -500, 500, 2
        fobj = F8
    elif func_name == 'F9':
        lb, ub, dim = -5, 5, 2
        fobj = F9
    elif func_name == 'F10':
        lb, ub, dim = -500, 500, 2
        fobj = F10
    elif func_name == 'F11':
        lb, ub, dim = -0.5, 0.5, 2
        fobj = F11
    elif func_name == 'F12':
        lb, ub, dim = -np.pi, np.pi, 2
        fobj = F12
    elif func_name == 'F13':
        lb, ub, dim = -3, 1, 2
        fobj = F13
    elif func_name == 'F14':
        lb, ub, dim = -100, 100, 2
        fobj = F14
    elif func_name == 'F15':
        lb, ub, dim =-5, 5, 2
        fobj = F15
    elif func_name == 'F16':
        lb, ub, dim = -1, 1, 2
        fobj = F16
    elif func_name == 'F17':
        lb, ub, dim = -5, 5, 2
        fobj = F17
    elif func_name == 'F18':
        lb, ub, dim = -5, 5, 2
        fobj = F18
    elif func_name == 'F19':
        lb, ub, dim = -5, 5, 2
        fobj = F19
    elif func_name == 'F20':
        lb, ub, dim = -5, 5, 2
        fobj = F20
    elif func_name == 'F21':
        lb, ub, dim = -5, 5, 2
        fobj = F21
    elif func_name == 'F22':
        lb, ub, dim = -5, 5, 2
        fobj = F22
    elif func_name == 'F23':
        lb, ub, dim = -5, 5, 2
        fobj = F23
    
    return lb, ub, dim, fobj

# Define your benchmark functions here:
def F1(x):
    return sum(x**2)

def F2(x):
    return sum(abs(x)) + np.prod(abs(x))

def F3(x):
    return sum((abs(x) + (x**2))**0.5)

def F4(x):
    return max(abs(x))

def F5(x):
    return sum(100 * (x[1:] - x[:-1]**2)**2 + (x[:-1] - 1)**2)

def F6(x):
    return sum(abs((x+.5)**2)) + np.prod(abs((x+.5)**2))

def F7(x):
    return sum(-x * np.sin(np.sqrt(abs(x))))

def F8(x):
    return sum(x**2 - 10 * np.cos(2 * np.pi * x) + 10)

def F9(x):
    return sum(abs(x) ** (1 + 10 * np.arange(1, len(x)+1) / (len(x)+1)))

def F10(x):
    return sum(x**2 - 10 * np.cos(2 * np.pi * x) + 10)

def F11(x):
    return 0.5 - ((np.sin((x[0]**2 + x[1]**2)**0.5))**2 - 0.5) / (1 + 0.001 * (x[0]**2 + x[1]**2))**2

def F12(x):
    return -20 * np.exp(-0.2 * np.sqrt(sum(x**2) / len(x))) - np.exp(sum(np.cos(2 * np.pi * x)) / len(x)) + 20 + np.exp(1)

def F13(x):
    return sum((x - 0.5)**2 - np.cos(2 * np.pi * (x - 0.5)))

def F14(x):
    return sum(x**2 / 4000) - np.prod(np.cos(x / (np.arange(1, len(x)+1)**0.5)))

def F15(x):
    return sum((x - 0.5)**2 - np.cos(2 * np.pi * (x - 0.5)))

def F16(x):
    return sum(-x * np.sin(np.sqrt(abs(x))))

def F17(x):
    return sum((x - 0.5)**2 - np.cos(2 * np.pi * (x - 0.5)))

def F18(x):
    return sum((x - 0.5)**2 - np.cos(2 * np.pi * (x - 0.5)))

def F19(x):
    return sum((x - 0.5)**2 - np.cos(2 * np.pi * (x - 0.5)))

def F20(x):
    return sum((x - 0.5)**2 - np.cos(2 * np.pi * (x - 0.5)))

def F21(x):
    return sum((x - 0.5)**2 - np.cos(2 * np.pi * (x - 0.5)))

def F22(x):
    return sum((x - 0.5)**2 - np.cos(2 * np.pi * (x - 0.5)))

def F23(x):
    return sum((x - 0.5)**2 - np.cos(2 * np.pi * (x - 0.5)))

func_plot('F1')  # Replace 'F1' with any function name you want to plot