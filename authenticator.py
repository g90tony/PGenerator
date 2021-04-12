from os import path

def loginUser(self):
    newResponse = dict()
    try:
        with open("user_authentication.txt", "r+") as authDB:
            requestCredentials = "{}#{}\n".format(email, password)
            for existingUser in authDB : 
               
                if(requestCredentials == existingUser):                   
                    newResponse["status"] = "success"
                    return newResponse
                
                else:
                    newResponse["status"] = "failed"
                    return newResponse
                
    except Exception as e:
        print(str(e))
        newResponse["status"] = "failed"
        return newResponse
    
    
    
def registerNewUser(email, password, password_2):
    newResponse = dict()
    
    if (password != None and  password_2 == password and  email != None):
        try:
            with open("user_authentication.txt", "a") as auth_DB:
                data = auth_DB.write("{}#{}\n".format(email, password))
                newResponse["status"] = "success"
                return newResponse
            
            
            if (path.exists("./user_files/{}.txt".format(email))):
                newResponse["status"] = "failed"
                raise Exception("Please use another email address. That one already exists")
            
                return newResponse
    
            else: 
                with open("./user_files/{}.txt".format(email), "w+") as newTable:
                    newResponse["status"] = "success"
                    return newResponse
        
        except Exception as e:
            print(str(e))
            newResponse["status"] = "failed"
            return newResponse