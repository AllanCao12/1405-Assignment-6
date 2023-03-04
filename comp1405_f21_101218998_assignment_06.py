#Allan Cao's Assignment 6 submission
#student number is 101218998 
#Submitted to Professor Collier on 2021-11-07

import pygame
import sys
import random

# initial random seeds.
random.seed()
# initialize the pygame module
pygame.init()
pygame.display.set_caption("comp1405_f21_101218998_assignment_06_by_Allan_Cao")
rows = 7
columns = 6
scale = 75
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
playerColour = [BLUE,RED]

def rollDice(): #function to roll the dice
	diceNum = random.randint(1, 6)
	return diceNum

font = pygame.font.SysFont("dejavuserif", 14, True)
board = pygame.Surface((columns * scale, rows * scale))
board.fill(WHITE)
#drawing the squares and printing the text for the numbers
for num in range(rows*columns):
		row = num // columns
		column = num % columns
		pygame.draw.rect(board, RED, (column*scale,(rows-1-row)*scale, scale,scale),1)
		text = font.render(str(1+num), False, BLACK)
		text_rect = text.get_rect(center = (column*scale+scale//2, (rows-1-row)*scale+scale//2)) #numbered tiles feature
		board.blit(text, text_rect)

player = [None,None]
player[0] = pygame.Surface((scale, scale)) #Making a surface for both players and representing them as circles
player[1] = pygame.Surface((scale, scale))
pygame.draw.circle(player[0],BLUE,(scale//3,scale//3),25)
pygame.draw.circle(player[1],RED,(scale*2//3,scale*2//3),25)
player[0].set_colorkey(BLACK)
player[1].set_colorkey(BLACK)
#setting up the screen 
screen = pygame.display.set_mode((board.get_width(), board.get_height()))
screen.fill(WHITE)
screen.blit(board, (0, 0))
screen.blit(player[0],(0,0))
screen.blit(player[1],(0,0))
pygame.display.flip()

playerColumn = [0,0]
playerRow = [rows-1,rows-1] #playerColumn and playerRow is the players' coordinates
whosTurn = 0 #While whosTurn = 0, it is player 1's turn, when it's equal to 1, it's player 2's turn

step = 0 #how many steps they are taking
winner = 0
while winner == 0:
	diceNum1 = rollDice()
	diceNum2 = rollDice()
	print("The two dice values are", diceNum1, "and", diceNum2)
	
	if(diceNum1 != diceNum2):
		step = diceNum1 + diceNum2
	else: #When they are the same
		step = 2*(diceNum1 + diceNum2) #Double move feature. When they roll a pair their move is doubled. 
	
	direction = 1 #if direction = 1, they move forward. if direction = -1, they move backwards
	for i in range(step):
		if direction == 1 and playerColumn[whosTurn] == columns-1: #if they are at the final column, they go to the beginning of the next row
			playerColumn[whosTurn] = 0
			playerRow[whosTurn] -= 1
		elif direction == -1 and playerColumn[whosTurn] == 0: #if they back up into the left-most column, they go back down
			playerColumn[whosTurn] = columns-1
			playerRow[whosTurn] += 1
		else:
			playerColumn[whosTurn] += direction #just move forward or backwards by 1
		
		if playerColumn[whosTurn] == columns-1 and playerRow[whosTurn] == 0:#if they will go past the end of the board they go backwards
			direction = -1
			#drawing everything
		screen.fill(WHITE)
		screen.blit(board, (0, 0))
		screen.blit(player[0],(playerColumn[0]*scale,playerRow[0]*scale))
		screen.blit(player[1],(playerColumn[1]*scale,playerRow[1]*scale))
		pygame.display.flip()
		pygame.time.delay(1000)
		
	if playerColumn[whosTurn] == 0: #If the player lands on a square in the 0 column, then they get an extra turn (extra turn specification)
		continue

	if playerColumn[whosTurn] == columns-1 and playerRow[whosTurn] == 0: #Checking if a player won the game
		winner = whosTurn + 1
		break
	
	otherPlayer = (whosTurn +1) % 2  #otherPlayer is the turn representation for the other player
	
	if playerColumn[whosTurn] == playerColumn[otherPlayer] and playerRow[whosTurn] == playerRow[otherPlayer]: #Sorry Collisions feature
		playerColumn[otherPlayer] = 0
		playerRow[otherPlayer] = 6
	
	if playerColumn[whosTurn] == 0: #If the player lands on a square in the 0 column, then they get an extra turn (extra turn specification)
		continue
		
	whosTurn = otherPlayer
print("Player",whosTurn+1, "is the winner!")	
input("press enter to stop")

