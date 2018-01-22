import os
import sys



def get_current_path():
    # 获取当前文件路径
    print('*****获取当前文件路径*****')
    print('__file__=%s' % (__file__))
    print('sys.argv[0]=%s' % (sys.argv[0]))

    # 获取当前文件夹路径
    print('\n*****获取当前文件夹路径*****')

    print('os.getcwd()=%s' % (os.getcwd()))
    print('sys.path[0]=%s' % (sys.path[0]))
    print('os.path.dirname(__file__)=%s' % (os.path.dirname(__file__)))
    print(os.path.abspath(os.path.join(os.getcwd(), '.')))
    print(os.path.abspath('.'))
    print(os.path.abspath(os.curdir))

    # 获取上级目录 os.path.abspath(当前路径) = 上级路径
    print('\n*****获取上级目录*****')

    print(os.path.abspath('..'))
    print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
    print(os.path.abspath(os.path.dirname(os.getcwd())))
    print(os.path.abspath(os.path.join(os.getcwd(), '..')))

    # 获取上上级目录
    print('\n*****获取上上级目录*****')

    print(os.path.abspath(os.path.join(os.getcwd(), '../..')))


if __name__ == '__main__':
    get_current_path()
