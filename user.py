user_db = []
from datetime import datetime

class User:
    def __init__(self):
        self.db = user_db  
        
    
    def create_user(self,user_id,status="logged out",login_time,logout_time):
        payload = {
            "user_id": len(self.db)+1
            "statue=s":status,
            "login_time":login_time,
            "last_logout":logout_time
        }
        self.db.append(payload)
    
    def logout(self,user_id):
        user = self.get_user_by_id(user_id)
        if user:
            if user['status']=="logged_in":
                user['logout_time'] = datetime.utcnow()
                return "you are now logged out"
            return "please you are not logged in"
        return "user does not exist"
 

class Moderator(User):
	
	def __init__(self):
		pass

	def can_delete(self):
		return True


	def can_edit_own(self):
		return True

    
    
        

    



    


