
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def func_plot(func_name):
    lb, ub, dim, fobj = get_functions_details(func_name)
    
    if func_name == 'F1':
        x = np.arange(lb, ub+1, 2)
        y = x
    else:
        x = np.arange(lb, ub+0.1, 0.1)
        y = x
    
    X, Y = np.meshgrid(x, y)
    f = np.zeros_like(X)
    
    for i in range(len(x)):
        for j in range(len(y)):
            if func_name != 'F15' and func_name != 'F19' and func_name != 'F20' and func_name != 'F21' and func_name != 'F22' and func_name != 'F23':
                f[i,j] = fobj(x[i], y[j])
            elif func_name == 'F15':
                f[i,j] = fobj(x[i], y[j], 0, 0)
            elif func_name == 'F19':
                f[i,j] = fobj(x[i], y[j], 0)
            elif func_name == 'F20':
                f[i,j] = fobj(x[i], y[j], 0, 0, 0, 0)
            elif func_name == 'F21' or func_name == 'F22' or func_name == 'F23':
                f[i,j] = fobj(x[i], y[j], 0, 0)
    
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
        lb, ub, dim = [-0.5, -0.5], [0.5, 0.5], 2
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
        lb, ub, dim = -5, 5, 4
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
        lb, ub, dim = -5, 5, 3
        fobj = F19
    elif func_name == 'F20':
        lb, ub, dim = -5, 5, 6
        fobj = F20
    elif func_name == 'F21':
        lb, ub, dim = -5, 5, 4
        fobj = F21
    elif func_name == 'F22':
        lb, ub, dim = -5, 5, 4
        fobj = F22
    elif func_name == 'F23':
        lb, ub, dim = -5, 5, 4
        fobj = F23
    
    return lb, ub, dim, fobj

# Define your benchmark functions here:
def F1(x, y):
    return x**2 + y**2

def F2(x, y):
    return abs(x) + abs(y) + abs(x * y)

def F3(x, y):
    return np.sqrt(abs(x) + abs(y) + abs(x * y))

def F4(x, y):
    return max(abs(x), abs(y))

def F5(x, y):
    return sum(100 * (y - x**2)**2 + (1 - x)**2)

def F6(x, y):
    return sum(abs((x+.5)**2) + abs((y+.5)**2) + abs((x+.5)**2 * (y+.5)**2))

def F7(x, y):
    return -x * np.sin(np.sqrt(abs(x))) - y * np.sin(np.sqrt(abs(y)))

def F8(x, y):
    return x**2 - 10 * np.cos(2 * np.pi * x) + y**2 - 10 * np.cos(2 * np.pi * y) + 20

def F9(x, y):
    return sum(abs(x) ** (1 + 10 * np.arange(1, len(x)+1) / (len(x)+1)) + abs(y) ** (1 + 10 * np.arange(1, len(y)+1) / (len(y)+1)))

def F10(x, y):
    return x**2 - 10 * np.cos(2 * np.pi * x) + y**2 - 10 * np.cos(2 * np.pi * y) + 20

def F11(x, y):
    return 0.5 - ((np.sin((x**2 + y**2)**0.5))**2 - 0.5) / (1 + 0.001 * (x**2 + y**2))**2

def F12(x, y):
    return -20 * np.exp(-0.2 * np.sqrt(x**2 + y**2) / 2) - np.exp(np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y) / 2) + 20 + np.exp(1)

def F13(x, y):
    return (x - 0.5)**2 - np.cos(2 * np.pi * (x - 0.5)) + (y - 0.5)**2 - np.cos(2 * np.pi * (y - 0.5))

def F14(x, y):
    return x**2 / 4000 + y**2 / 4000 - np.cos(x / np.sqrt(np.arange(1, len(x)+1))) - np.cos(y / np.sqrt(np.arange(1, len(y)+1)))

def F15(x, y, z, t):
    return (x - 0.5)**2 - np.cos(2 * np.pi * (x - 0.5)) + (y - 0.5)**2 - np.cos(2 * np.pi * (y - 0.5)) + (z - 0.5)**2 - np.cos(2 * np.pi * (z - 0.5)) + (t - 0.5)**2 - np.cos(2 * np.pi * (t - 0.5))

def F16(x, y):
    return -x * np.sin(np.sqrt(abs(x))) - y * np.sin(np.sqrt(abs(y)))

def F17(x, y):
    return (x - 0.5)**2 - np.cos(2 * np.pi * (x - 0.5)) + (y - 0.5)**2 - np.cos(2 * np.pi * (y - 0.5))

def F18(x, y):
    return (x - 0.5)**2 - np.cos(2 * np.pi * (x - 0.5)) + (y - 0.5)**2 - np.cos(2 * np.pi * (y - 0.5))

def F19(x, y, z):
    return (x - 0.5)**2 - np.cos(2 * np.pi * (x - 0.5)) + (y - 0.5)**2 - np.cos(2 * np.pi * (y - 0.5)) + (z - 0.5)**2 - np.cos(2 * np.pi * (z - 0.5))

def F20(x, y, z, t, w, u):
    return (x - 0.5)**2 - np.cos(2 * np.pi * (x - 0.5)) + (y - 0.5)**2 - np.cos(2 * np.pi * (y - 0.5)) + (z - 0.5)**2 - np.cos(2 * np.pi * (z - 0.5)) + (t - 0.5)**2 - np.cos(2 * np.pi * (t - 0.5)) + (w - 0.5)**2 - np.cos(2 * np.pi * (w - 0.5)) + (u - 0.5)**2 - np.cos(2 * np.pi * (u - 0.5))

def F21(x, y, z, t):
    return (x - 0.5)**2 - np.cos(2 * np.pi * (x - 0.5)) + (y - 0.5)**2 - np.cos(2 * np.pi * (y - 0.5)) + (z - 0.5)**2 - np.cos(2 * np.pi * (z - 0.5)) + (t - 0.5)**2 - np.cos(2 * np.pi * (t - 0.5))

def F22(x, y, z, t):
    return (x - 0.5)**2 - np.cos(2 * np.pi * (x - 0.5)) + (y - 0.5)**2 - np.cos(2 * np.pi * (y - 0.5)) + (z - 0.5)**2 - np.cos(2 * np.pi * (z - 0.5)) + (t - 0.5)**2 - np.cos(2 * np.pi * (t - 0.5))

def F23(x, y, z, t):
    return (x - 0.5)**2 - np.cos(2 * np.pi * (x - 0.5)) + (y - 0.5)**2 - np.cos(2 * np.pi * (y - 0.5)) + (z - 0.5)**2 - np.cos(2 * np.pi * (z - 0.5)) + (t - 0.5)**2 - np.cos(2 * np.pi * (t - 0.5))


