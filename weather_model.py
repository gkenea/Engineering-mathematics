#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
from matplotlib import pyplot as plt


# In[5]:


A = np.array([[0.5, 0.5, 0.25], [0.25, 0, 0.25], [0.25, 0.5, 0.5]])


# In[6]:


xtoday = [1, 0, 0]


# In[7]:


the_weather = np.zeros((50, 3))
the_weather[0, :] = xtoday
for i in range(50):
    xtomorrow = A @ xtoday  # xtomorrow is linear combination of xtoday\n",
    xtoday = xtomorrow
    the_weather[i, :] = xtomorrow


# In[8]:


plt.plot(the_weather)
plt.grid(True)


# In[ ]:




