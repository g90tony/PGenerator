import passwordGeneratorEngine


def generateVerifiedPassword(pass_length):
    return passwordGeneratorEngine.generateNewPassword(pass_length)
        

def loadPasswords(userEmail):
    newResponse = dict()
    try:
        with open("./user_files/{}.txt".format(userEmail)) as savedPassword:
            passwordArr = list()
            newResponse = dict()
            for password in savedPassword:
                passwordItem = dict()
                passowrdsAttributes = password.split(" ## ")
                
                passwordItem["id"] = passowrdsAttributes[0]
                passwordItem["username"] = passowrdsAttributes[1]
                passwordItem["password"] = passowrdsAttributes[2]
                
                passwordArr.append(passwordItem)
                
                
            newResponse["status"] = "success"
            newResponse["data"] = passwordArr
            return newResponse
            
    
    except Exception as e:
        print(str(e))
        newResponse["status"] = "failed"
        return newResponse


def createNewCredentialItem(newCredentialName, newCredentialUser, passwordLength, userEmail):
    newResponse = dict()
    try:
        generatedPassword = generateVerifiedPassword(passwordLength)
        with open("./user_files/{}.txt".format(userEmail), "a") as authenticatedOperation :
            newEntry = "{} ## {} ## {}".format(newCredentialName, newCredentialUser, generatedPassword)
            authenticatedOperation.write("{}\n".format(newEntry))
            responseText = "The credentials for {} have been successfully generated. \n username: {} \n password:{}".format(newCredentialName, newCredentialUser, generatedPassword )
            newResponse["status"] = "success"
            newResponse["data"] = responseText
            return newResponse

    except Exception as e:
        print(str(e))
        newResponse["status"] = "failed"
        return newResponse  
    



def addExistingCredentialItem(newCredentialName, newCredentialUser, newCredentialPassword, userEmail):   
    newResponse = dict()
    try:
        with open("./user_files/{}.txt".format(userEmail), "a") as authenticatedOperation :
            newEntry = "{} ## {} ## {}".format(newCredentialName, newCredentialUser, newCredentialPassword)
            authenticatedOperation.write("{}\n".format(newEntry))
            responseText = "The credentials for {} have been successfully generated. \n username: {} \n password: {}".format(newCredentialName.upper(), newCredentialUser, newCredentialPassword)
            newResponse["status"] = "success"
            newResponse["data"] = responseText
            return newResponse

    except Exception as e:
        print(str(e))
        newResponse["status"] = "failed"
        return newResponse  
    