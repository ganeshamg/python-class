# nested if
# percentage = 55

# if(percentage>=40):
#     print("user is pass")
#     if(percentage>=80):
#         print("user in distinction")
#     elif(percentage>=60):
#         print(user in first dicision)
# else:
#     Print("fail")


         
# singleline if
# gender = "M"
# if (gender=="M"):
#  print("male")
# else:
#    print("female")

# gender = "M"
# a = "Male" if gender=="M" else "Female"
# print(a)

# a = "ganesh"
# print(a.upper())
# print(a.title())
# print(a. lower())
# print(a.capitalize())


# a = int(input("percentage of student"))
# if(a>=80):
#     print("distinction")
# elif(a>=60 and a<80):
#     print("first division")
# elif(60>a>=40):
#     print("second division")
# elif(40>a>=30):
#     print("third division")
# else:
#     print("fail")

_marks = int(input("enter marks obtains"))

print(_marks)

if(_marks > 100 or _marks < 0):
    print("your number is invalid. Number between 0 and 100 is only acceptable")
elif(_marks >= 80):
    print("you have scored a distinction")
elif(_marks >= 60):
    print("you have scored first division")
elif(_marks >= 50):
    print("you have scored second division")
elif(_marks >= 40):
    print("you have scored third division")
else:
    print("you have failed")

# nested if
percentage = float(input("enter the percentage of the student"))
if(percentage>=40):
    if(percentage<=100):
        print("user is pass")
        if(percentage>=80):
            print("distinction")
        elif(percentage>=60):
            print("first division")
        elif(percentage>=50):
            print("second division")
        elif(percentage>=40):
            print("third division")
    else:
        print("the marks entered is invalid")
else:
    print("the student has failed")
    
    