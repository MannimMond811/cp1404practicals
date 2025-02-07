"""
Define MINIMUM_LENGTH as 8
Prompt the user to enter a password: "Enter your password (more than 8 characters or alphabets)"
Get the length of the password
While the password length is less than MINIMUM_LENGTH:
    Print "Unqualified password"
    Prompt the user to re-enter the password
    Get the new password length
Print "*" repeated for the length of the password

"""
MINIMUM_LENGTH = 8
password = input("Enter your password(more than 8 numbers or alphabets):")
length = len(password)
while length < MINIMUM_LENGTH:
        print("Unqualified password")
        password = input("Enter your password(more than 8 numbers or alphabets):")
        length = len(password)
print("*" * length)