# 通过用户输入两个数字，并计算两个数字之和

num1 = input('请输入第一个数字：')
num2 = input('请输入第二个数字：')

sum = float(num1) + float(num2)
print('数字{0}和{1}相加的结果为：{2}'.format(format(num1),format(num2),sum))
