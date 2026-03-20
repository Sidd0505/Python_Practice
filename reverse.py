def reverse(num):
    new = 0
    while num > 0:
        n1 = num % 10
        new = (new * 10) + n1
        num = num // 10
    print(new)


print("Enter a number to reverse :")
a = int(input())
reverse(a)
