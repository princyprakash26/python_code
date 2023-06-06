#Convert the number into conversion:s

n = int(input("enter a value:"))
newnum = 0
while n > 0:
   remainder = n%10
   newnum = newnum *10 + remainder
   n = n//10
print(newnum)


while newnum > 0:
    num = newnum % 10
    if num == 1:
        print('One', end=' ')
    elif num == 2:
        print("Two", end=' ')
    elif num == 3:
        print("Three", end=' ')
    elif num == 4:
        print("Four", end=' ')
    elif num == 5:
        print("Five", end=' ')
    elif num == 6:
        print("Six", end=' ')
    elif num == 7:
        print("Seven", end=' ')
    elif num == 8:
        print("Eight", end=' ')
    elif num == 9:
        print("Nine", end=' ')

    newnum = newnum // 10