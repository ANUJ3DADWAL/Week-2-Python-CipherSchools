# def higher(a,b):
#     if a>b:
#         return "Greater"
#     return "Smaller"
# x=int(input("Enter a first Number: "))
# y=int(input("Enter Second Number: "))   
# print(f"a is {higher(x,y)} than b")  

#  now making a code for three numbers
def higher(a,b,c):
    if a>b and a>c:
        return a
    else:
        if b>a and b>c:
            return b
    return c
x=int(input("Enter First Number: "))
y=int(input("Enter Second No: "))
z=int(input("Enter Third Number: "))    
print(f"Number {higher(x,y,z)}  greater from all of this three Numbers")    