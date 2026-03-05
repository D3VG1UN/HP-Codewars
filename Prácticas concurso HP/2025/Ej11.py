#Armstrong numbers
num=input()

totalnum=0

for i in range(len(num)):
    totalnum+=int(num[i])**int(len(num))

if totalnum==int(num):
    print("True")
else:
    print("False")