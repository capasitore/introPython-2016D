__author__ = 'andaro'
import os.path
import os
import sys
#ta in path argument


my_path = "/chalmers/users/andaro/Desktop/test1/"


for root, dirs, files in os.walk(my_path, topdown=False):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))

#
#
# def getSize(filename):
#     st = os.stat(filename)
#     return st.st_size
#
# my_path = "/chalmers/users/andaro/Desktop/test1/"
#
# files = os.listdir(my_path)
# print files
#
#
# print getSize(my_path)
#
#
#
# #for i in files:
# #    files[i].
#
# #print 'Argument', str(sys.argv)
# #print filer i mappen