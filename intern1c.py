#Copyright 2021 Asink Inc

   #importing module
import os
   #getting directory path as input
path=input("Enter path of directory whose files need to be displayed : ")
   #saving files in given directories' path,in variable
out=os.listdir(path)
   #printing elements in separate lines
for x in out:
 sub=("%s\%s"%(path,x))
 d=os.listdir(sub)
 if(len(d))!=0:
    for i in d:
     print("\t",d)
  
 
     
