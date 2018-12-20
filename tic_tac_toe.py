from mygraphics import *
import math,sys
'''TODO: 
- language processing
- build ai
'''

SIZE_OF_BOX = 250

class Field:
	def __init__(self,x,y,path):
		self.path = path
		self.img = Image(Point(x,y),path)
		self.lowerX = self.img.anchor.x-(SIZE_OF_BOX/2)
		self.lowerY = self.img.anchor.y-(SIZE_OF_BOX/2)
		self.upperX = self.lowerX + SIZE_OF_BOX
		self.upperY = self.lowerY + SIZE_OF_BOX


class Tic_Tac_Toe_Game:
	def __init__(self):
		self.initialize_game_field()
		self.player = 0
		self.result = -1
		backgroundImage = Image(Point(450,450),"field.gif")
		self.win = GraphWin("My Chess Game",backgroundImage.getHeight(),backgroundImage.getWidth())
		self.win.setBackground('black')
		backgroundImage.draw(self.win)
		self.print_field()
		while not(self.is_game_over()):
			location = self.win.getMouse()
			for row in range(0,len(self.field)):
				for col in range(0,len(self.field)):
					if(self.field[row][col].path == "" and location.getX() >= self.field[row][col].lowerX and location.getX() <= self.field[row][col].upperX 
						and location.getY() >= self.field[row][col].lowerY and location.getY() <= self.field[row][col].upperY):
						self.field[row][col].img.undraw()
						if(self.player == 0):
							self.field[row][col] = Field(self.field[row][col].img.anchor.x,self.field[row][col].img.anchor.y,"cross.gif")
						elif(self.player == 1):
							self.field[row][col] = Field(self.field[row][col].img.anchor.x,self.field[row][col].img.anchor.y,"circle.gif")
						self.field[row][col].img.draw(self.win)
			self.change_player()
			time.sleep(0.1)
		self.evaluate_result()
		time.sleep(2)
		self.win.close()
	def evaluate_result(self):
		if(self.result == -1):
			print("Draw.")
		elif(self.result == 0):
			print("Player 1 has won.")
		elif(self.result == 1):
			print("Player 2 has won.")
		else:
			sys.exit()

	def is_game_over(self):
		game_over = False
		draw = True
		for i in range(0,len(self.field)):
			for j in range(0,len(self.field)):
				if(self.field[i][j].path == ""):
					draw = False
		game_over = game_over or draw
		self.result = -1
		if((self.field[0][0].path == "cross.gif" and self.field[0][1].path == "cross.gif" and self.field[0][2].path == "cross.gif") or
			(self.field[1][0].path == "cross.gif" and self.field[1][1].path == "cross.gif" and self.field[1][2].path == "cross.gif") or
			(self.field[2][0].path == "cross.gif" and self.field[2][1].path == "cross.gif" and self.field[2][2].path == "cross.gif") or
			(self.field[0][0].path == "cross.gif" and self.field[1][0].path == "cross.gif" and self.field[2][0].path == "cross.gif") or
			(self.field[0][1].path == "cross.gif" and self.field[1][1].path == "cross.gif" and self.field[2][1].path == "cross.gif") or
			(self.field[0][2].path == "cross.gif" and self.field[1][2].path == "cross.gif" and self.field[2][2].path == "cross.gif") or
			(self.field[0][0].path == "cross.gif" and self.field[1][1].path == "cross.gif" and self.field[2][2].path == "cross.gif") or
			(self.field[2][0].path == "cross.gif" and self.field[1][1].path == "cross.gif" and self.field[0][2].path == "cross.gif")):
			game_over = True
			self.player = 0
			self.result = 0

		elif((self.field[0][0].path == "circle.gif" and self.field[0][1].path == "circle.gif" and self.field[0][2].path == "circle.gif") or
			(self.field[1][0].path == "circle.gif" and self.field[1][1].path == "circle.gif" and self.field[1][2].path == "circle.gif") or
			(self.field[2][0].path == "circle.gif" and self.field[2][1].path == "circle.gif" and self.field[2][2].path == "circle.gif") or
			(self.field[0][0].path == "circle.gif" and self.field[1][0].path == "circle.gif" and self.field[2][0].path == "circle.gif") or
			(self.field[0][1].path == "circle.gif" and self.field[1][1].path == "circle.gif" and self.field[2][1].path == "circle.gif") or
			(self.field[0][2].path == "circle.gif" and self.field[1][2].path == "circle.gif" and self.field[2][2].path == "circle.gif") or
			(self.field[0][0].path == "circle.gif" and self.field[1][1].path == "circle.gif" and self.field[2][2].path == "circle.gif") or
			(self.field[2][0].path == "circle.gif" and self.field[1][1].path == "circle.gif" and self.field[0][2].path == "circle.gif")):
			game_over = True
			self.player = 1
			self.result = 1

		return game_over

	def change_player(self):
		self.player = 1-self.player

	def legal_move(self,row,col,row2,col2):
		is_legal_move = True

		return is_legal_move			

	def print_field(self):
		for row in self.field:
			for elem in row:
				if(elem.path != ""):
					elem.img.draw(self.win)


	def initialize_game_field(self):
		self.field = []
		firstrow = [Field(150,150,""),Field(450,150,""),Field(750,150,"")]
		secondrow = [Field(150,450,""),Field(450,450,""),Field(750,450,"")]
		thirdrow = [Field(150,750,""),Field(450,750,""),Field(750,750,"")]
		self.field.append(firstrow)
		self.field.append(secondrow)
		self.field.append(thirdrow)


demo = Tic_Tac_Toe_Game()
