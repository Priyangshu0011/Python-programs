a=int(input("Enter marks in 1st subject : "))
b=int(input("Enter marks in 2nd subject : "))
c=int(input("Enter marks in 3rd subject : "))
d=int(input("Enter marks in 4th subject : "))
e=int(input("Enter marks in 5th subject : "))
f=(((a+b+c+d+e)/500)*100)
if(e>=90):
   print("Grade O")
elif(e>90 and e<=80):
    print("Grade A+")
elif(e>80 and e<=75):
    print("Grade A")
elif(e>75 and e<=65):
    print("Grade B+")
elif(e>75 and e<=65):
    print("Grade B")
elif(e>75 and e<=65):
    print("Grade B+")
elif(e>65 and e<=60):
    print("Grade C")
elif(e>60 and e<=55):
    print("Grade D")
else:
    print("Fail")
