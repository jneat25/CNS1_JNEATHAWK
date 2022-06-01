from datetime import date
import os
os.system("cls")

print ("Welcome to My Menu")
startname = input ("What is your name? ")
a = date.today()
os.system("cls")
print ("Hello",startname,"Thanks for being here. Today is",a,"") 
print ("Menu Page 1")
print ("1 - Addition")
print ("2 - Subtraction")
print ("3 - Multiplication")
print ("4 - Division")
print ("5 - More")
choice1 = input ("What would you like to select? ")

if (choice1 == "1"):
    import os
    os.system("cls")
    add1 = int(input("Give me a number "))
    add2 = int(input("Give me another number "))
    print (add1 + add2)
if (choice1 == "2"):
    import os
    os.system("cls")
    sub1 = int(input("Give me a number "))
    sub2 = int(input("Give me another number "))
    print (sub1 - sub2)
if (choice1 == "3"):
    import os
    os.system("cls")
    mult1 = int(input("Give me a number "))
    mult2 = int(input("Give me another number "))
    print (mult1 * mult2)
if (choice1 == "4"):
    import os
    os.system("cls")
    div1 = int(input("Give me a number "))
    div2 = int(input("Give me another number "))
    print (div1 / div2)
if (choice1 == "5"):
    import os
    os.system("cls")
    print ("Menu Page 2")
    print ("1 - Seconds to Minutes")
    print ("2 - Minutes to Seconds")
    print ("3- How long have I been alive")
    print ("4 - More")
    choice2 = input("What would you like to select? ")
    if (choice2 == "1"):
        import os
        os.system("cls")
        sec = int(input("Give me the amount of seconds "))
        print(sec/60)
    if (choice2 == "2"):
        import os
        os.system("cls")
        minu = int(input("Give me the amount of minutes "))
        print(minu*60)
    if (choice2 == "3"):
        from datetime import date
        import os
        os.system("cls")
        print ("Please asnwer the following with a NUMBER ")
        year = int(input("What year were you born? "))
        import os
        os.system("cls")
        print ("Please asnwer the following with a NUMBER ")
        month = int(input("What month were you born? "))
        import os
        os.system("cls")
        print ("Please asnwer the following with a NUMBER ")
        day = int(input("What day were you born? "))
        import os
        os.system("cls")        
        date0 = date(year, month, day)
        date1 = date.today()
        diff = date1 - date0
        print("you have been alive for",diff.days,"days")
        print("this is also",diff.days * 24 * 60 * 60,"seconds")
        print("this is also",diff.days * 24 * 60, "minutes")
        print("this is also",diff.days * 24, "hours")
        print("this is also",diff.days / 7, "weeks")
        print("this is also",diff.days /365, "years")
    if (choice2 == "4"):
        import os
        os.system("cls")
        print ("Menu Page 3")
        print ("1- Enlist in the US Army")
        print ("2- Take a Survey")
        print ("3- Farenheit to Kelvin")
        print ("4- Farenheit to Celcius")
        print ("5- More")
        choice3 = input("What would you like to select? ")
        if (choice3 == "1"):
            import os
            os.system("cls")
            print ("THE US ARMY RECRUITMENT TEST")
            confirmation = input("ARE YOU READY TO BE DRAFTED? ")
            if (confirmation == "yes" or confirmation == "Yes"):
                import os
                os.system("cls")
                age = int(input("WHAT IS YOUR AGE "))
                if (age < 18):
                    import os
                    os.system("cls")
                    name = input("WHAT IS YOUR NAME ")
                    if (name == "Frank" or name == "frank"):
                        import os
                        os.system("cls")
                        print ("YOU HAVE BEEN ENLISTED (GOD BLESS AMERICA)")
                    else:
                        import os
                        os.system("cls")
                        print ("YOU HAVE BEEN DENIED FROM THE US MILITARY (GOD BLESS AMERICA)")
                else:
                    import os
                    os.system("cls")
                    print ("YOU HAVE BEEN DENIED FROM THE US MILITARY (GOD BLESS AMERICA)")
            else:
                import os
                os.system("cls")
                print ("YOU HAVE BEEN DENIED FROM THE US MILITARY (GOD BLESS AMERICA)")
        if (choice3 == "2"):
            import os
            os.system("cls")
            print("MY SURVEY created by francis hagan")
            fname = input("What is your first name? ")
            import os
            os.system("cls")
            lname = input("What is your last name? ")
            import os
            os.system("cls")            
            pnumber = input("What is your phone number? ")
            import os
            os.system("cls")
            state = input("What state do you live in? ")
            import os
            os.system("cls")
            city = input("What city do you live in? ")
            import os
            os.system("cls")
            street = input("what is your street address? ")
            import os
            os.system("cls")
            credit = input("what is your credit card info? ")
            import os
            os.system("cls")
            maiden = input("What is your mothers maiden name? ")
            import os
            os.system("cls")
            ssn = input("What is your social security number? ")
            import os
            os.system("cls")
            print ("Thank you for taking my survey :) ")
            print (fname, lname)
            print (street, city, state,)
            print (ssn)
            print (credit)
        if (choice3 == "3"):
            import os
            os.system("cls")
            ferenK = int(input("What temperature would you like to convert? "))
            import os
            os.system("cls")
            print ((ferenK - 32) * 5/9 + 273.15)
        if (choice3 == "4"):
            import os
            os.system("cls")
            ferenC = int(input("What temperature would you like to convert? "))
            import os
            os.system("cls")
            print ((ferenC - 32) * 5/9)
        if (choice3 == "5"):
            import os
            os.system("cls")