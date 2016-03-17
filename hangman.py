import os
import random
import sys

def decider(words):
	return random.choice(words)
	

def printit(guess, theword, r, chance):
	b=[]
	for g in range(len(theword)):
		b.append('_')
	
	for x in guess:
		for y in range(len(theword)):
				if(theword[y] == x):
					b[y]=x
				 
	print('\n')
	if r == True:
		print('Good going, you hit it')
		print('You have {} chances left'.format(chance))
	else:
		print('Bam, you lost a chance')
		chance-=1
		print('You have {} chances left'.format(chance))

	print(' '.join(b))
	print('\n')
	return chance	
	
		
	
	


def checkit(theword, a):
	for x in range(len(theword)):
		if theword[x] == a:
			return True
	return False	
	

words = ['petrified', 'classic', 'penthouse', 'flamingo','ardent','glorious','niche','love','claustrophia','gene','cliche']
u =0
while u == 0:
	
	theword = decider(words)
	length = len(theword)
	print('Hola, try to guess this {} letter word'.format(length))
	print('You have a total of 10 chances')
	print("_ "*length)
	
	guess = []
	chance = 10
	j=0
	while j == 0:
		
		a = raw_input(">>")	
		
		r = checkit(theword, a)
		if r == True:
			guess.append(a)
		
		chance = printit(guess, theword, r, chance)
		
		if chance == 0:
			print("You are done. Game over")
			print('The word was ',theword)
			j == 1
	
	
		if len(guess) == length:
			print("Yohoo! You won it")
			
		if len(guess) == length or chance ==0:
			q = raw_input("Wanna play again? y/n \n")
			if q == 'y':
						break
			else:
						u = 1
