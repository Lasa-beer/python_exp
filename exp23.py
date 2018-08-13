# *coding:utf-8 *
# Author : silence
# Time   : 2018/8/9 8:31
# File   : exp23.py
# IDE    : PyCharm

# python最大公约数 算法

def hcf(x,y):       # 该函数返回两个数的最大公约数
    # 获取两个数中的最小值
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1,smaller + 1):
        if (x % i == 0 and y % i == 0):
            hcf = i
    return  hcf

num1 = int(input('请输入第一个数字：'))
num2 = int(input('请输入第二个数字：'))

print('{0}和{1}的最大公约数为{2}'.format(num1,num2,hcf(num1,num2)))

