class Restaurant:
  """This class stores attributes : restaurant name and the cuisine type"""
  
  def __init__(self,restaurant_name,cuisine_type):
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
  
 
  def describe_restaurant(self):
    """Describes the restaurant"""
    print(f"Welcome to {self.restaurant_name.title()} where we cook the finest {self.cuisine_type.title()} food in town!")
    

  
  def open_restaurant(self):
    print(f"{self.restaurant_name.title()} is now open!")
    
    
restaurant = Restaurant('rojas','mexican')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_two = Restaurant('peking', 'beijing')
restaurant_two.describe_restaurant()
restaurant_two.open_restaurant()

restaurant_three = Restaurant('la meizi', 'sichuan')
restaurant_three.describe_restaurant()
restaurant_three.open_restaurant()
         