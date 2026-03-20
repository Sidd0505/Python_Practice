######
# print("Enter the number you want :")
# a = int(input())
# ans =1
# while(a>0):
#     ans = ans * a
#     a -= 1
# print(f'The answer is {ans}')

# print("Enter the number you want :")
# a = int(input())
# print(fact(a))

def fact(num):
    if num <= 1:  # Base case
        return 1
    else:
        return num * fact(num - 1)  # Recursive case

print("Enter the number you want :")
a = int(input())
print(fact(a))
