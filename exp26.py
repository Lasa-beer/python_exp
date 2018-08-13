# *coding:utf-8 *
# Author : silence
# Time   : 2018/8/9 9:02
# File   : exp26.py
# IDE    : PyCharm


# 文件 IO

# 写文件
with open("test.txt", "wt") as out_file:
    out_file.write("该文本会写入到文件中\n看到我了吧！")

# Read a file
with open("test.txt", "rt") as in_file:
    text = in_file.read()

print(text)