import random
import string

length=int(input("Enter the length: "))

chars=string.ascii_letters + string.digits + string.punctuation
password=""

# password = ''.join([random.choice(chars) for i in range(length)])   optimization

for i in range(length):
  password += random.choice(chars)                  
    
print("Your random password is: ",password)