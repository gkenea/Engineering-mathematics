#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
from matplotlib import pyplot as plt


# In[13]:


dt = .002 # change the value of dt to get optimum value with minimum erret
t = np.linspace(-2, 4, 60)
f = np.sin(t)

# Exact Derivative\n",
dfdt = np.cos(t)


# In[16]:


# plotting commands\n",
plt.plot(t, f, 'k--', linewidth=1.2)
plt.grid(True)
plt.plot(t, dfdt, 'k', linewidth=3)
plt.legend(['Function', 'Exact Derivative'], fontsize=14)
plt.xlim(-2, 4)
plt.ylim(-1.5, 1.5)
plt.show()


# Forward Difference Approximation\n",
dfdtF = (np.sin(t + dt) - np.sin(t)) / dt

# Backward Difference Approximation\n",
dfdtB = (np.sin(t) - np.sin(t - dt)) / dt

# Central Difference Approximation\n",
dfdtC = (np.sin(t + dt) - np.sin(t - dt)) / (2 * dt)

plt.figure(figsize=(20, 4))
plt.subplot(1, 2, 1)
plt.plot(t, dfdt, 'k', linewidth=3)
plt.plot(t, dfdtF, 'b', linewidth=1.2)  # Forward Difference\n",
plt.plot(t, dfdtB, 'g', linewidth=1.2)  # Backward Difference\n",
plt.plot(t, dfdtC, 'r', linewidth=1.2)  # Central Difference\n",
plt.legend(['Exact Derivative', 'Forward Diff', 'Backward Diff', 'Central Diff'],fontsize=14, framealpha=1.0)  # get rid of legend transparency\n",
plt.grid(True)
    
# now make a zoomed-in plot\n",
plt.subplot(1, 2, 2)
plt.plot(t, dfdt, 'k', linewidth=3)
plt.plot(t, dfdtF, 'b', linewidth=1.2)  # Forward Difference\n",
plt.plot(t, dfdtB, 'g', linewidth=1.2)  # Backward Difference\n",
plt.plot(t, dfdtC, 'r', linewidth=1.2)  # Central Difference\n",
plt.grid(True)
plt.xlim(0, 2)
plt.show()


# In[7]:





# In[ ]:




