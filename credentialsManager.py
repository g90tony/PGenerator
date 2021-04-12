import fileManager
import passwordGeneratorEngine

    def generateVerifiedPassword(pass_length):
       return passwordGeneratorEngine.generateNewPassword(pass_length)
            
    # @staticmethod
    def loadPasswords(userEmail):
        try:
            with open("./user_files/{}.txt".format(userEmail)) as savedPassword:
                
        
        except Exception as e:
            print(str(e))
            newResponse["status"] = "failed"
      
      
  
    def createNewCredentialItem(newCredentialName, newCredentialUser, passwordLength, userEmail):
        try:
            generatedPassword = generateVerifiedPassword(passwordLength)
            with open("./user_files/{}.txt".format(email), "a") as authenticatedOperation :
                newEntry = "{}#{}#{}".format(newCredentialName, newCredentialUser, password)
                authenticatedOperation.write(newEntry)
                
                newResponse["status"] = "success"
                newResponse["data"] = entry
                return newResponse

        except Exception as e:
            print(str(e))
            newResponse["status"] = "failed"
            return newResponse  
        
    

    def addExistingCredentialItem(newCredentialName, newCredentialUser, newCredentialPassword, userEmail):     
        