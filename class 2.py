#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = 10


# In[2]:


x


# In[3]:


y = 10


# In[4]:


y


# In[5]:


id(x)


# In[6]:


id(y)


# In[7]:


z = 1000
a = 1000
z
a


# In[8]:


id(z)


# In[9]:


id(a)


# In[18]:


x = "Rakib"
y = "Bangladesh"
print("My country name is " +y)


# In[12]:


x = "Rakib"
print("My name is "+x)


# # Local vs Global

# In[26]:


x = 1000 #global
def func1():
    x = 500 #local
    print("Valu : ",x)
func1()
def func2():
    print("Valu : ",x)
func2() 


# In[ ]:




