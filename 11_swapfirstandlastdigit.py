#using integer:

num = int(input("Enter your number:"))
count = 0
n = num
while (n > 0):
    n = n//10
    count += 1



lastdigit = num % 10
firstdigit = num // 10**(count-1)
remaining = num % 10**(count-1)

swapnum = lastdigit * 10**(count-1) + remaining - lastdigit
swapnum = swapnum + firstdigit
print(count)
print(f"The Lastdigit is {lastdigit} and the firstdigit is {firstdigit} and the remaining number is {remaining}")
print("Swapped Number:", swapnum)


 
