
string=input("Enter any value:")

vowels=0
consonants=0
empty_space=0
j=0
while j<len(string):
    if (string[j]=='a' or string[j]=='e' or string[j]=='i' or string[j]=='o' or string[j]=='u' or string[j]=='A' or string[j]=='E' or string[j]=='I' or string[j]=='O' or string[j]=='U'):
        vowels +=1

    elif (string[j]==" "):
        empty_space +=1
    else:
        consonants +=1

    j +=1

print("Vowels:",vowels)
print("Consonants:",consonants)


