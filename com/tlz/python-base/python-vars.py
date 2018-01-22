
'''
python 变量 作用域🌧


PYTHON的作用域由def、class、lambda等语句产生，
if、try、for等语句并不会产生新的作用域。
变量名引用分为三个作用域进行查找：
首先是本地，然后是函数内（如果有的话），之后是全局，最后是内置。
'''

for i in range(3):
    print(i)
print('i = ', i)
