
def is_leap(year):
    flag = False
    if(year%400 == 0) or (year%4 ==0 and year%100 != 0):
        return True
    return flag

year = int(input())
print(is_leap(year))