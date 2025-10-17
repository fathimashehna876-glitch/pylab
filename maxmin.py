a=int(input("Enter the first number :"))
b=int(input("Enter the second  number :"))
c=int(input("Enter thew third number :"))
if a>b and a>c:
    print("Largest:",a)
elif b>a and b>c:
    print("Largest:",b)
else:
    print("Largest:",c)
if a<b and a<c:
    print("Smallest:",a)
elif b<a and b<c:
    print("Smallest:",b)
else:
    print("Smallest:",c)
          
