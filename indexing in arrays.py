import numpy as np


#(                          indexing in arrays                       )
#(--------------------------------------------------------------------)


#one dimensional arrays 
my_array=np.array([1,2,3,4,5,6,7,8,])
# acessing a array by indexing 

# example 
# print(my_array[3])



# two dimensonal arrays 
l1=[1,2,3,7,5]
l2=[4,5,6,7,6]
l3=[7,8,9,8,9]
my_array2=np.array([l1,l2,l3])

print(my_array2)

# in 2 dimensional array we we do indexing like this :
# print(my_array2[1:3,0:3])

# in left we always write the raw index we want 
# in right  we always write the coloum index we want 

print(my_array2[1:,2:4])










