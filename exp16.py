# *coding:utf-8 *
# Author : silence
# Time   : 2018/8/8 18:00
# File   : exp16.py
# IDE    : PyCharm

#输出指定范围内的所有素数

lower = int(input('请输入区间最小值：'))
upper = int(input('请输入区间最大值：'))

for num in range(lower,upper + 1):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num)
