class Restaurant:
  """This class stores attributes : restaurant name and the cuisine type"""
  
  def __init__(self,restaurant_name,cuisine_type):
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    self.number_served =  3
  
 
  def describe_restaurant(self):
    """Describes the restaurant"""
    print(f"Welcome to {self.restaurant_name.title()} where we cook the finest {self.cuisine_type.title()} food in town!")
    

  
  def open_restaurant(self):
    print(f"{self.restaurant_name.title()} is now open!")
  
  #Added values to the attributes 
    
  def set_number_served(self):
    """Shows numbers served"""
    print(f"Served {self.number_served}")
    
  def increment_number_served(self, number_of_guest):
    """Add the given amount served in a restaurant"""
    self.number_served += number_of_guest
    
    
restaurant = Restaurant('rojas','mexican')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_two = Restaurant('peking', 'beijing')
restaurant_two.describe_restaurant()
restaurant_two.open_restaurant()

restaurant_three = Restaurant('la meizi', 'sichuan')
restaurant_three.describe_restaurant()
restaurant_three.open_restaurant()
restaurant_three.set_number_served()

restaurant_three.increment_number_served(2)
         