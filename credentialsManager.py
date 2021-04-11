import fileEditor
import passwordGenerator

class Credentials:
        
    def __init__(self, email, password):
            self.isAuthenticated = false
            self.email = email
            self.password = password
            self.savedPasswords = []