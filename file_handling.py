
# x=open("abc.txt","r")
# y=x.read()
# print(y)

# #overwrite
# x=open("buggu.txt","w")
# x.write("this is new contact\n")
# x.write("welcome to new code")
# x.close()

# #append
# x=open("shejal.txt","a")
# x.write("new line added")


##second method
# with open("abc.txt","r")as file:
#     print(file.read())

# with open("abc.txt","a")as file:
#     print('new line added in this file')

# #somethig adding with append method
# with open("shejal.txt","a") as f:
#     f.write("we are from prayagraj\n")
#     f.write("india is a great country\n")
#     print("data appended successfully")

# with open("shejal.txt","r") as f:
#     line=f.readlines()
#     word="from kunda"
#     with open("shejal.txt","w") as f:
#         for line in line: 
#             if word not in line:
#                 f.write(line)

# remove =1
# with open("shejal.txt","r") as f:
#     line=f.readlines()
#     with open("shejal.txt","w") as f:
#         for i, line in enumerate(line):
#             if i!= remove:
#                 f.write(line)

# import os
# os.mkdir("AIPA.py")
# os.rename("AIPA.py","singh")
#remove directory
# os.rmdir("singh")

# #remove all files
# import shutil
# shutil.rmtree("singh")

# xyz = os.listdir(".")
# print(xyz)

# xyz = os.listdir()
# print(xyz)

# abc = os.getcwd()
# print(abc)

# os.mkdir("gungun")
# with open("gungun/student.txt","w") as file:
#     file.write("""student details:
#                 shejal, 
#                akriti, 
#                anamika""")
# print("details add.")

#practice
import os
#creat folder
# os.mkdir("studentData")
#inside studentdata create folder
os.mkdir("studentdata")
with open("studentdata/assignments","w") as file: