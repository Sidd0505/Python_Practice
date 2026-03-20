mylist = ["a", "b", "c"]
mylist[1:2] = ["x", "y"]
print(mylist[2])

print(len(mylist))

#Insert Items in List : 
mylist.insert(-1, "cherry")  #In Python, list.insert(index, element) inserts the element before the specified index position.
print(mylist)
print(len(mylist))

mylist.append("z")
print(mylist)

mylist2 = ["g", "h"]
mylist.extend(mylist2)
print(mylist)

#Remove items from list :
mylist.remove("x")
print(mylist)
mylist.pop(2)
print(mylist)
del mylist[-1]
print(mylist)

flag = 0
for i in range(len(mylist)):
    if(mylist[i]=="y"):
        flag += 1
print(flag)

f1 = len([x for x in mylist if x =="y"])
print(f1)

