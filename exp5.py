# *coding:utf-8 *
# Author : silence
# Time   : 2018/8/8 9:54
# File   : exp5.py
# IDE    : PyCharm

# 计算三角形的面积

a = float(input('请输入三角形的第一边长：'))
b = float(input('请输入三角形的第二边长：'))
c = float(input('请输入三角形的第三边长：'))

#计算半周长
s = (a + b + c)/2

#计算面积
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print('三角形面积为：%0.3f'%area)

