'''
特征值 特征向量
'''
import numpy as np
import numpy.linalg as la
import numpy.random as rd

# rand函数，产生0到1的随机数，参数是shape
# randn函数，产生标准正态分布，均值为0，方差为1，参数也是shape
# randint函数，产生指定范围的随机整数，前两个参数表示范围，最后一个参数是size=（shape）

# 随机产生一个3*3矩阵
m = rd.rand(3, 3)

# m = np.array([[4, -1, 6],
#               [2, 1, 6],
#               [2, -1, 8]])

print('m:', m)
# 对矩阵求特征值和特征向量
rs, vs = la.eig(m)
# 打印特征值
print('rs:', rs)
# 特征向量
print('vs:', vs)

for i in range(m.shape[0]):
    v1 = np.matmul(m, vs[:, i])
    v2 = rs[i] * vs[:, i]
    print('m * vs[{}]:'.format(i), v1)
    print('rs[{0}] * vs[{0}]:'.format(i), v2)
    distance = np.sum(np.square(v2 - v1))
    print('distance', distance)