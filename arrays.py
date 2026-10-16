""""
What is an array :
-------------------- ---------------------------------------------------------
An array is a data structure that stores values of same data type[cite: 1]. 
In Python, this is the main difference between arrays and lists[cite: 1]. 
While python lists can contain values corresponding to different data types, 
arrays in python can only contain values corresponding to same data type[cite: 1].
=============================================================================
"""



# importing the numpy 
import numpy as np
# example :
my_lst=[12,34,56,7]

# one dimensional array
my_arr=np.array(my_lst)

# we can see the dimension by using shape 
# which shows the coloum and rows
print(my_arr.shape)


# ========================================================

# we can see it by using the( type ) method 

print(type(my_arr))
# numpy.ndarray

#==========================================================================

# 2 dimensional array:
l1=[1,2,3,7,5]
l2=[4,5,6,7,6]
l3=[7,8,9,8,9]
my_array2=np.array([l1,l2,l3])

# use shape to see its dimension
print(my_array2.shape)

# we can see that its a two dimensionl array becuse it has 3 rows and 3 coloums


# =======================================================



# if you want to reshape your array's coloum and rows you can do it by ( reshape         )
print(my_array2.reshape(5,3))


#  your reshaping be careful that number of elements should be  equal