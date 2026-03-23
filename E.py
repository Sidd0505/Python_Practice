#print How many elements and the unique list without duplicates
def re_du(s):
    k = 1
    for i in range(1, len(s)):
        if(s[i]!=s[i-1]):
            s[k] = s[i]
            k += 1
    return k

new_list = [1,1,2,2,3,3,4]
k = re_du(new_list)
print(k)
print(new_list[:k])