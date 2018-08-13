# *coding:utf-8 *
# Author : silence
# Time   : 2018/8/8 17:35
# File   : exp13.py
# IDE    : PyCharm

#python 获取最大值函数
# N = int(input('请输入你要比较的数字的个数：'))
# print('请输入你要要比较的数字：')
# num = []
# for i in range(1,N + 1):
#     temp = int(input('请输入第 %d个数字'%i))
#     num.append(temp)
# print('您输入的数字为：',num)
# print('最大值为：',max(num))

N = int(input('请输入你要比较的数字的个数：'))

num = [int(input('请输入你要比较的数字：'))for i in range(1,N + 1)]

print('请输入的数字为:',list(num))
print('最大值为：',max(list(num)))