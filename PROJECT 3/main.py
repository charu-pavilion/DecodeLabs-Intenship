#generate a random password
import random

import string

charValues = string.ascii_letters + string.digits + string.punctuation

pass_length = int(input("Enter the length of the password: "))
password = ""
password = "".join([random.choice(charValues) for i in range(pass_length)])
print("Your random password is: ", password)


