'''
Grant Novota
CSCI 1300
Rec 111
'''
import pygame
import sys
from Ship import Ship
from random import randint

#Defining colors to be shown on the gameboard
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#Creating the ships that the game will be played with
Destroyer = Ship()
Carrier = Ship()
Cruiser = Ship()
Submarine = Ship()

#This finds a random number between 0-6 to choose which ship layout to play the game with
ship_pos = randint(0,5)

#Setting the names of each ship
Destroyer.setShipName("Destroyer")
Carrier.setShipName("Carrier")
Cruiser.setShipName("Cruiser")
Submarine.setShipName("Submarine")

#Setting the length of each ship
Destroyer.setSize(2)
Carrier.setSize(5)
Cruiser.setSize(3)
Submarine.setSize(3)



class GameBoard:
	def __init__(self, result = 0, turns = 0):
		self.resut = result
		self.grid = [] #Used for making the gameboard
		self.turns = turns
		for row in range(10): #Creating a list with 10 elements and each element contains another list of 10 elements, basically 2D array
			self.grid.append([])
			for column in range(10):
				self.grid[row].append(0)

	def getTurns(self): #Returns the amount of turns taken to main so that it can be used in the scoreboard
		return self.turns

	def analyzeResult(self, row, column, ship_pos): #Contains 6 different ship positions. Will use the group that corresponds to the random number that was generated
		if ship_pos == 0: #Random number that was generated at the beginning
			if (row == 5 and column == 5) or (row == 5 and column == 6): #If the coordinate selected is any of these, the ship has been hit
				Destroyer.recordHit()
				print "Hit!\n"
				return 2
			elif (row == 0 and column == 0) or (row == 1 and column == 0) or (row == 2 and column == 0) or (row == 3 and column ==0) or (row == 4 and column == 0):
				Carrier.recordHit()
				print "Hit!\n"
				return 2
			elif (row == 9 and column == 0) or (row == 9 and column == 1) or (row == 9 and column == 2):
				Cruiser.recordHit()
				print "Hit!\n"
				return 2
			elif (row == 3 and column == 3) or (row == 3 and column == 4) or (row == 3 and column == 5):
				Submarine.recordHit()
				print "Hit!\n"
				return 2
			else:
				print "Miss!\n"
				return 1

		elif ship_pos == 1:
			if (row == 0 and column == 0) or (row == 0 and column == 1):
				Destroyer.recordHit()
				print "Hit!\n"
				return 2
			elif (row == 1 and column == 0) or (row == 1 and column == 1) or (row == 1 and column == 2) or (row == 1 and column == 3) or (row == 1 and column == 4):
				Carrier.recordHit()
				print "Hit!\n"
				return 2
			elif (row == 9 and column == 0) or (row == 9 and column == 1) or (row == 9 and column == 2):
				Cruiser.recordHit()
				print "Hit!\n"
				return 2
			elif (row == 3 and column == 3) or (row == 3 and column == 4) or (row == 3 and column == 5):
				Submarine.recordHit()
				print "Hit!\n"
				return 2
			else:
				print "Miss!\n"
				return 1

		elif ship_pos == 2:
			if (row == 9 and column == 8) or (row == 9 and column == 9):
				Destroyer.recordHit()
				print "Hit!\n"
				return 2
			elif (row == 5 and column == 0) or (row == 5 and column == 1) or (row == 5 and column == 2) or (row == 5 and column == 3) or (row == 5 and column == 4):
				Carrier.recordHit()
				print "Hit!\n"
				return 2
			elif (row == 0 and column == 4) or (row == 0 and column == 5) or (row == 0 and column == 6):
				Cruiser.recordHit()
				print "Hit!\n"
				return 2
			elif (row == 0 and column == 0) or (row == 1 and column == 0) or (row == 2 and column == 0):
				Submarine.recordHit()
				print "Hit!\n"
				return 2
			else:
				print "Miss!\n"
				return 1

		elif ship_pos == 3:
			if (row == 7 and column == 8) or (row == 7 and column == 9):
				Destroyer.recordHit()
				print "Hit!\n"
				return 2
			elif (row == 0 and column == 9) or (row == 1 and column == 9) or (row == 2 and column == 9) or (row == 3 and column == 9) or (row == 4 and column == 9):
				Carrier.recordHit()
				print "Hit!\n"
				return 2
			elif (row == 0 and column == 4) or (row == 0 and column == 5) or (row == 0 and column == 6):
				Cruiser.recordHit()
				print "Hit!\n"
				return 2
			elif (row == 0 and column == 0) or (row == 1 and column == 0) or (row == 2 and column == 0):
				Submarine.recordHit()
				print "Hit!\n"
				return 2
			else:
				print "Miss!\n"
				return 1

		elif ship_pos == 4:
			if (row == 9 and column == 8) or (row == 9 and column == 9):
				Destroyer.recordHit()
				print "Hit!\n"
				return 2
			elif (row == 8 and column == 1) or (row == 8 and column == 2) or (row == 8 and column == 3) or (row == 8 and column == 4) or (row == 8 and column == 5):
				Carrier.recordHit()
				print "Hit!\n"
				return 2
			elif (row == 7 and column == 4) or (row == 7 and column == 5) or (row == 7 and column == 6):
				Cruiser.recordHit()
				print "Hit!\n"
				return 2
			elif (row == 6 and column == 0) or (row == 6 and column == 1) or (row == 6 and column == 2):
				Submarine.recordHit()
				print "Hit!\n"
				return 2
			else:
				print "Miss!\n"
				return 1

		elif ship_pos == 5:
			if (row == 0 and column == 8) or (row == 1 and column == 8):
				Destroyer.recordHit()
				print "Hit!\n"
				return 2
			elif (row == 0 and column == 9) or (row == 1 and column == 9) or (row == 2 and column == 9) or (row == 3 and column == 9) or (row == 4 and column == 9):
				Carrier.recordHit()
				print "Hit!\n"
				return 2
			elif (row == 0 and column == 6) or (row == 1 and column == 6) or (row == 2 and column == 6):
				Cruiser.recordHit()
				print "Hit!\n"
				return 2
			elif (row == 0 and column == 2) or (row == 1 and column == 2) or (row == 2 and column == 2):
				Submarine.recordHit()
				print "Hit!\n"
				return 2
			else:
				print "Miss!\n"
				return 1

	def printBoard(self):
		#This sets the WIDTH and HEIGHT of each grid location
		WIDTH = 20
		HEIGHT = 20
		 
		#This sets the margin between each cell
		MARGIN = 5
		 
		#Initialize pygame
		pygame.init()
		hit_sound = pygame.mixer.Sound("hit.wav")
		miss_sound = pygame.mixer.Sound("splash.wav")
		 
		#Set the HEIGHT and WIDTH of the screen
		WINDOW_SIZE = [255, 255]
		screen = pygame.display.set_mode(WINDOW_SIZE)
		 
		#Set title of screen
		pygame.display.set_caption("Battleship")
		 
		#Loop until the user clicks the close button.
		AllShipsSunk = False
		 
		#Used to manage how fast the screen updates
		clock = pygame.time.Clock()
		 
		# ***** Main program loop that loops until all of the ships have been sunk*****
		while not AllShipsSunk:
		    for event in pygame.event.get():  # User did something
		        if event.type == pygame.QUIT:  # If user clicked close
		            done = True  # Flag that we are done so we exit this loop
		        elif event.type == pygame.MOUSEBUTTONDOWN:
		        	self.turns += 1
		        	pos = pygame.mouse.get_pos() #gets the position from where the mouse was clicked
		        	column = pos[0] // (WIDTH + MARGIN) # Change the x/y screen coordinates to grid coordinates
		        	row = pos[1] // (HEIGHT + MARGIN)
		        	print "Grid coordinates: ", (row, column)
		        	self.grid[row][column] = self.analyzeResult(row, column, ship_pos) #Compares coordinates to coordinates of the ships. Returns either 1 or 2
		        	if self.grid[row][column] == 1:
		        		pygame.mixer.Sound.play(miss_sound)
		        	elif self.grid[row][column] == 2:
		        		pygame.mixer.Sound.play(hit_sound)
		        	print "Ships Sunk: " #Lets the user know which ships have been sunk
		        	if Destroyer.isSunk():
		        		print Destroyer.getShipName()
		        	if Carrier.isSunk():
		        		print Carrier.getShipName()
		        	if Cruiser.isSunk():
		        		print Cruiser.getShipName()
		        	if Submarine.isSunk():
		        		print Submarine.getShipName()
		        	if Destroyer.isSunk() == False and Carrier.isSunk() == False and Cruiser.isSunk() == False and Submarine.isSunk() == False:
		        		print "None"
		        	print "\n"
		        	if Destroyer.isSunk() == True and Carrier.isSunk() == True and Cruiser.isSunk() == True and Submarine.isSunk() == True: #The game has been won
		        		print "Congratulations, You have won the game!\n"
		        		print "It took you ", self.turns, " Turns to sink all ships\n"
		        		AllShipsSunk = True #Exits the loop
		    
		    #Drawing the display        
			screen.fill(BLACK)
			for row in range(10): #Fills all of the grid spaces with white
				for column in range(10):
					color = WHITE
					if self.grid[row][column] == 1: #Miss
						color = GREEN
					if self.grid[row][column] == 2: #Hit
						color = RED
					pygame.draw.rect(screen,
		                             color,
		                             [(MARGIN + WIDTH) * column + MARGIN,
		                              (MARGIN + HEIGHT) * row + MARGIN,
		                              WIDTH,
		                              HEIGHT])
		 
		    #Limit to 60 frames per second
			clock.tick(60)
		 
		    #Updates the screen with what has been drawn.
			pygame.display.flip()