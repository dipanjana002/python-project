import random
import string

def generate_password(length):
    """Generate a random password"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    """Main function"""
    print("Random Password Generator")
    print("-------------------------")
    length = int(input("Enter the length of the password: "))
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == '__main__':
    main()
