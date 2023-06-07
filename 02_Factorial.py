#Factorial of the given number:
n = int(input("Enter the value:"))
fact = 1
num = 1
while num <= n:
    fact = fact * num
    num += 1
print("Factorial of The given number:", fact)
