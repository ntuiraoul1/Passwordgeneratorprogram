import random
import string

print("Welcome to another pypassword generator program")

length = int(input("Enter the length of the password"))

lower = string.ascii_lowercase
upper =string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = upper + lower + num + symbols

temp = random.sample(all,length)

password = "".join(temp)

print(password)