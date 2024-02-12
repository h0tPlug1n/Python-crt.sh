#!/bin/python3
from crtsh import crtshAPI # pip3 install crtsh
import sys

f = open("from-crtsh.txt",'a')
out = list(crtshAPI().search('%.'+sys.argv[1]))
for i in out:
        if(not(i["name_value"].find("*"))):
                continue
        f.write(i["name_value"]+"\n")