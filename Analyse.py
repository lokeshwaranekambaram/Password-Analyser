import re
import getpass

class Analyser:
    def __init__(self):
        self.minlength=8
        self.score=0
        self.feedback=[]
    def Verifylength(self,password):
        if len(password)>=self.minlength:
            self.score+=1
            self.feedback.append("Password length is good")
        else:
            self.feedback.append("Password length is not good")
            
    def VerifyUppercase(self,password):
        if re.search(r'[A-Z]',password):
            self.score+=1
            self.feedback.append("Password contains uppercase letter")
        else:
            self.feedback.append("Password does not contain uppercase letter")
            
    def VerifyLowercase(self,password):
        if re.search(r'[a-z]',password):
            self.score+=1
            self.feedback.append("Password contains lowercase letter")
        else:
            self.feedback.append("Password does not contain lowercase letter")
            
    def VerifyDigit(self,password):
        if re.search(r'[0-9]',password):
            self.score+=1
            self.feedback.append("Password contains digit")
        else:
            self.feedback.append("Password does not contain digit")
        
    def VerifySpecialCharacter(self,password):
        if re.search(r'[^A-Za-z0-9]',password):
            self.score+=1
            self.feedback.append("Password contains special character")
            return True
        else:
            self.feedback.append("Password does not contain special character")
            return False
            
    def VerifyPassword(self,password):
        self.Verifylength(password)
        self.VerifyUppercase(password)
        self.VerifyLowercase(password)
        self.VerifyDigit(password)
        self.VerifySpecialCharacter(password)
        return self.feedback
    def GetScore(self):
        return self.score
    def GetFeedback(self):
        return self.feedback
s=input("Enter password: ")
a=Analyser()
print(a.VerifyPassword(s))
print(a.GetScore())         