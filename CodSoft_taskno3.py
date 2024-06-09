import string
import random

def generate_password(length):
    # Define possible characters in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    # Prompt the user for the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length for the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print("Generated password:", password)

if _name_ == "_main_":
    main()
