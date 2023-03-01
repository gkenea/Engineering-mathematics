#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Numerical integration with the rectangle and trapezoidal rules
# import libraries\n",
import numpy as np
from matplotlib import pyplot as plt


# In[3]:


# define physical constants and time base\n",
a = 0
b = 10
dxf = 0.01
xf = np.linspace(a, b, int(b / dxf))
yf = np.sin(xf)
plt.figure()
plt.grid(True)
plt.plot(xf, yf)

dxc = 0.5
xc = np.linspace(a, b, int(b / dxc))
edges = np.linspace(a, b, int(b / dxc) + 1, endpoint=True)
yc = np.sin(xc)
plt.stairs(yc, edges, color='r')
plt.grid(True)
plt.show()


# In[4]:


n = len(xc)
  
# left-rectangle rule\n",
area1 = 0
for i in range(n - 1):
    area1 = area1 + yc[i] * dxc
print(area1)


# In[5]:


# right-rectangle rule\n",
area2 = 0
for i in range(n - 1):
    area2 = area2 + yc[i + 1] * dxc
print(area2)


# In[6]:


# trapezoid rule\n",
area3 = 0
for i in range(n - 1):
    area3 = area3 + (dxc / 2) * (yc[i] + yc[i + 1])
print(area3)


# In[7]:


# we can also use built in python functions\n",
area1 = sum(yc[:-1]) * dxc
area2 = sum(yc[1:]) * dxc
area3 = np.trapz(yc, xc)
print(area1, area2, area3)
area3 = np.trapz(yc) * dxc
print(area1, area2, area3)


# In[8]:


# we can also figure out better estimate using fine resolution data\n",
area1f = sum(yf[:-1]) * dxf
area2f = sum(yf[1:]) * dxf
area3f = np.trapz(yf, xf)  # This one gets very close to the true value of 1.8391!\n",
print(area1, area2, area3f)
area3f = np.trapz(yf) * dxf
print(area1, area2, area3f)


# In[ ]:




