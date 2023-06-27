#!/usr/bin/env python3

# myfile = open('/Users/rfnoc/tmp/python-starter/codebase/python-camp/00-Python-Object-and-Data-Structure-Basics/test.txt')

# content = myfile.read()

# print(content)

# myfile.seek(0)

# content = myfile.readlines()

# print(content)

# myfile.close()

with open('/Users/rfnoc/tmp/python-starter/codebase/python-camp/00-Python-Object-and-Data-Structure-Basics/test.txt', mode='r') as my_new_file:
    contents = my_new_file.read()

print(contents)
