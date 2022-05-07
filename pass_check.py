import re
print ('Password must Contain:\n\tAtleast Seven Characters\n\tAtleast One Uppercase Letter\n\tAtleast One Lowercase Letter\n\tAtleast One Numeric Digit\n\tAtleast One Special Characters\n\tNo Spaces')
p= input("Input your password : ")
x = True
while x:  
    if len(p)<7:
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")
