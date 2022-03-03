# ------------------------------------------------------
#  Names: Dayeon Kang, Joyce Lee, Elena Wang, Brianna Mateo
#  References: NA
# ------------------------------------------------------

from graphics import *
import functions
import random

# Creating a pet
keep_going = False
while keep_going != True:   # Make sure input is correct
  create_pet = input("Do you want to create a pet? ('Yes' or 'No'): ")   # Ask if user wants to play
  if create_pet.lower() == "yes":
    print("Great, let's get started!")
    keep_going = True
  elif create_pet.lower() == "no":
    keep_going = True
  else:
    print('That is not a valid input.')  # Program loops to ask question again
    keep_going = False

while create_pet.lower() != "no":
  win = GraphWin("Your pet", 500, 400)   # Window
  
  # Choosing the color
  keep_going = False
  while keep_going != True:   # Make sure input is correct
    color = input("Is your pet blue, red, or green: ")
    if (color == "blue") or (color == "red") or (color == "green"): 
      keep_going = True
    else:
      print("That is not a valid color.")
      keep_going = False   # Program loops to ask question again
  

  # Making the shape
  keep_going = False
  while keep_going != True: # Make sure it's a correct shape input
    shape = input("Is your pet a circle (C), rectangle (R), or oval (O): ")
    if shape.upper() == "C":
      functions.body_circle(color, win)
      keep_going = True
    elif shape.upper() == "R":
      functions.body_rectangle(color, win)
      keep_going = True
    elif shape.upper() == "O":
      functions.body_oval(color, win)
      keep_going = True
    else: 
      print("That is not a supported shape.")
      keep_going = False   # Program loops to ask question again


  # Making the eyes
  keep_going = False
  while keep_going != True:   # Make sure input is correct
    eyes = input("Does your pet have 0, 1, 2, or 3 eyes: ")
    if eyes == "0":
      None
      keep_going = True
    elif eyes == "1":
      functions.one_eye(win)
      keep_going = True
    elif eyes == "2":
      functions.two_eyes(win)
      keep_going = True
    elif eyes == "3":
      functions.three_eyes(win)
      keep_going = True
    else:
      print("That is not a supported number of eyes.")
      keep_going = False   # Program loops to ask question again


  # Making the legs
  keep_going = False
  while keep_going != True:   # Make sure input is correct
    legs = input("Does your pet have 0, 1, 2, or 3 legs: ")
    if legs == "0":
      None
      keep_going = True
    elif legs == "1":
      functions.one_leg(win)
      keep_going = True
    elif legs == "2":
      functions.two_legs(win)
      keep_going = True
    elif legs == "3":
      functions.three_legs(win)
      keep_going = True
    else:
      print("That is not a supported number of legs.")
      keep_going = False   # Program loops to ask question again
  
  print()
  
  # List of Names
  blue_names = ['Blue-Gummed Toothless', 'Alicia Grubb', 'Shinyoung Cho', 'Forgetful Dory', "Niagara Falls", "Bleu Cheese", "Smushed Blueberry", "Chip", "Toothpaste"]
  red_names = ['Alicia Grubb', 'Shinyoung Cho', 'Ramen' ,'Pig', "Sriracha", "Mapo Tofu", "Rose", "Justin Bieber", "Angry Bull", 'Fireflame', "Your First Love", "Kimchi"]
  green_names = ['Prickly Pear', 'Wasabi', 'Shinyoung Cho', 'Alicia Grubb', 'Moldy Meatlug', "Old Tree", "Bud", "Seaweed", "Mike Wazowski", "Chipotle", "Pea", "Green Onion"]
  
  
  # Assigning name
  # A name is randomly chosen from a list corresponding to the user-chosen color
  if color.lower() == "red":
    name = random.choice(red_names)
    print("Your pet's name is:", name)
  elif color.lower() == "green":
    name = random.choice(green_names)
    print("Your pet's name is:", name)
  elif color.lower() == "blue":
    name = random.choice(blue_names)
    print("Your pet's name is:", name)
    
  print()
  
  keep_going = False
  while keep_going != True:   # Make sure input is correct
    create_pet = input("Another pet? *screenshot now or it will be deleted FOREVER* ('Yes' or 'No'): ")   # Asks if user wants to play again
    if create_pet.lower() == "yes":
      print("Here we go again!")
      keep_going = True
    elif create_pet.lower() == "no":
      keep_going = True
    else:
      print('That is not a valid input.')
      keep_going = False   # Program loops to ask question again
    print()
  
  win.close()   # Close window


print ("Goodbye!")
