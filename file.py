filename = input("Enter the filename: ")

if '.' in filename and filename.rfind('.') != 0:
    extension = filename.split('.')[-1]
    print("The extension of the file is:", extension)
else:
    print("No extension found.")
