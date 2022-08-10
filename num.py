import numpy as np
from tabulate import tabulate
x1 = np.zeros((5,2),dtype=int)
x0 = np.ones((2,5),dtype=int)
info = f'''
x0 shape:{x0.shape}
x0 content:{tabulate(x0,tablefmt='grid')}
x1 shape:{x1.shape}
x1 content:{tabulate(x1,tablefmt='grid')}
'''
print(info)