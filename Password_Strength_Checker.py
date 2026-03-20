def password(text):
    special_ch = "@#$%^&*"
    digits = "0123456789"
    flag = 0
    a = False
    b = False
    c = False
    for ch in text:
        if ch in special_ch :
            a = True
        if ch in digits :
            b = True
        '''
        flag+= 1
        if flag >= 8:
            c = True
        else: 
            c = False
        '''
    if len(text)>= 8:
        c = True
    if (a and b and c):
            print("strong Password")
    else :
        print("Weak password")

word = input('Enter the Password :')
password(word)
            

