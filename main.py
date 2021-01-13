import random
# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

#Function creation
def greeting_with_name(name,location):
  greet = ["Hello ", "How are you "]
  location_greet = ["What is it like in ", "Is the Temp hot in ", "I would love to visit your  "]
  # print outout of the function with input variables from the function call

  print(random.choice(greet) + name)
  print(random.choice(location_greet) + location)
  

greeting_with_name(name="Terrell", location="Texas")
  

