a=raw_input("Enter the string:")
def strcount(string):
    d=dict()
    for n in string:
        if n not in d:
            d[n]=1
        else:
            d[n]+=1
    return d
print(strcount(a))
