class Credentials:
    def __init__(self):
        self.accountID = None
        self.accountUsername = None
        self.accountPassword = None
          
    def createNewCredential(self, id, username, password):
        self.accountID = id
        self.accountUsername = username
        self.accountPassword = password
            
    def loadCredential():
        credentialInstance = dict()
        
        credentialInstance["id"] = self.id
        credentialInstance["username"] = self.accountUsername
        credentialInstance["savedPassword"] = self.accountPassword
        
    def updatePassword(password):
        self.accountPassword = password