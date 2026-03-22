#List is palindrome or not

def pallindrome(s):
    new_list = [i.lower() for i in s if i.isalnum()]
    start = 0
    end = len(new_list) -1
    flag =0 
    while(start<end):
        if (new_list[start] == new_list[end]):
            start += 1
            end -= 1
        else:
            flag = 1
            break
    if(flag == 0):
        print("This is pallindrome")
    else:
        print("This is not pallindrome")

print("Enter the string :")
name = input()
output = pallindrome(name)
#print(output)