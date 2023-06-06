
a = input("Enter Any String:")
char = "l"
result = 0
i = 0
print(len(a))
while i < len(a):
    if a[i] == char:
        result += 1
    i += 1

print("Result=", result)