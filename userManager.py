import fileManager

newResponse = dict()

def registerNewUser(email, password, password_2):
    if (password != None and  password_2 == password and  email != None):
       response = fileManager.createNewUser(email, password)
       
       
    if (response["status"] == "success"):
        res = fileManager.createNewUserFile(email, password)
    
        if(res["status"] == "success"):
            newResponse["status"] = "success"
            return newResponse
    
        else:
            newResponse["status"] = "failed"
            return newResponse
    
    else:
      newResponse["status"] = "failed"
      return newResponse
    
    print(res["message"])
           
            
def loginUser(email, password):
    res = fileManager.authenticateUser(email, password)
    
    if(res["status"] == "success"):
        newResponse["status"] = "success"
        # newResponse[data] = res["data"]
        return newResponse
    else:
        newResponse["status"] = "failed"
        return newResponse
    
    print(res["message"])