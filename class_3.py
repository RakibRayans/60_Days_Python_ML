#!/usr/bin/env python
# coding: utf-8

# # Input Function

# In[5]:


data = "Data science fun!"


# In[6]:


type(data)


# In[9]:


data = input()


# In[10]:


data


# In[11]:


x = input()
y = input()


# In[12]:


x + y  #input taking as a string not a digit


# In[13]:


type(x)
type(y)


# In[14]:


x = int(x)
y = int(y) #now those string converted as an integer value


# In[15]:


x + y


# In[17]:


x = int(input("Enter the 1st number :"))


# In[18]:


x


# In[20]:


y =int(input("Enter the 2nd number :")) #input should be integer value


# In[21]:


y =int(input("Enter the 2nd number :"))


# In[22]:


y =int(input("Enter the 2nd number :"))


# In[23]:


y


# In[24]:


y =float(input("Enter the 2nd number :"))


# In[25]:


y


# In[26]:


x+y


# # String

# In[27]:


data = "This is our 60 days data Science course."


# In[28]:


type(data)


# In[29]:


len(data) #space also count as a character


# In[30]:


import sys
sys.getsizeof(data) #here we can find how much memory it takes to store


# In[31]:


data.count("course") #count hoy many time word or line repeate


# # Python string methode

# In[32]:


data.find("our") #searching any data location


# In[34]:


data.find("60",6,15) #searching any word or character bitween a range. If findabel it will show location,otherwise it will show -1.


# In[35]:


data.find("60",6,10)


# In[37]:


data.index("60",6,10) #in index methode it will show error if data is not present in that range


# In[38]:


data.lower()


# In[39]:


data.upper()


# In[40]:


data.casefold() #lower


# In[43]:


x = "hi My name Is RAKIB. i am from BANGLADESH."


# In[44]:


x.capitalize()


# In[45]:


x.swapcase()


# In[46]:


x.title()


# In[47]:


x.islower() #checking lower/upper?


# In[48]:


data.isupper()


# In[49]:


data.islower()


# In[50]:


x.encode()


# In[51]:


type(x.encode) #method type


# In[52]:


type(x.encode()) #result storing type


# In[53]:


x.split() # Splitting string


# In[54]:


data.split()


# In[56]:


data.split()[3] #showing sub string from data


# In[62]:


y = "Here total index value is 100, i am showing in the middle."


# In[63]:


y.center(100) #here data will be showen in middle 


# In[64]:


data.replace("course","tutorial")


# In[65]:


a = 5000
b = 12000
c = a+b


# In[68]:


print("I have {} taka.".format(c))


# In[ ]:





# In[ ]:




