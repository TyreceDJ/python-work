"""
Creating classes for your classmates
"""

# TODO: Section 1
# Define a class of "Dog". Ensure that all of the class instantiations of "Dog" have a
# property of "animal_type" set to "mammal". This dog should have some attributes set
# in it's init function including name, breed, and age. 

# TODO:
# Instantiate an instance of the "Dog" class named "Fido". Fido is a 3 year old Bulldog. You can
# store the instantiated class in a variable "fido". Then print the following statement using f
# shorthand: "Fido is a 3 year old Bulldog."

class Dog: 
    animal_type = "mammal"

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

fido = Dog("Fido", "Bulldog", 3)

print(f"{fido.name} is a {fido.age} years old {fido.breed}")


####################################################################################################

# TODO: Section 2
# Define a method, "country_info", for the below class of "Country". When called, the method should
# print the the following statement using f shorthand: "{country} is {age} years old with a
# population of {population} people." 

# HINT: Does the method need any parameters besides "self"?

# Instantiate the class defined below with the correct data types for each attribute. Make sure to
# assign the right type of data to the class instantiation based on it's name. Then call the method
# "country_info".

class Country:
  def __init__(self, name, age, population): # HINT: What data type should colors be?
    self.name = name
    self.age = age
    self.population = population
  def country_info(self, country, age, poplation):
      print(f"{country} is {age} years old with a population of {population} people.")

US = Country()

US.country_info("United States of America", 244, 330000000)
