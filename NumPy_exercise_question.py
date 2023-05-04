#!/usr/bin/env python
# coding: utf-8

# 
# # NumPy exercises
# 

# In[1]:


# Import the numpy package under the name np
import numpy as np

# Print the numpy version and the configuration
print(np.__version__)


# ![purple-divider](https://user-images.githubusercontent.com/7065401/52071927-c1cd7100-2562-11e9-908a-dde91ba14e59.png)
# 
# ## Array creation

# ### Create a numpy array of size 10, filled with zeros.

# In[2]:


# your code goes here
np.zeros(10)


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Create a numpy array with values ranging from 10 to 49

# In[3]:


# your code goes here
np.arange(10,50)


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Create a numpy matrix of 2*2 integers, filled with ones.

# In[7]:


# your code goes here
a=(2,2)
np.ones(a)


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Create a numpy matrix of 3*2 float numbers, filled with ones.

# In[8]:


# your code goes here
b=(3,2)
np.ones(b)


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, create a new numpy array with the same shape and type as X, filled with ones.

# In[12]:


# your code goes here
c=(4,4)
np.ones(c)


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy matrix, create a new numpy matrix with the same shape and type as X, filled with zeros.

# In[13]:


# your code goes here
np.zeros(c)


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Create a numpy matrix of 4*4 integers, filled with fives.

# In[14]:


# your code goes here
np.full((4,4),fill_value = 5)


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy matrix, create a new numpy matrix with the same shape and type as X, filled with sevens.

# In[17]:


# your code goes here
np.full((4,4),fill_value = 7)


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Create a 3*3 identity numpy matrix with ones on the diagonal and zeros elsewhere.

# In[18]:


# your code goes here
np.identity(3)


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Create a numpy array, filled with 3 random integer values between 1 and 10.

# In[25]:


# your code goes here
np.random.randint(1,10,3)


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Create a 3\*3\*3 numpy matrix, filled with random float values.

# In[26]:


# your code goes here
np.random.randn(3,3,3)


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X python list convert it to an Y numpy array

# In[30]:


# your code goes here
x=[1,2,3,4,5,6,7]
y=np.array(x)
y


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, make a copy and store it on Y.

# In[35]:


# your code goes here
x= np.arange(1,20,2)
y=x.copy
y


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Create a numpy array with numbers from 1 to 10

# In[38]:


# your code goes here
x= np.arange(1,11)
x


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Create a numpy array with the odd numbers between 1 to 10

# In[39]:


# your code goes here
np.arange(1,11,2)


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Create a numpy array with numbers from 1 to 10, in descending order.

# In[41]:


# your code goes here
np.arange(10,0,-1)


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Create a 3*3 numpy matrix, filled with values ranging from 0 to 8

# In[44]:


# your code goes here
a=np.array([[0,1,2],
         [3,4,5],
         [6,7,8]])
a.shape


# ![purple-divider](https://user-images.githubusercontent.com/7065401/52071927-c1cd7100-2562-11e9-908a-dde91ba14e59.png)
# 
# ## Array indexation
# 

# 
# 
# ```
# X = np.array([
#     [1,   2,  3,  4],
#     [5,   6,  7,  8],
#     [9,  10, 11, 12],
#     [13, 14, 15, 16]
# ])
# ```
# 
# 

# In[101]:


X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])


# ### Given the X numpy array, show it's first element

# In[81]:


# your code goes here
X[0]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, show it's last element

# In[82]:


# your code goes here
X[-1]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, show it's first three elements

# In[83]:


# your code goes here
X[0:3]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, show all middle elements

# In[84]:


# your code goes here
X[1:-1]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, show the elements in reverse position

# In[85]:


# your code goes here
np.flip(X)


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, show the elements in an odd position

# In[86]:


# your code goes here
X[1],X[3]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy matrix, show the first row elements

# In[87]:


# your code goes here
X[0]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy matrix, show the last row elements

# In[88]:


# your code goes here
X[-1]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy matrix, show the first element on first row

# In[90]:


# your code goes here
X[0][0]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy matrix, show the last element on last row

# In[91]:


# your code goes here
X[-1][-1]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy matrix, show the middle row elements

# In[93]:


# your code goes here
X[1:-1]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy matrix, show the first two elements on the first two rows

# In[94]:


# your code goes here
X[0:2,0:2]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy matrix, show the last two elements on the last two rows

# In[102]:


# your code goes here
X[2:,2:]


# ![purple-divider](https://user-images.githubusercontent.com/7065401/52071927-c1cd7100-2562-11e9-908a-dde91ba14e59.png)
# 
# ## Array manipulation
# 

# ### Convert the given integer numpy array to float

# In[2]:


# your code goes here
X = [-5, -3, 0, 10, 40]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Reverse the given numpy array (first element becomes last)

# In[5]:


# your code goes here
np.flip(X)


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Order (sort) the given numpy array

# In[6]:


# your code goes here
np.sort(X)


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, set the fifth element equal to 1

# In[7]:


# your code goes here
X[4]=1
X


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, change the 40 with a 50

# In[10]:


# your code goes here
X[-1] = 50
X


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy matrix, change the last row with all 1

# In[105]:


# your code goes here
X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy matrix, change the last item on the last row with a 0

# In[107]:


# your code goes here
X[-1][-1]=0
X


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy matrix, add 5 to every element

# In[108]:


# your code goes here
X+5


# ![purple-divider](https://user-images.githubusercontent.com/7065401/52071927-c1cd7100-2562-11e9-908a-dde91ba14e59.png)
# 
# ## Boolean arrays _(also called masks)_
# 

# ### Given the X numpy array, make a mask showing negative elements

# In[12]:


# your code goes here
X = np.array([-1,2,0,-4,5,6,0,0,-9,10])

X[X<0]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, get the negative elements

# In[69]:


# your code goes here
mask= X<0
X[mask]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, get numbers higher than 5

# In[71]:


# your code goes here
X>5
X[X>5]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, get numbers higher than the elements mean

# In[72]:


# your code goes here
X>X.mean()
X[X>X.mean()]


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, get numbers equal to 2 or 10

# In[13]:


# your code goes here
X[(X==2)|(X==10)]


# ![purple-divider](https://user-images.githubusercontent.com/7065401/52071927-c1cd7100-2562-11e9-908a-dde91ba14e59.png)
# 
# ## Summary statistics

# ### Given the X numpy array, show the sum of its elements

# In[63]:


# your code goes here
X = np.array([3, 5, 6, 7, 2, 3, 4, 9, 4])


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, show the mean value of its elements

# In[64]:


# your code goes here
np.mean(X)


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy matrix, show the sum of its columns

# In[58]:


# your code goes here
X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy matrix, show the mean value of its rows

# In[62]:


# your code goes here
np.mean(X,axis = 1)


# ![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# 
# ### Given the X numpy array, show the max value of its elements

# In[59]:


# your code goes here
np.max(X)


# ![purple-divider](https://user-images.githubusercontent.com/7065401/52071927-c1cd7100-2562-11e9-908a-dde91ba14e59.png)
