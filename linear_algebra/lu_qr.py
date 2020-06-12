'''
LU 分解和QR分解
'''

import numpy as np
import scipy.linalg as la
import numpy.random as rd

# rand函数，产生0到1的随机数，参数是shape
# randn函数，产生标准正态分布，均值为0，方差为1，参数也是shape
# randint函数，产生指定范围的随机整数，前两个参数表示范围，最后一个参数是size=（shape）

# 随机产生一个4*3矩阵
m = rd.rand(4, 3)

l, u = la.lu(m, permute_l=True)
q, r = la.qr(m)
print('q:', q) # q是m*n单位正交基
print('r:', r) # r是n*n上三角矩阵，且对角线元素为正
print(np.sum(q**2, axis=0))
