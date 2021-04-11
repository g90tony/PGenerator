import random 
import string 


def generateNewPassword(password_length):
    if (password_length < 8):
        print("A secure password should be no less that 8 characters. Please input a password length greater or equal to 8")
    else:
        letters = string.ascii_letters
        numbers = string.digits
        specialCharacters = string.punctuation


        acceptablePasswordCharacters = letters + numbers + specialCharacters
        generatedPassword = "".join(random.choice(acceptablePasswordCharacters) for i in range(password_length))

        # print("Your generared password is: " +generatedPassword)
    
        return generatedPassword
    