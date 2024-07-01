# project-2
# Task 3: Password Generator
import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]
    all_characters = lower + upper + digits + special
    password += random.choices(all_characters, k=length - 4)

    random.shuffle(password)

    return ''.join(password)
if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    generated_password = generate_password(password_length)
    print(f"Generated Password: {generated_password}")
