n=input("Enter a String: ")  
def is_palindrom(x):
    if x==x[::-1]:
        return True
    return False
  
print(is_palindrom(n))        