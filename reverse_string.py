def reverse_string(s):
    new_list = list(s)
    left = 0
    right = len(new_list)-1
    while(left<right):
        new_list[left], new_list[right] = new_list[right], new_list[left]
        left +=  1
        right -= 1
    return "".join(new_list)  #To convert the list into string

print("Enter a string :")
name = input()
output = reverse_string(name)
print(output)