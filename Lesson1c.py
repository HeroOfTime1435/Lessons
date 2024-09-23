# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 18:31:03 2024

@author: izzy1
"""

#I first wrote out the list of values before converting it into an array going down from 10 to zero in units of 0.5#
a = (10,9.5,9,8.5,8,7.5,7,6.5,6,5.5,5,4.5,4,3.5,3,2.5,2,1.5,1,0.5)

array(a)
Out[17]: 
array([10. ,  9.5,  9. ,  8.5,  8. ,  7.5,  7. ,  6.5,  6. ,  5.5,  5. ,
        4.5,  4. ,  3.5,  3. ,  2.5,  2. ,  1.5,  1. ,  0.5,  0. ])

y = array(a)

#This is the code I used for the final calculation, imputting the whole equation with careful use of the parenthesis#
sqrt((2*(10-y))/9.81)
Out[29]: 
array([0.        , 0.31943828, 0.45175395, 0.55328334, 0.63887656,
       0.71428571, 0.7824608 , 0.84515425, 0.9035079 , 0.95831485,
       1.01015254, 1.05945693, 1.10656667, 1.15175111, 1.19522861,
       1.23717915, 1.27775313, 1.31707778, 1.35526185, 1.39239919])

#This is me using the given code and realizing it allows me to get the different in values by shifting them, use it for both arrays to get dt and dy# 
y[1:20]
Out[30]: 
array([9.5, 9. , 8.5, 8. , 7.5, 7. , 6.5, 6. , 5.5, 5. , 4.5, 4. , 3.5,
       3. , 2.5, 2. , 1.5, 1. , 0.5])

y[0:19]
Out[31]: 
array([10. ,  9.5,  9. ,  8.5,  8. ,  7.5,  7. ,  6.5,  6. ,  5.5,  5. ,
        4.5,  4. ,  3.5,  3. ,  2.5,  2. ,  1.5,  1. ])

y[1:20]-y[0:19]
Out[32]: 
array([-0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5,
       -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5])

dy = y[1:20]-y[0:19]

dt = t[1:20]-t[0:19]

#By utilizing the new values of the difference I was able to calculate the average velocity over an interval#
v = dy/dt

v
Out[11]: 
array([ -1.56524758,  -3.77884195,  -4.9246827 ,  -5.84158351,
        -6.63049517,  -7.3340579 ,  -7.97531375,  -8.56844457,
        -9.12293148,  -9.64549022, -10.14108641, -10.61351563,
       -11.06575711, -11.50020061, -11.91879801, -12.32316816,
       -12.71467146, -13.09446421, -13.46353913])

