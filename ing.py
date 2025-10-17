w=input("Enter a word:")
if len(w)<=3:
    print("This string is not valid!!!")
elif w[-3:]=="ing":
    replace=w.replace("ing","ly")
    print("replaced word is:",replace)