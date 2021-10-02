list=[]
n=int(input("Enter the number of elements:"))
print("Enter the elements:")
for i in range(0,n):
    ele=int(input())
    list.append(ele)
print("The list is:")
for i in range(0,n):
    print(list[i])
print("The updated list is:")
for num in list:
    if num>=0:
        print(num)
