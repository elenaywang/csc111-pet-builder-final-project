# csc111-pet-builder-final-project

*Title of project:* Exotic Pet Builder   
*Contributor(s):* Elena Wang, Dayeon Kang, Joyce Lee, Brianna Mateo   
*Course:* CSC 111 Intro to Computer Science through Programming, Spring 2021   
*Instructors:* Alicia Grubb, Shinyoung Cho      
*Timeline:* April-May 2021

### *Overview:*    
This is the final project that I created with my group members for the CSC 111 Intro to Computer Science through Programming class at Smith College. Our goal was to learn how to use functions and graphics in Python. The project allows a user to design their own exotic pet. 

### *What this project does:*  
The user interface of the program  will ask the user if they would like to create an exotic pet using the functions.py, graphics.py, and main.py files.

For example:  
Do you want to create a pet?('Yes' or 'No'): Yes

If ‘Yes’, the user should input a string indicating which kind of characteristic they desire.  
For example:  
Is your pet blue, red, or green: red  
Is your pet a circle (C), rectangle (R), or oval (O): O  
Does your pet have 0, 1, 2, or 3 eyes: 3  

If the user does not input characteristics from the options indicated by the program, the program will ask the user the question again.

Depending on the color, a random generator will name your exotic pet from a pre-made list for each color.   
For example:
```
if color == ‘red’:  
  name = random.choice(red_names)
```

After a name is generated and your pet is drawn, the program will ask the user if they would like to create a new pet and remind them to screenshot their pet!  
If Yes, the user would go through the program again making more pets!   
If No, the program will output “Goodbye!”  

### *What we used:*
The code was written in Python and uses the graphics.py library. The exoticpet(example).png file is a screenshot of the graphics window created by running this program. The Design.pdf document was written collaboratively in Google Docs.  

### *Files:*
* main.py: contains the code that facilitates the user's flow through the program  
* Design.pdf: a document that explains the personas of expected users of our program; was required by the instructors for submission of project
* exoticpet(example).png: screenshot of an example pet created by our program and its corresponding user input
* functions.py: contains the functions used in our program
* graphics.py: contains the graphics.py library
* README.md: contains information about the project