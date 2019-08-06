'''
@Description: 
@Author: FWZ
@Date: 2019-08-06 10:00:26
'''

import os
import sys


def get_file_list(dir):
    list = []
    for (dirpath, dirnames, filenames) in os.walk(dir):
        list.extend(filenames)
        break
    return list

if len(sys.argv) < 3:
    print("please enter oldstr,newstr and dir paras.like this: renamefile.py 720p 1080p path")
    exit(1)

oldstr = sys.argv[1]
newstr = sys.argv[2]
try:
    path = sys.argv[3]
except:
    path = "./"

all_files = get_file_list(path)


for x in all_files:
    if oldstr in x:
        print(x)
        newfilename = x.replace(oldstr,newstr)
        of = os.path.join(path,x)
        nf = os.path.join(path,newfilename)
        print("rename {} to {}".format(of,nf))
        os.rename(of,nf)

print(oldstr, newstr)
