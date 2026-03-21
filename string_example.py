def swap_case(s):
    s1 = ""
    for i in s:
        if(i.islower()):
            i = i.upper()
        else:
            i = i.lower()
        s1 = s1 + i
    return s1

print("Enter the string :")
name = input()
solution = swap_case(name)
print(solution)        