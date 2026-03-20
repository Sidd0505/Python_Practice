'''
print("Enter the value for 2 variables :")
a = int(input())
b = int(input())
sum = a+b
print(f"The {a} and {b} sum is :",sum)
'''

'''
print("Enter a Number :")
num = int(input())
new = 0
#a = num

while(num>0):
    a = num%10
    new = new*10 + a
    num = num//10

print("The number is :",new)
'''
'''
flag = 0
a = "This is a stringI"
for i in a:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i =='u'):
        flag += 1
print(flag)
'''

def vowels(text):
    vowelss = "aeiouAEIOU"
    flag =0

    for ch in text:
        if ch in vowelss:
            flag += 1

    return flag

word = input("Enter the input :")
print("The final value is : ",vowels(word))



