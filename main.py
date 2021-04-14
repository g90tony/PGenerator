import os 

import authenticator
import user
import credentialsManager
import credentials

    
def landingPage():
    try:
        os.mkdir("./user_files/")
        
    except Exception as e:
        print(e)
        
        
    welcomeInput = input("Welcome to Pasword Keeper. Select an option to continue \n 1: Create a new account \n 2: Login into an existing account.\nPress enter to continue... \n")


    if welcomeInput != '1' and welcomeInput != '2':
        print('Please enter a valid input. \n')
        landingPage()


    if welcomeInput == "1":

        newEmail = input("Please enter your email and press to continue... \n")

        newPassword1 = input("Please enter a new password and press enter to continue... \n")

        newPassword2 = input("Please re-enter the password and pressenter to continue... \n")

        res = authenticator.registerNewUser(newEmail, newPassword1, newPassword2)
        if (res["status"] == "success"):
            print("Thank you for creating a new account with us. Please log in to add password items.\n \n")
            landingPage()
            
        else:
            print("Login failed. Please try again or create a new account \n \n")
            landingPage()

    elif welcomeInput == "2":
        newEmail = input("Please enter your email and press enter to continue...\n")
        newPassword = input("Please enter your password and press enter to continue...\n")
    
        res = authenticator.loginUser(newEmail, newPassword)
        
        if (res["status"] == "success"):
            currentUser = user.User(newEmail, newPassword)
            print("Log in Successful \n")
            loggedIn(currentUser)
        else:
            print("\n Login failed. Please try again or create a new account \n")
            landingPage()
            
       
def loggedIn(currentUser):
    authenticatedInput = input("Welcome back. Select an option to continue \n 1: List saved passwords \n 2: Generate a new account credentials \n 3: Add an existing account credentials. \n 4: Genereate a secure password \n 5: Logout\n Press enter to continue...\n")


    if authenticatedInput != '1' and authenticatedInput != '2' and authenticatedInput != '3' and authenticatedInput != '4'  and authenticatedInput != '5':
        print('Please enter a valid input. \n')
        loggedIn(currentUser)


    if authenticatedInput == "1":
        verifiedEmail = currentUser.getUserEmail()
        res = credentialsManager.loadPasswords(verifiedEmail)
        
        if res["status"] == "success":
            items = res["data"]
            
            for item in items:
                print("Platform: {} \n\tUsername: {} \n\tPassword: {}".format(item["id"], item["username"], item["password"])) 
        
        loggedIn(currentUser)
        
    if authenticatedInput == "2":

        name = input("Please enter a name for the new entry and press to continue... \n")

        username = input("Please enter the account username or email and press enter to continue... \n")

        passwordLength = int(input("Please enter the length of your new password (min: 8) and press enter to continue... \n"))
        
        verifiedEmail = currentUser.getUserEmail()

        res = credentialsManager.createNewCredentialItem(name, username, passwordLength, verifiedEmail)
        
        if (res["status"] == "success"):
            print("The new item has been saved and generated a password for you: {}.\n \n".format(res["data"]))
            loggedIn(currentUser)
            
        else:
            print("There was a problem saving the entry. Please try again \n \n")
            loggedIn(currentUser)

    elif authenticatedInput == "3":
        name = input("Please enter a name for the new entry and press to continue... \n")

        username = input("Please enter the account username or email and press enter to continue... \n")

        password = input("Please enter the account password and press enter to continue... \n")
        
        verifiedEmail = currentUser.getUserEmail()
        
        res = credentialsManager.addExistingCredentialItem(name, username, password, verifiedEmail)
        
        if (res["status"] == "success"):
            print("The new item has been saved and generated a password for you: {}.\n \n".format(res["data"]))
            loggedIn(currentUser)
            
        else:
            print("There was a problem saving the entry. Please try again \n \n")
            loggedIn(currentUser)
            
    elif authenticatedInput == "4":
       try:
            quickPasswordLength = int(input("Please enter the length of your new password (min: 8) and press enter to continue... \n"))
            print("Your generated password is: {}".format(credentialsManager.generateVerifiedPassword(quickPasswordLength)))
            loggedIn(currentUser)
            
       except Exception as e :
           print('There was a fatal error: {}'.format(e))

    elif authenticatedInput == "5":
        print("You have successfully logged out.\n\n")
        landingPage()
            
landingPage()