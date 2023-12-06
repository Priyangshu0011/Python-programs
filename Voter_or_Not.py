age=int(input("Enter the age : "))
if(age>=18):
    print("You are allowed to vote")
    print(" ")
    if(18<=age<=25):
        print("Young preference last")
    elif(25<age<=45):
        print("Adult give second preference")
    elif(45<age<=60):
        print("Middle age given first preference")
    else:
        print("Old age will be allowed without line")
else:
    print("Not aloowed to vote")
