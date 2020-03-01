from django.contrib.auth import authenticate


class Authentication:

    def __init__(self,username,password):
        self.username=username
        self.password=password
        
    def user_credential_check(self):
        try:
            user = authenticate(username=self.username, password=self.password)
            
            if user is not None:
                return "valid user"
            else:
                return "invalid user"
        except:
            return "invalid user"