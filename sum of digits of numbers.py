n=int(input("Enter the number:"))
def digit(n):
    sum = 0
    while n >0:
        d=n%10
        sum=sum+d
        n=n//10
    print("sum of digits is:",sum)
digit(n)