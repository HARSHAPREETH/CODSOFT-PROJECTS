import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    extra_special_chars = "@#$%^&*()-_=+[]{}|;:,.<>/?"
    
    while True:
        password = ''.join(random.choice(characters + extra_special_chars) for _ in range(length))
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password) and
            any(c in extra_special_chars for c in password)):
            return password

def password_generator():
    try:
        length = int(input("Enter the desired password length (minimum 8): "))
        if length < 8:
            print("Password length must be at least 8 characters.")
        else:
            password = generate_password(length)
            print(f"Generated password: {password}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

password_generator()
