from graphics import *


win = GraphWin("Your Pet", 500, 400)   # Window

def body_circle(color, win):
  cir_bod = Circle(Point(250, 200), 100)   # Circle shape for body
  cir_bod.setFill(color)   # Fill body with chosen color
  cir_bod.draw(win) 

def body_oval(color, win):   # Oval body with color
  oval_bod = Oval(Point(100, 100), Point(400, 300))
  oval_bod.setFill(color)
  oval_bod.draw(win)
  
def body_rectangle(color, win):   # Rectangle body with color
  rect_bod = Rectangle(Point(100,100), Point(400,300))
  rect_bod.setFill(color)
  rect_bod.draw(win)

def one_eye(win):   # Draw one eye
  eye = Oval(Point(225,145), Point(275,175))
  pupil = Circle(Point(250,160), 10)
  eye.setFill('white')
  pupil.setFill('black')
  eye.draw(win)
  pupil.draw(win)

def two_eyes(win):   # Draw two eyes
  # Draw left eye
  eye1 = Oval(Point(190,145), Point(240,175))
  pupil1 = Circle(Point(215,160), 10)
  eye1.setFill('white')
  pupil1.setFill('black')
  eye1.draw(win)
  pupil1.draw(win)
  # Draw right eye
  eye2 = Oval(Point(260,145), Point(310,175))
  pupil2 = Circle(Point(285,160), 10)
  eye2.setFill('white')
  pupil2.setFill('black')
  eye2.draw(win)
  pupil2.draw(win)

def three_eyes(win):   # Draw three eyes
  # Draw left eye
  eye1 = Oval(Point(190,160), Point(240,190))
  pupil1 = Circle(Point(215,175), 10)
  eye1.setFill('white')
  pupil1.setFill('black')
  eye1.draw(win)
  pupil1.draw(win)
  # Draw right eye
  eye2 = Oval(Point(260,160), Point(310,190))
  pupil2 = Circle(Point(285,175), 10)
  eye2.setFill('white')
  pupil2.setFill('black')
  eye2.draw(win)
  pupil2.draw(win)
  # Draw center eye
  eye3 = Oval(Point(225,120), Point(275,150))
  pupil3 = Circle(Point(250,135), 10)
  eye3.setFill('white')
  pupil3.setFill('black')
  eye3.draw(win)
  pupil3.draw(win)

def one_leg(win):   # Draw one leg
  # Draw center leg
  rect_leg = Rectangle(Point(250, 280), Point(260, 350))
  rect_leg.setFill('black')
  rect_leg.draw(win)
  # Draw foot
  rect_ft = Rectangle(Point(250, 350), Point(270, 360))
  rect_ft.setFill('black')
  rect_ft.draw(win)

def two_legs(win):   # Draw two legs
  # Draw right leg
  rect_leg1 = Rectangle(Point(265, 280), Point(275, 350))
  rect_leg1.setFill('black')
  rect_leg1.draw(win)
  # Draw right foot
  rect_ft1 = Rectangle(Point(265, 350), Point(285, 360))
  rect_ft1.setFill('black')
  rect_ft1.draw(win)
  # Draw left leg
  rect_leg2 = Rectangle(Point(225, 280), Point(235, 350))
  rect_leg2.setFill('black')
  rect_leg2.draw(win)
  # Draw left foot
  rect_ft2 = Rectangle(Point(235, 350), Point(215, 360))
  rect_ft2.setFill('black')
  rect_ft2.draw(win)

def three_legs(win):   # Draw three legs
  # Draw center leg
  rect_leg1 = Rectangle(Point(250, 280), Point(260, 350))
  rect_leg1.setFill('black')
  rect_leg1.draw(win)
  # Draw center foot
  rect_ft1 = Rectangle(Point(250, 350), Point(270, 360))
  rect_ft1.setFill('black')
  rect_ft1.draw(win)
  # Draw left leg
  rect_leg2 = Rectangle(Point(215, 280), Point(225, 350))
  rect_leg2.setFill('black')
  rect_leg2.draw(win)
  # Draw left foot
  rect_ft2 = Rectangle(Point(225, 350), Point(205, 360))
  rect_ft2.setFill('black')
  rect_ft2.draw(win)
  # Draw right leg 
  rect_leg3 = Rectangle(Point(285, 280), Point(295, 350))
  rect_leg3.setFill('black')
  rect_leg3.draw(win)
  # Draw right foot
  rect_ft3 = Rectangle(Point(285, 350), Point(305, 360))
  rect_ft3.setFill('black')
  rect_ft3.draw(win)