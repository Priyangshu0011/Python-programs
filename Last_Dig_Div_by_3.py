#wap to take a no from a user and check whether the last digit of the no is divisible by 3 or not
a=int(input("Enter a Number : "))
if((a%10)%3==0):
    print("Number is divisible by 3")
else:
    print("Number is not divisible by 3")
