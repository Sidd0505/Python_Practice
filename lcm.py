def gcf(num1, num2):
    num = 0
    flag = 1
    if(num1>num2):
        num = num1
    else:
        num = num2
    for i in range(1, num):
        if(num1%i ==0 and num2%i ==0):
            flag = i
    return flag
    
def lcm(num1, num2):
    ans =0
    ans = num1*num2//gcf(num1, num2)
    print(f"THe LCM of {num1} and {num2} is {ans}")

print("Enter the 2 numbers :")
a = int(input())
b = int(input())
lcm(a,b)

