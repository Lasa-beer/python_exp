# *coding:utf-8 *
# Author : silence
# Time   : 2018/8/8 10:04
# File   : exp7.py
# IDE    : PyCharm

# 摄氏度和华氏度相互转化

a = int(input('摄氏度转为华氏度请按1\n'
              '华氏度转化为摄氏度请按2\n'))
while a != 1 and a != 2:
    a = int(input('您输入的不正确，请重新输入：'))

if a == 1:
    c = float(input('请输入摄氏度：'))
    f = (c * 1.8) + 32  # 摄氏度 华氏度转化公式
    print('%0.1f 摄氏度转化为华氏度为：%0.1f'%(c,f))
else:
    f = float(input('请输入华氏度：'))
    c = (f - 32)/ 1.8
    print('%0.1f 华氏度转化为摄氏度为：%0.1f'%(f,c))
