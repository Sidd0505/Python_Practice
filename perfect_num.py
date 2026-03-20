def perfect_num(num):
    ans = 0
    for i in range(2, num):
        if(num%i == 0):
            ans = ans + i
    ans += 1
    if(ans == num):
        print(f"The {num} is perfect number")
    else:
        print("Not a perfect number")

print("Enter a number :")
a = int(input())
perfect_num(a)
