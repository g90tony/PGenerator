import userManager
import credentialsManager

verifiedEmail = ""

    
    
def landingPage():

    welcomeInput = input("Welcome to Pasword Keeper. Select an option to continue \n 1: Create a new account \n 2: Login into an existing account.\nPress enter to continue... \n")


    if welcomeInput != '1' and welcomeInput != '2':
        print('Please enter a valid input. \n')
        landingPage()


    if welcomeInput == "1":

        newEmail = input("Please enter your email and press to continue... \n")

        newPassword1 = input("Please enter a new password and press enter to continue... \n")

        newPassword2 = input("Please re-enter the password and pressenter to continue... \n")

        res = userManager.registerNewUser(newEmail, newPassword1, newPassword2)
        if (res["status"] == "success"):
            print("Thank you for creating a new account with us. Please log in to add password items.\n \n")
            landingPage()
            
        else:
            print("Login failed. Please try again or create a new account \n \n")
            landingPage()

    elif welcomeInput == "2":
        newEmail = input("Please enter your email and press enter to continue...\n")
        newPassword1 = input("Please enter your password and press enter to continue...\n")
    
        res = userManager.loginUser(newEmail, newPassword1)
        
        if (res["status"] == "success"):
            print("Log in Successful \n")
            verifiedEmail = newEmail
            loggedIn()
        else:
            print("\n Login failed. Please try again or create a new account \n")
            landingPage()
            
       
def loggedIn():
    authenticatedUser = credentialsManager.Credentials(verifiedEmail)
    authenticatedUser.isAuthenticated = True
    # authenticatedUser.loadPasswords()


    authenticatedInput = input("Welcome back. Select an option to continue \n 1: Generate a new account credential \n 2: Add an existing account credentials.\n 3: Genereate a secure password \n 4: Logout\n Press enter to continue...\n")


    if authenticatedInput != '1' and authenticatedInput != '2' and authenticatedInput != '3' and authenticatedInput != '4':
        print('Please enter a valid input. \n')
        loggedIn()


    if authenticatedInput == "1":

        name = input("Please enter a name for the new entry and press to continue... \n")

        username = input("Please enter the account username or email and press enter to continue... \n")

        passwordLength = int(input("Please enter the length of your new password (min: 8) and press enter to continue... \n"))

        res = authenticatedUser.createNewCredentialItem(name, username, passwordLength, verifiedEmail)
        
        if (res["status"] == "success"):
            print("The new item has been saved and generated a password for you: {}.\n \n".format(res["data"]))
            loggedIn()
            
        else:
            print("There was a problem saving the entry. Please try again \n \n")
            loggedIn()

    elif authenticatedInput == "2":
        name = input("Please enter a name for the new entry and press to continue... \n")

        username = input("Please enter the account username or email and press enter to continue... \n")

        password = input("Please enter the account password and press enter to continue... \n")

        res = authenticatedUser.addExistingCredentialItem(name, username, password, verifiedEmail)
        
        if (res["status"] == "success"):
            print("The new item has been saved and generated a password for you: {}.\n \n".format(res["data"]))
            loggedIn()
            
        else:
            print("There was a problem saving the entry. Please try again \n \n")
            loggedIn()
            
    elif authenticatedInput == "3":
       try:
            quickPasswordLength = int(input("Please enter the length of your new password (min: 8) and press enter to continue... \n"))
            print("Your generated password is: {}".format(authenticatedUser.generateVerifiedPassword(quickPasswordLength)))
            loggedIn()
            
       except Exception as e :
           print('There was a fatal error: {}'.format(e))

    elif authenticatedInput == "4":
        authenticatedUser.isAuthenticated = False
        print("You have successfully logged out.")
        landingPage()
            
landingPage()