s = input("Enter a string: ")
count = 0
for i in range(len(s)):
    if (s[i] in 'aeiouAEIOU'):
        count=count+1
        print("The Number of vowels:", count)



