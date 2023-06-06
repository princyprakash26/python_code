
a = input("enter your value:")
revstring = ""
i = len(a)
print(i)
while i > 0:
   revstring += a[i-1]
   i -= 1
print(revstring)    
if revstring == a:
    print("This string is a palindrome", a)
else:
    print("No,this string is not a palindrome", revstring)    
