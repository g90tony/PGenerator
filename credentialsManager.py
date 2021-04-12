import fileManager
import passwordGeneratorEngine

class Credentials:
    def __init__(self, email):
            self.isAuthenticated = False
            self.email = email
            self.savedPasswords = []
            
    @staticmethod
    def generateVerifiedPassword(pass_length):
       return passwordGeneratorEngine.generateNewPassword(pass_length)
            
    # @staticmethod
    def loadPasswords(self):
        res = fileManager.getSavedPasswordItems(self.email, self.isAuthenticated) 
        if(res["status"] == "success"):
            self.savedPasswords = res.data
        print(res["message"])
      
      
    @staticmethod  
    def createNewCredentialItem(newCredentialName, newCredentialUser, passwordLength, email):
        
        newResponse = dict()
        
        newPassword = passwordGeneratorEngine.generateNewPassword(passwordLength)
        res = fileManager.addNewPasswordItem(newCredentialName, newCredentialUser, newPassword, email)
        
        if res["status"] == "success":
            newResponse["status"] = "success"
            newResponse["data"] = newPassword
            return newResponse
            
        else:
            newResponse["status"] = "failed"
            return newResponse
        
        print(res["message"])
        
    
    @staticmethod
    def addExistingCredentialItem(newCredentialName, newCredentialUser, newCredentialPassword, userEmail):     
        res =  fileManager.addNewPasswordItem(newCredentialName, newCredentialUser, newCredentialPassword, userEmail)
        print(res["message"])