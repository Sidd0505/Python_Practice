thislist = ["Apple", "Orange", "Banana"]
print(thislist[0:-1])

#print(type(thislist[0]))

list1 = ["Apple", "Banana", "Orange"]
list1[1] = "Ba"
print(list1[1])

#How to insert in list : append, insert(insert will insert the element before index position mentioned)
list1.append("Grapes")
print(list1)
list1.insert(-1, "Lily")
print(list1)

#Remove items from list : remove, pop, clear(will remove all the contents of list)
list1.remove("Ba")
print(list1)
list1.pop(0)
print(list1)

#List comprehension - This method syntax  is used for filtering
newlist = [x for x in thislist if x!="Orange"]
print(newlist)

#List comprehension - This method syntax is used for replacing the current element
newlist2 = [x if x != "Banana" else "Chocolate" for x in thislist]
print(newlist2)

#Sorting the list
thislist.sort()
print(thislist)

thislist.sort(reverse = True)
print(thislist)

list3 = ["Apple", "Orange", "banana", "kiwi", "audi"]
list3.sort(key = str.lower)
print(list3)

#Reverse the list - This will not sort the list - it will reverse directly
list3.reverse()
print(list3)

#Copy a list 
mylist = thislist.copy()
print(mylist)

newlist = list(mylist)
print(newlist)

n1 = mylist[:]
print(n1)

#Join List
n2 = n1 + newlist
print(n2)

n2.extend(n1)
print(n2)