from os import path

newResponse = dict()

def addNewPasswordItem (name, user, password, email):
    try:
        with open("./user_files/{}.txt".format(email), "a") as authenticatedOperation :
            newEntry = "{}#{}#{}".format(name, user, password)
            authenticatedOperation.write(newEntry)
            
            newResponse["status"] = "success"
            newResponse["message"] = "Item added successfully"
            return newResponse

    except Exception as e:
        print(str(e))
        newResponse["status"] = "failed"
        newResponse["message"] = "fatalError"
        return newResponse
    



def getSavedPasswordItems(authenticatedEmail, isAuthenticated):
    if (isAuthenticated):
        try:
            with open("./user_files/{}.txt".format(authenticatedEmail)) as savedPassword:
                 newResponse["status"] = "success"
                 newResponse["message"] = "Password fetch successful"
                 return newResponse
        
        except Exception as e:
            print(str(e))
            newResponse["status"] = "failed"
            newResponse["message"] = "fatalError"
            print("An error occurred in getSavedPassword")
            return newResponse
        
    else: 
        newResponse["status"] = "failed"
        newResponse["message"] = "User not authenticated"
        return newResponse
    
    
def createNewUserFile(email, password):
    try:
        if (path.exists("./user_files/{}.txt".format(email))):
            newResponse["status"] = "failed"
            newResponse["message"] = "Please use another email address. That one already exists"
            return newResponse
    
        else: 
            with open("./user_files/{}.txt".format(email), "w+") as newTable:
                newResponse["status"] = "success"
                newResponse["message"] = "Account created successfully"
                return newResponse
           
    except Exception as e:
        print(str(e))
        newResponse["status"] = "failed"
        newResponse["message"] = "fatalError"
        return newResponse
    
  
def createNewUser(email, password):
    try:
        with open("user_authentication.txt", "a") as auth_DB:
            data = auth_DB.write("{}#{}\n".format(email, password))
            newResponse["status"] = "success"
            newResponse["message"] = "User added successfully"
            return newResponse
    
    except Exception as e:
        print(str(e))
        newResponse["status"] = "failed"
        newResponse["message"] = "fatalError"
        return newResponse
        

def authenticateUser(email, password):
    try:
        with open("user_authentication.txt", "r+") as authDB:
            requestCredentials = "{}#{}\n".format(email, password)
            for existingUser in authDB : 
               
                if(requestCredentials == existingUser):
                    isAuthenticated = True
                    savedCredentials = getSavedPasswordItems(email, isAuthenticated)
                   
                    newResponse["status"] = "success"
                    newResponse["message"] = "User logged in successfully"
                    newResponse["data"] = savedCredentials
                    return newResponse
                
                else:
                    newResponse["status"] = "failed"
                    newResponse["message"] = "Password missmatch"
                    return newResponse
                
    except Exception as e:
        print(str(e))
        newResponse["status"] = "failed"
        newResponse["message"] = "fatalError"
        return newResponse