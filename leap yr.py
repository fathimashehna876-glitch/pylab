
year = int(input("Enter starting year: "))
final_year = int(input("Enter final year: "))

print("Leap years:")

while year <= final_year:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year)
    year += 1
