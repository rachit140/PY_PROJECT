

#program to calculate no.
#by rachit sharma on 25 11 2022

first = int(input("enter your first no. "))
operator = input("enter your operator (+,-,*,/,%) : ")
second = int(input("enter your second number"))

if operator =="+":
    print (first+second)

elif operator =="-":
    print (first-second)

elif operator =="*":
    print (first*second)

elif operator =="/":
    print (first/second)

elif operator =="%":
    print (first%second)

else:
    print("invalid operation")