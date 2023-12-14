#  WAP to accept a name from a user. 
# Raise and handle appropriate exception(s) 
# if the text entered by the user contains digits and/or special characters.

name = ''


while True:
    try:
        x = input("Enter Your Name : ")
        for i in x:
            if not(i.isalpha() or i.isspace()):
                raise Exception

        name = x 
        break
    
    except :
        print("You have entered wrong name. Try Again")


print("Yooooooo!!!! Your Name is ", name)
        