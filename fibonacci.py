a=0
b=1
print("Enter the number upto which the series is to be calculated : ")
n=int(input())
if(n<0):
    print("Enter a valid number")
elif(n==1):
    print(a)
elif(n==2):
    print(b)
else:
    print(a)
    print(b)
    for i in range(1,n):
        c=a+b
        a=b
        b=c
        print(c)
