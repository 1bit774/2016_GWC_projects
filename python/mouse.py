"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)

def random_color():
	return random_color(colors)




pygame.init()




# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Ball Game")


class Circle():
	def __init__(self, mouse_position):
		self.mouse_position = mouse_position
		self.x_pos = mouse_position[0]
		self.y_pos = mouse_position[1]
	def draw(self):
		global screen
		global BLACK
		pygame.draw.circle(screen, BLACK, self.mouse_position, 5)
	def move(self, x_speed,y_speed, x_pos, y_pos):
		#screen.fill(WHITE)
		self.x_speed= x_speed
		self.y_speed= y_speed
		self.x_pos+= x_speed
		self.y_pos+= y_speed
# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

circle_list=[]

# -------- Main Program Loop -----------
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True


	# --- Game logic should go here
	pressed = pygame.mouse.get_pressed()	
	if pressed[0]== 1:
		print ("Here!")
		screen.fill(WHITE)
		mouse_position= pygame.mouse.get_pos()
		circle = Circle(mouse_position)
		circle_list.append(circle)
		for circle in circle_list:
			circle.draw()
		circle.move(0,1)
		
	
		
	
		

	# Here, we clear the screen to white. Don't put other drawing commands
	# above this, or they will be erased with this command.

	# If you want a background image, replace this clear with blit'ing the
	# background image.
	

	# --- Drawing code should go here
	

	




	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
