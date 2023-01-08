# jazz
# intialize a empty list
jazz = []
str1 = "030"
# Loop through a range of numbers.
x = range(10)
for i in x:
# Append the square of i to the list
    jazz.append(str1 + str(i))

# Telenor
telenor = []
str2 = '034'
y = range(8)
for i in y:
    telenor.append(str2 + str(i))

# Ufone
ufone = []
str3 = '033'
z = range(8)
for i in z:
    ufone.append(str3 + str(i))

# Zong
zong = []
str4 = '031'
a = range(5)
for i in a:
    zong.append(str4 + str(i))

#Taking number as input from user.
num = (input("Enter Your Number: "))
# Assigning the length of a input to a new variable called "length".
length = len(num)
# Comparing if the length of a input is equal to 11 or not.
if length == 11:
    print("The number you entered is valid.")
# Checking if the length of a string is more then 11 or not.
if length > 11:
    print("The Number is Wrong kindly check and try again Thank you.")
# Checking if the length of a string is less then 11 or not.
if length < 11:
    print("The Number is not complete please check and try again Thank you.")

# Slicing a string a extracting first four elements from a string, and assigning it to a new variable.
first_four_digits = num[:4]

# Checking if first four elements were in zong list, if yes then printing the service provider.
if first_four_digits in zong:
    print("The service provider is zong.")
# Checking if first four elements were in Ufone list, if yes then printing the service provider.
if first_four_digits in ufone:
    print("The serivce provider is Ufone.")
# Checking if first four elements were in telenor list, if yes then printing the service provider.
if first_four_digits in telenor:
    print("The service provider is Telenor.")
# Checking if first four elements were in jazz list, if yes then printing the service provider.
if first_four_digits in jazz:
    print("The service provider is jazz.")


