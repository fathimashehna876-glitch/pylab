n = int(input("Enter the number of terms: "))
f1 = 0
f2 = 1
count = 0

print("Fibonacci series of", n, "terms:")

while count < n:
    print(f1, end=" ")
    temp = f1 + f2
    f1 = f2
    f2 = temp
    count += 1
