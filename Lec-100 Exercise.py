# reversing using slicing method
# def reverse(l):
#     return l[::-1]
# numbers=[1,2,3,4,5,6,7,8,9,10] 
# print(reverse(numbers))



# reversing using reverse method 
# def reverse(l):
#     l.reverse()
#     return l
# num=[1,2,3,4,56,7,89,45]    
# print(reverse(num))        


# reversing using append and pop method
def reverse(l):
    rev=[]
    for i in range(len(l)):
        popped=l.pop()
        rev.append(popped)
    return rev
num=[1,2,3,4,56,7,89,45] 
print(reverse(num))     
