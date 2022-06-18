import os

while 1:
  command = input ("os:")
  os.system(command)
print("你是怎么退出的?")
filed = open("whatexit.txt")
filed.write(input ("请输入回答:"), "\n")
