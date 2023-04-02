'''
Generate Password.

This code defines a generate_password() function that takes an optional length parameter (defaulting to 8) and returns a random password of that length. The password includes a mix of uppercase and lowercase letters, digits, and punctuation marks.
The if __name__ == '__main__': block allows the code to be executed as a standalone script. It prompts the user for the desired length of the password and then calls generate_password() to generate a password of that length. Finally, it prints the password to the console.
You can customize this code to suit your needs, for example by adding additional options for the types of characters to include in the password, or by integrating it into a larger application.

Reference:
  - https://www.freecodecamp.org/news/python-projects-for-beginners/#qr-code-encoder-decoder-python-project
'''


import random
import string

def generate_password(length=8):
    """Generate a random password with the given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == '__main__':
    length = int(input("Enter the length of the password: "))
    password = generate_password(length)
    print("Your password is:", password)