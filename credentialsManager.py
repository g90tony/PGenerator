import fileManager
import passwordGeneratorEngine

class Credentials:
        
    def __init__(self, email, password):
            self.isAuthenticated = false
            self.email = email
            self.password = password
            self.savedPasswords = []
            
            
    def loadPasswords():
        res = fileEditor.getSavedPasswordItems() 
        if(res["status"] == "success"):
            self.savedPasswords = res.data
        print(res["message"])
        
    def createNewCredentialItem(newCredentialName, newCredentialUser, passwordLength):
        newPassword = passwordGenerator.generateNewPassword(passwordLength)
        res = fileEditor.addNewPasswordItem(credentialName, credentialUser, newPassword, self.isAuthenticated)
        print(res["message"])
        
    def addExistingCredentialItem(newCredentialName, newCredentialUser, newCredentialPassword):        
        res =  fileEditor.addNewPasswordItem(credentialName, credentialUser, credentialPassword, self.isAuthenticated)
        print(res["message"])