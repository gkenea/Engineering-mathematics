#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Compute central difference derivative for sin(x)
import numpy as np
from matplotlib import pyplot as plt


# In[3]:


n = 30
x = np.linspace(0.1, 3, n)
f = np.sin(x)

plt.plot(x, f, 'k')
plt.plot(x, f, 'rx', linewidth=2)
plt.show()

dx = x[1] - x[0]
dfdx = np.zeros(n)


# Perform the finite differencing\n",
dfdx[0] = (f[1] - f[0]) / (x[1] - x[0]);   # forward diff at f(x_1)\n",
for i in range(1, n - 1):
    dfdx[i]  = (f[i + 1] - f[i - 1]) / (x[i + 1] - x[i - 1])  # central in between\n",
dfdx[-1] = (f[-1] - f[-2])/(x[-1]-x[-2])  # backward diff at f(x_n)"


plt.figure
plt.plot(x, np.cos(x), 'k', label='true derivative')
plt.plot(x, dfdx, 'rx', label='computed derivative')
plt.legend()
plt.show()


# In[ ]:




