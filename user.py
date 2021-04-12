class User:
    def __init__(self, userEmail, userPassword):
        self.email = userEmail
        self.password = userPassword
        self.savedPasswords = list()
    
    newResponse = dict()          
                
    def setUserCredential(self, userEmail, userPassword):
        self.email = userEmail
        self.password = userPassword
        
    def loadSavedPasswords(selfpasswords):
        self.savedPasswords = passwords
        
    def getUserEmail(self):
        return self.email
    
    def getSavedPassword(self):
        return self.password