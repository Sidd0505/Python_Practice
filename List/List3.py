'''
list1 = [1,5,4,2,3]
rev = []

for i in list1:
    rev = [i] + rev
print(rev)
'''
'''
mylist = [7,5,1,4,2]
for i in range(len(mylist)):
    for j in range(len(mylist)-1):
        if(mylist[j]>mylist[j+1]):
            mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
print(mylist)
'''

def bubble_sort(mylist):
    for i in range(len(mylist)):
        for j in range(len(mylist)-1-i):
            if(mylist[j]>mylist[j+1]):
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
    return mylist


mylist = [7,5,1,4,2]
print(bubble_sort(mylist))