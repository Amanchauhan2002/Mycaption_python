print("Enter the element in the list")
list1 = input().split()
print("list = ",list1)
print("Positive number = ",end="")
for i in list1:
    if int(i) > 0:
        print(i,end=", ")

