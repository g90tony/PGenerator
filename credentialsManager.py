import fileEditor
import passwordGenerator

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