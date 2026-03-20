print("Enter how many numbers :")
num = int(input())
a = 0
b = 1
print("0\n1")

for i in range(2, num):
    c = a + b
    a, b = b, c
    print(c)