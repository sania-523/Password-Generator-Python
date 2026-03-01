import random
import string

print("---- PASSWORD GENERATOR ----")

length = int(input("Enter password length: "))

# All possible characters
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ''.join(random.choice(characters) for i in range(length))

print("Generated Password:", password)