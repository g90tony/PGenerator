import fileManager

class User:
    def __init__(self):
        self.email = None
        self.password = None
        self.savedPasswords = list()
    
    newResponse = dict()          
                
    def setUserCredential(email, password):
        self.email = email
        self.password = password
        
    def loadSavedPasswords(passwords):
        self.savedPasswords = passwords
        
    def getUserEmail:
        userData["email"] = self.email
        
    def getSavedPassword:
        userData["passwords"] = self.savedPasswords