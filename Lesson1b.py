from numpy import *

ones([100])
Out[2]: 
array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])
#This gives us the array of 100 numbers that we need to start with#

a = ones([100])

# Since exp(x) gives me the natural logarithm, using the array I can get 100 values all equal to the natural logarithm e#
exp(a)
Out[4]: 
array([2.71828183, 2.71828183, 2.71828183, 2.71828183, 2.71828183,
       2.71828183, 2.71828183, 2.71828183, 2.71828183, 2.71828183,
       2.71828183, 2.71828183, 2.71828183, 2.71828183, 2.71828183,
       2.71828183, 2.71828183, 2.71828183, 2.71828183, 2.71828183,
       2.71828183, 2.71828183, 2.71828183, 2.71828183, 2.71828183,
       2.71828183, 2.71828183, 2.71828183, 2.71828183, 2.71828183,
       2.71828183, 2.71828183, 2.71828183, 2.71828183, 2.71828183,
       2.71828183, 2.71828183, 2.71828183, 2.71828183, 2.71828183,
       2.71828183, 2.71828183, 2.71828183, 2.71828183, 2.71828183,
       2.71828183, 2.71828183, 2.71828183, 2.71828183, 2.71828183,
       2.71828183, 2.71828183, 2.71828183, 2.71828183, 2.71828183,
       2.71828183, 2.71828183, 2.71828183, 2.71828183, 2.71828183,
       2.71828183, 2.71828183, 2.71828183, 2.71828183, 2.71828183,
       2.71828183, 2.71828183, 2.71828183, 2.71828183, 2.71828183,
       2.71828183, 2.71828183, 2.71828183, 2.71828183, 2.71828183,
       2.71828183, 2.71828183, 2.71828183, 2.71828183, 2.71828183,
       2.71828183, 2.71828183, 2.71828183, 2.71828183, 2.71828183,
       2.71828183, 2.71828183, 2.71828183, 2.71828183, 2.71828183,
       2.71828183, 2.71828183, 2.71828183, 2.71828183, 2.71828183,
       2.71828183, 2.71828183, 2.71828183, 2.71828183, 2.71828183])

#This used the arange function by getting an array starting with zero and below 361 in units of 1#
arange(0,361)
Out[2]: 
array([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,
        13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,
        26,  27,  28,  29,  30,  31,  32,  33,  34,  35,  36,  37,  38,
        39,  40,  41,  42,  43,  44,  45,  46,  47,  48,  49,  50,  51,
        52,  53,  54,  55,  56,  57,  58,  59,  60,  61,  62,  63,  64,
        65,  66,  67,  68,  69,  70,  71,  72,  73,  74,  75,  76,  77,
        78,  79,  80,  81,  82,  83,  84,  85,  86,  87,  88,  89,  90,
        91,  92,  93,  94,  95,  96,  97,  98,  99, 100, 101, 102, 103,
       104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116,
       117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129,
       130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142,
       143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155,
       156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168,
       169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181,
       182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194,
       195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207,
       208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220,
       221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233,
       234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246,
       247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259,
       260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272,
       273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285,
       286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298,
       299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311,
       312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324,
       325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337,
       338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350,
       351, 352, 353, 354, 355, 356, 357, 358, 359, 360])

#By using the conversion rate of degrees to radians, I simply used the same command now with the units in radians# 
arange(0,361,(180/pi))
Out[5]: 
array([  0.        ,  57.29577951, 114.59155903, 171.88733854,
       229.18311805, 286.47889757, 343.77467708])

#By making sure to start with 12 and end with 17 in 0.2 units, I got an array that goes from 12 to 17 not including 17#
arange(12,17,0.2)
Out[6]: 
array([12. , 12.2, 12.4, 12.6, 12.8, 13. , 13.2, 13.4, 13.6, 13.8, 14. ,
       14.2, 14.4, 14.6, 14.8, 15. , 15.2, 15.4, 15.6, 15.8, 16. , 16.2,
       16.4, 16.6, 16.8])

#By adding 0.2, it allows me to add 17 to the array without going any further#
arange(12,17.2,0.2)
Out[7]: 
array([12. , 12.2, 12.4, 12.6, 12.8, 13. , 13.2, 13.4, 13.6, 13.8, 14. ,
       14.2, 14.4, 14.6, 14.8, 15. , 15.2, 15.4, 15.6, 15.8, 16. , 16.2,
       16.4, 16.6, 16.8, 17. ])

