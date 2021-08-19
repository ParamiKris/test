#Copyright 2021 Asink Inc

   #importing module
import os,time
   #getting directory name as input
Name=input("Enter name of directory whose files need to be displayed : ")
   #using formatting to obtain final path
path=("C:\\%s"%(Name))
   #saving files in given directories' path,in variable
out=os.listdir(path)
   #printing elements in separate lines
for x in out:
   #getting path for each file
 uni_path=[os.path.abspath(x)]
 print(x,"\t",uni_path)
   #displaying modified date
 if os.path.isfile(x):
  print("last modified : %s"%(time.ctime(os.path.getmtime(x))))
