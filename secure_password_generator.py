import secrets
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        raise ValueError("At least one character set must be selected.")

    return ''.join(secrets.choice(chars) for _ in range(length))

if __name__ == "__main__":
    print("=== Secure Password Generator ===")
    length = int(input("Enter password length: "))
    upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    digits = input("Include digits? (y/n): ").lower() == 'y'
    symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, upper, digits, symbols)
    print(f"\nGenerated Password: {password}")
