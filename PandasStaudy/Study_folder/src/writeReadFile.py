import sys
#===============================================================================
# s1 = '''How many seas must a white dove sail
# Before she sleeps in the sand'''
# s2 = """How many roads must a man walk down
# Before they call him a man"""
# path_file = r'C:\Users\yzhou\Documents\Workspace\pythonStudy\testStudy\src.txt'
# dest_file = r'C:\Users\yzhou\Documents\Workspace\pythonStudy\testStudy\dest.txt'
# f1 = open(path_file, 'w+')
# f1.write(s1)
# f1.seek(0)
# rString = f1.readlines()
# print rString
# f1.close()
# f2 = open(dest_file, 'w+')
# f2.write(s2)
# f2.write('\n')
# f2.writelines(rString)
# f2.seek(0)
# rString = f2.readlines()
# print rString
# f2.close()
#===============================================================================
s3 = '''Life is short, you need Python.
Simple is better than complex.'''
path_file1 = r'C:\Users\yzhou\Documents\Workspace\pythonStudy\testStudy\test.txt'
f3 = open(path_file1, 'w+')
f3.write(s3)
f3.seek(0)
fp = open(path_file1, 'r+', 0)
fp.readline()
fp.seek(10, 1)
print fp.readline()