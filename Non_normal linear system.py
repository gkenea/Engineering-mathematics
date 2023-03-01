#!/usr/bin/env python
# coding: utf-8

# In[22]:


import numpy as np
from matplotlib import pyplot as plt
import scipy
from scipy.integrate import solve_ivp


# In[25]:


t = np.linspace(0, 1000, 10000)
A = np.array([[-0.009, 1], [0, -0.01]])
y0 = np.array([0, 1])
def linear_ode(t, y):
    return A @ y
    
# integrate linear system from (0, 1000) with 
# initial condition of y0 and returning solution at times t_eval
linear_ode_solution = solve_ivp(linear_ode, (0, 1000), y0, t_eval=t)
y = linear_ode_solution.y.T
plt.plot(t, y)
plt.legend(['x', 'v'], fontsize=12, framealpha=1.0)
plt.ylabel('x, v')
plt.xlabel('Time')
plt.grid(True)


# In[24]:


e_values, e_vectors = scipy.linalg.eig(A)
print('e_values',e_values)
print('e_vectors', e_vectors)
print("A'A", A.T@A)
print("AA'", A@A.T)


# In[ ]:




