import random
import string

def generate_password(length, strength="strong"):
    if strength == "weak":
        characters = string.ascii_letters
    elif strength == "medium":
        characters = string.ascii_letters + string.digits
    else:  # strong
        characters = string.ascii_letters + string.digits + string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

print("=== Password Generator ===")
try:
    length = int(input("Enter password length (6-32): "))
    if length < 6 or length > 32:
        print("Password length must be between 6 and 32.")
    else:
        strength = input("Choose strength (weak/medium/strong): ").lower()
        password = generate_password(length, strength)
        print("Generated Password:", password)

        # Save option
        save = input("Do you want to save this password? (y/n): ").lower()
        if save == "y":
            with open("passwords.txt", "a") as f:
                f.write(password + "\n")
            print("Password saved to passwords.txt ✅")
except ValueError:
    print("Please enter a valid number!")
