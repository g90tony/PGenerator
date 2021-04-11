import fileEditor

newResponse = dict()

def registerNewUser(email, password, password_2):
    if (password != None and  password_2 == password and  email != None):
       response = fileEditor.createNewUser(email, password)
       
       
    if (response["status"] == "success"):
        res = fileEditor.createNewUserFile(email, password)
    
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
            