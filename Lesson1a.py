from numpy import *
#Here I imported Numpy in order to use arrays, then tested it#
r = array([1,2,3,4,5,6,7,8,9])

r
Out[3]: array([1, 2, 3, 4, 5, 6, 7, 8, 9])

r = arrange (0,29,9)
Traceback (most recent call last):

  Cell In[4], line 1
    r = arrange (0,29,9)

NameError: name 'arrange' is not defined


r = arange (0,29,9)
# Here I mistakenly used the format to get evenly spaced values of 9 out of 29#
r
Out[6]: array([ 0,  9, 18, 27])

29/9
Out[7]: 3.2222222222222223
#Here I used 29/9 as a value in order to get evenly spaced values and 9 integers#
r = arange(0,29,(29/9))

r
Out[9]: 
array([ 0.        ,  3.22222222,  6.44444444,  9.66666667, 12.88888889,
       16.11111111, 19.33333333, 22.55555556, 25.77777778])

r**2
Out[10]: 
array([  0.        ,  10.38271605,  41.5308642 ,  93.44444444,
       166.12345679, 259.56790123, 373.77777778, 508.75308642,
       664.49382716])
#I then directly squared the array giving me each individual value squared#
r+r
Out[11]: 
array([ 0.        ,  6.44444444, 12.88888889, 19.33333333, 25.77777778,
       32.22222222, 38.66666667, 45.11111111, 51.55555556])

r*2
Out[12]: 
array([ 0.        ,  6.44444444, 12.88888889, 19.33333333, 25.77777778,
       32.22222222, 38.66666667, 45.11111111, 51.55555556])
#And finally I both added it to itself and multiplied it by two to get double of every value#
