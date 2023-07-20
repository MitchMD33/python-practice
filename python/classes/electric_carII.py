"""A set of classes that can be used to represent electric cars."""
from car import Car


class Battery:
  """"A simple attempt to model a battery for an electric car"""
   
  def __init__(self, battery_size=75):
   """Initialize the battery's attributes"""     
   self.battery_size = battery_size
  
  
class ElectricCar(Car):
  """Represent aspects of a car, specific to electric vehicles."""
  
  def __init__(self, make, model, year):
    """Initialize attributes of the parent class"""
    super().__init__(make, model, year)
    self.battery = Battery() 
  
  def describe_battery(self):
    print(f"This car ahs a {self.battery_size}-kwh battery.")
  
  def fill_gas_tank(self):
    print("This car doesn\'t need a gas tank!")