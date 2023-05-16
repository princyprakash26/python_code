# #using string  method:(swap the first and lastdigit)
# num=int(input("get the number:"))
# i=0
# length=0

# n=str(num)
# firstnum=n[0]
# lastnum=n[length-1]
# newnum=n[1:-1]

# print("length=",len(n))
# print(n)
# print(type(n))
# print("num=",firstnum+lastnum)

# print('newnum=',lastnum+newnum+firstnum)
# swapnum=int(newnum)
# print(type(swapnum))



#using integer:

num=int(input("Enter your number:"))
count=0
n=num
while (n>0):
    n=n//10
    count+=1



lastdigit=num%10
firstdigit=num//10**(count-1)
remaining=num%10**(count-1)

swapnum=lastdigit*10**(count-1)+remaining-lastdigit
swapnum=swapnum+firstdigit
print(count)
print(f"The Lastdigit is {lastdigit} and the firstdigit is {firstdigit} and the remaining number is {remaining}")
print("Swapped Number:",swapnum)


 
