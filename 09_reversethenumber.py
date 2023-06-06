
n = int(input("enter the value of n:"))

rev_number = 0
while n >= 0:
    remainder = n%10
    rev_number = rev_number * 10 + remainder
    n = n // 10
print(rev_number)