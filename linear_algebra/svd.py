'''
奇异值分解
'''

import numpy as np
import numpy.linalg as la
import numpy.random as rd

# rand函数，产生0到1的随机数，参数是shape
# randn函数，产生标准正态分布，均值为0，方差为1，参数也是shape
# randint函数，产生指定范围的随机整数，前两个参数表示范围，最后一个参数是size=（shape）

# 随机产生一个4*3矩阵
# m = rd.rand(4, 3)
m = np.array([[4, 11, 14], [8, 7, -2]])

s, v, d = la.svd(m)
print('s:', s)
print('v:', v)
print('d:', d)