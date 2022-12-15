# Example-1
n=int(input("Enter a number: "))
total=0
for i in range(0,n+1):
    total+=i
print(total)

# Example-2
n=input("Enter a two or more digit No: ")
total=0
for i in range(0,len(n)):
    total+=int(n[i])
print(total)    