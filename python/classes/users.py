class User:
  def __init__(self, first_name, last_name, city, country,):
   self.first_name = first_name
   self.last_name = last_name 
   self.city = city 
   self.country = country 

  
  def describe_user(self):
    print(f"This is {self.first_name.title()} {self.last_name}, he/she is from {self.city.title()}, {self.country.title()} ")
  
  def greet_user(self):
    print(f"Welcome {self.first_name.title()}!")
    
    
firstUser = User('bob', 'seagar', 'new york city','usa') 

firstUser.describe_user()
firstUser.greet_user()

secondUser = User('marylinn', 'mason', 'kansas city', 'usa') 

secondUser.describe_user()
secondUser.greet_user()

thirdUser = User('james', 'brown', 'augusta', 'usa') 

thirdUser.describe_user()
thirdUser.greet_user()
