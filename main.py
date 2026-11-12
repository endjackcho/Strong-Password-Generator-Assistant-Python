import os

def clearing():
    os.system("cls")

sc = "`~!@#$%^&*)(-=_+][}{:;\|\'\',./?><\"\""

def start():
    while True :
        password = input("Enter your password : ")
        if len(password) < 6 :
            print("\n>> Your password length must higher then 6 characters !\n")
        elif password.isnumeric():
            print("\n>> Your password shoud't be jjust numbers !\n")
        elif password.islower() or password.isupper() :
            print("\n>> Use some special characters in your password !\n")
        else :
            score = 0
            b = True
            if "123" in password or "1234" in password or "12345" in password or "123456" in password or "1234567" in password or "123456789" in password or "abc" in password or "abcd" in password : b == False
            for i in password :
                if password.count(i) >= 10 and len(password) / 2 < password.count(i) : b == False
                if i.isnumeric() : score += 1.5
                elif i.isupper() : score += 1.5
                elif i.islower() : score += 1
                elif i in sc : score += 2
            if score <= 20 :
                print("\n>> Enter Stronger Password use more number, UpperCase words and Special Characters !\n")
            elif b == False :
                print("\n>> Don't reapit words or using templates !\n")
            elif score > 20 and b == True :
                print(f"\n>> Great !\n- Your strong Password : {password}") 
                input("\nEnter something to continue !\n- ")
                return password

def main()
    while True :
        clearing()
        print("\n>>>> Welcome !\n- I wanna help you to create a Strong Password !\nAre you ready ?")
        q = input("\n>> ")
        clearing()
        q = q.replace(" ","").lower()
        if q == "y" or q == "yes" or q == "yeah" or q =="yup" or q == "yep" or q == "ye" or q == "yu" or q == "yeet" or q == "are" or q == "bale" :
            print(start())
        else :
            print("\n>> Ok goodbye !\n")
            break

if __name__ == "__main__" :
    main()
    clearing()
    print("\n>> Thanks for choosing us ;)\n")