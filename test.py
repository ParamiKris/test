#Copyright 2021 Asink Inc

 #importing modules
import os
from pathlib import Path
import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument('--folder',type=str,required=True)
parser.add_argument('--ignore',type=str)
parsed_args = parser.parse_args()
avoidr=parsed_args.ignore
  #getting current directory as input
if '.' in parsed_args.folder:
  path = os.getcwd()
  #getting directory path as input
elif os.path.exists(parsed_args.folder):
 path=parsed_args.folder
  #handling wrong inputs and exiting
else:
    print("give proper path")
    sys.exit()
  #checking for type of slash
if "\\" in path:
  slash_char="\\"
elif "/" in path:
  slash_char="/"
  #path's length and slash's count
length=len(path)
slash=path.count(slash_char)
if os.path.exists(path):
 def listdirs(rootdir):
    global exist
    for it in os.scandir(rootdir):
      extras=(it.path.count(slash_char))
      if it.is_dir() or it.is_file():  
         length2=len(it.path)
        #indenting sub-directories, keeping directories at corner
         if extras-slash==1:
             print(it.path[length+1:length2+1])
         else:
            i=extras-slash 
            j="\t"*i
            print(j,it.path[length+1:length2+1])
         with open(avoidr,'r') as g:
            omit=g.readlines()
            if it.path in omit:
                break
            else:
              if it.path.endswith('.py'):
               with open(it.path,'r')as f:
                reader=f.readlines()
                exist=False
                for row in reader:
                 if not row.strip():
                   continue
                 elif "#Copyright 2021 Asink Inc" in row:
                   exist=True
                   break
                 else:
                  exist=False
                  break
               if exist==False:
                with open(it.path,'r+')as f:
                 lines=f.read()
                 f.seek(0,0)
                 f.write("#Copyright 2021 Asink Inc".rstrip('\r\n')+'\n'+'\n'+lines)
              else:
               if it.is_dir():
              #iterating for sub-directories
                 listdirs(it)
 #function call
 listdirs(path)

