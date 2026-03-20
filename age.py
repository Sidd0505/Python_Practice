print("How many :")
num = int(input())
young =0
middle = 0
old =0
for i in range(0, num):
    print("Enter the Age :")
    try:
        age = int(input())
    except valueerror:
        print("You entered wrong value!!")
        break
    if(age >= 30 and age <= 50 ):
        middle = middle + 1
    if(age < 30 and age > 0):
        young = young + 1
    else:
        old = old + 1

print(f"The final count is : Young : {young}, Middle-Aged :{middle}, Old :{old}")


