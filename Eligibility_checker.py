age = int(input())
income = float(input())
citizen = input()
if(age>18 and income>30 and (citizen == 'yes'or 'y' or 'Y' )):
    print("Elgible")
else:
    print("Not")

