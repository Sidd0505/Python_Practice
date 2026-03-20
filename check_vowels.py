def check_vowels(str):
    flag = 0
    vowels = "aeiouAEIOU"
    for i in str:
        if i in vowels:
            flag += 1
    if(flag >0):
        print(f"The word {str} has vowels")
    else:
        print(f"The word {str} does not have vowels")

print("Enter the string :")
a = input()
check_vowels(a)
        