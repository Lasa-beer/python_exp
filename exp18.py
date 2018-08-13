# *coding:utf-8 *
# Author : silence
# Time   : 2018/8/8 18:14
# File   : exp18.py
# IDE    : PyCharm


# 九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(i, j, i*j), end='')
    print()
