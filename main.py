# This program is created to test the functionality of the objects, objects can  use the attributes inside the class as well as the methods inside them.


#creating classes
class User:
  
  #creating objects attributes 
  def  __init__(self, userid, username):
    self.id = userid
    self.uID = username
    self.follower = 0
    self.following = 0

  #creating objects methods
  def follow(self, user):
    self.following +=1
    user.follower +=1


#creating objects  

user_1 = User("001","aakash")
user_2 = User("002", "Smriti")


#Using objects with attributes
print(user_1.id)


#Using objects with methods

user_1.follow(user_2)
print(f"{user_1.uID} followers are {user_1.fo}")
