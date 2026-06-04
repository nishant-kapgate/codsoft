import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase 
    if use_lower:
        characters += string.ascii_lowercase 
    if use_digits:
        characters += string.digits 
    if use_symbols:
        characters += string.punctuation 

    if not characters:
        print("Error: You must select at least one character type!")
        return None
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

def get_yes_no(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ("y", "yes"):
            return True
        elif choice in ("n", "no"):
            return False
        else:
            print("Please enter y or n.")

def main():
    print("\n===== Password Generator =====\n")
    while True:
        try:
            length = int(input("Enter password length: "))
            if length < 1:
                print("Length must be at least 1.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    use_upper = get_yes_no("Include uppercase letters? (y/n): ")
    use_lower = get_yes_no("Include lowercase letters? (y/n): ")
    use_digits = get_yes_no("Include digits? (y/n): ")
    use_symbols = get_yes_no("Include symbols? (y/n): ")
    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)

    if password:
        print(f"\nYour generated password: {password}")
        print(f"Password length: {len(password)}")
    while get_yes_no("\nGenerate another password? (y/n): "):
        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        if password:
            print(f"\nYour generated password: {password}")
            print(f"Password length: {len(password)}")

    print("\nThank you for using Password Generator!")
if __name__ == "__main__":
    main()