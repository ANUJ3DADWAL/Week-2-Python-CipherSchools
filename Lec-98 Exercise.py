def square_list(l):
    sq=[]
    for i in l:
        sq.append(i**2)
    return sq

number=list(range(1,100000000))
print(square_list(number))
    