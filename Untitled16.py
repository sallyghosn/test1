#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
l1=np.random.randint(1,10,8)
l2=np.random.randint(1,10,8)
l3=np.random.randint(1,10,8)
l4=np.random.randint(1,10,8)
l5=np.random.randint(1,10,8)
l6=np.random.randint(1,10,8)
l7=np.random.randint(1,10,8)
l8=np.random.randint(1,10,8)
l9=np.random.randint(1,10,8)
l10=np.random.randint(1,10,8)

l=[l1,l2,l3,l4,l5,l6,l7,l8,l9,l10]
ll=pd.DataFrame(l)
ll


# In[5]:


s=[True,True,False,True,False,False,False,False]
t=['sally','reem','raneem','ali','lana','dana','sally','reem']
l2=s
l5=s 
l8=t
l3=t
l6=t

l=[l1,l2,l3,l4,l5,l6,l7,l8,l9,l10]
ll=pd.DataFrame(l)
ll


# In[10]:


d={"num1":l1,"bool1":l2,"name1":l3,"num2":l4,"bool2":l5,"name2":l6,"num3":l7,"bool3":l8,"name3":l9,"num4":l10}
d


# In[7]:





# In[ ]:




