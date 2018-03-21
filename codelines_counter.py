#coding=utf-8
'''
设计一个程序，用于统计一个项目中的代码数，包括文件个数，
代码行数，注释行数，空行行数
例如：
files:10
code_lines:200
comments:100
blanks:20
调用方法：在终端输入:python3 本文件名 路径 要查找的语言
目前只统计了python的，其他的类似
'''
import sys
import os

fpath = sys.argv[1]

def findFiles(path, L):
    try:
        parents = os.listdir(path)
    except:
        parents = ''
    for parent in parents:
        if parent.startswith('.'):
            continue
        child = os.path.join(path, parent)
        if os.path.isfile(child):
            #排除隐藏文件
            if not child.startswith('.') and child.split('.')[-1] == 'py':
                print(child)
                L.append(child)
        else:
            findFiles(child, L)

def counter(file_list):
    code_lines = 0
    blanks = 0
    comments = 0
    in_multi_comment = False
    for file_ in file_list:
        try:
            f = open(file_, encoding='utf-8')
            for line in f.readlines():
                line = line.strip()
                if line == '' and not in_multi_comment:
                    blanks += 1
                #''''''或""""""包含的单行注释，多行注释
                elif line.startswith('#') or \
                        (line.startswith("'''") and line.endswith("'''")) or \
                        (line.startswith('"""') and line.endswith('"""')) or \
                        (in_multi_comment and not(line.startswith("'''") or line.startswith('"""'))):
                    comments += 1
                elif line.startswith("'''") or line.startswith('"""'):
                    in_multi_comment = not in_multi_comment
                    comments += 1
                else:
                    code_lines += 1
        except:
            pass
        finally:
            f.close()
    print("files:", len(file_list))
    print("blanks:", blanks)
    print("code_lines:", code_lines)
    print("comments:", comments)

if __name__ == '__main__':
    fpath = sys.argv[1]
    file_list = []
    findFiles(fpath, file_list)
    counter(file_list)
