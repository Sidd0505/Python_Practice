def split_and_join(s):
    s1 = s.split(" ")
    s2 = "-".join(s1)
    return s2

print("Enter a string :")
try:
    name = input()
except valueerror:
    print("Not a corrct value!!")
result = split_and_join(name)
print(result)
