from os import path

newResponse = dict()

def addNewPasswordItem (name, user, password, authenticatedEmail, isAuthenticated):
    if (isAuthenticated):
        try:
            with open("{}.txt".format(authenticatedEmail), "a") as authenticatedOperation :
                newEntry = "{}#{}#{}".format(name, user, password)
                authenticatedOperation.write()
               
                newResponse["status"] = "success"
                newResponse["message"] = "Item added successfully"
                return newResponse
    
        except Exception as e:
            print(str(e))
            newResponse["status"] = "failed"
            newResponse["message"] = "fatalError"
            print("An error occurred in addPasswordItem")
            return newResponse
    
    else:
            newResponse["status"] = "failed"
            newResponse["message"] = "User not authenticated"
            return newResponse


def getSavedPasswordItems(authenticatedEmail, isAuthenticated):
    if (isAuthenticated):
        try:
            with open("{}.txt".format(authenticatedEmail)) as savedPassword:
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