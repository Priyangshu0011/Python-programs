a,b,c=int(input("A :")),int(input("B: ")),int(input("C: "))
if(a==b==c):
    print("Equilateral traingle")
elif(a!=b and b!=c and c!=a):
    print("Scalene Triangle")
elif(a==b or b==c or c==a):
    print("Isosceles Triangle")
