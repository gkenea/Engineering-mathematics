#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp


# In[16]:


# define time base and initial condition\n",
t = np.linspace(0, 10, 10000)
y0 = [2, -3]
 
x = np.exp(-t) + np.exp(-2 * t)
plt.plot(t, x, 'k')
    
A = np.array([[0, 1], [-2, -3]])

def linear_ode(t, y):
    return A @ y 
  
linear_ode_solution = solve_ivp(linear_ode, (0, 10), y0, t_eval=t)
y = linear_ode_solution.y
plt.plot(t, y[0, :], 'r--')
plt.xlabel('Time [s]')
plt.ylabel('Solution x')
plt.legend(['Analytic', 'RK45'])
plt.grid(True)
 
# eigenvalues of A should be roots of characteristic equation!\n",
eigvals, eigvecs = np.linalg.eig(A)
print(eigvals)


# In[ ]:




