print("Enter the number of terms you want of fibonacci sequence")
n = int(input())
a = 0;
b = 1;
print("Fibonacci sequence is: ")
print(a,",", b, end=" , ")
for i in range(2, n):
    n = a+b
    print(a+b, end=" , ")
    a = b
    b = n
print("............")