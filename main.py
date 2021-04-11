import authenticationManager
import credentialsManager

    
    
def landingPage():
    print("\n"  )

    welcomeInput = input("Welcome to Pasword Keeper. Select an option to continue \n 1: Create a new account \n 2: Login into an existing account.\nPress enter to continue... \n")


    if welcomeInput != '1' and welcomeInput != '2':
        print('Please enter a valid input. \n')


    if welcomeInput == "1":

        newEmail = input("Please enter your email and press to continue... \n")

        newPassword1 = input("Please enter a new password and press enter to continue... \n")

        newPassword2 = input("Please re-enter the password and pressenter to continue... \n")

        res = authenticationManager.registerNewUser(newEmail, newPassword1, newPassword2)
        if (res["status"] == "success"):
            print("Thank you for creating a new account with us. Please log in to add password items.\n \n")
            landingPage()
            
        else:
            print("Login failed. Please try again or create a new account \n \n")
            landingPage()

    elif welcomeInput == "2":
        print("Please enter your email \n")
        newEmail = input("Please Enter to continue...")

        print("Please enter your password \n")
        newPassword1 = input("Please enter to continue...")
    
        res = authenticationManager.registerNewUser(newEmail, newPassword1, newPassword2)
        
        if (res["status"] == "success"):
            print("Log in Successful \n")
            input("Press enter to continue...")
            loggedIn()
        else:
            print("Login failed. Please try again or create a new account \n")

landingPage()