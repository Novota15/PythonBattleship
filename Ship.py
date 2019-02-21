'''
Grant Novota
CSCI 1300
Rec 111
'''
class Ship:
	def __init__(self, name = "", shipsize = 0, hits = 0):
		self.name = name
		self.shipsize = shipsize
		self.hits = hits

	def setShipName(self, shipname): #Gives the ship a name
		self.name = shipname

	def getShipName(self):
		return self.name

	def setSize(self, sizeinput): #Sets the size of the ship
		self.shipsize = sizeinput

	def getSize(self):
		return self.shipsize

	def recordHit(self): #Records the amount of times the ship has been hit
		self.hits += 1

	def isSunk(self): #If the amount of hits that the ship has received is equal to its size, that ship is sunk
		if(self.hits == self.shipsize):
			return True
		elif(self.hits != self.shipsize):
			return False