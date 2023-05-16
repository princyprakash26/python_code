
n1=int(input("enter the value of num1:"))
n2=int(input("enter the value of num2:"))
n3=int(input("enter the value of num3:"))
#find the greatest value of these Numbers:
if (n1>=n2) and (n1>=n3):
    print("num1 is the greatest number:",n1)
elif (n2>=n1) and (n2>=n3):
    print("num2 is the greatest number:",n2)
else:
    print("num3 is the greatest number:",n3)