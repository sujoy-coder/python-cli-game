import random
choices = ['stone', 'paper', 'scissor']

def random_selector():
	return random.choice(choices)

def player_choise():
	a = input('1. For Stone,   press ==> 1\n2. For Paper,   press ==> 2\n3. For Scissor, press ==> 3\nWhat do you select : ')
	while a not in ['1','2','3']:
		print('Invalid Choise !!!')
		return player_choise()
	return choices[int(a)-1]

def give_point(plr_ch, bot_ch):
	''' return 1 if player wins, return 0 if bot wins. also print the msg'''
	print(f'You Choosed : {plr_ch}\tComputer Choosed : {bot_ch}')
	if plr_ch=='stone' and bot_ch=='scissor':
		print('You Won...')
		return 1 
	if bot_ch=='stone' and plr_ch=='scissor':
		print('Computer Won...')
		return 0 
	if plr_ch=='paper' and bot_ch=='stone':
		print('You Won...')
		return 1 
	if bot_ch=='paper' and plr_ch=='stone':
		print('Computer Won...')
		return 0 
	if plr_ch=='scissor' and bot_ch=='paper':
		print('You Won...')
		return 1 
	if bot_ch=='scissor' and plr_ch=='paper':
		print('Computer Won...')
		return 0 
	print('Tied...')
	return None
	 
def main():
	print('### Welcome To Stone-Paper-Scissor Game ###')
	print('---------------------------------------------')
	n = int(input('How many Games you want to play : '))
	player_score = 0 
	bot_score = 0 
	confirm = input('Do you want to start (y/n) : ')
	if confirm in ['y', 'Y']:
		while n>0:
			plr_ch = player_choise()
			bot_ch = random_selector()
			point = give_point(plr_ch, bot_ch)
			# if player wins
			if point==1:
				player_score += 1
			# if bot wins
			if point==0:
				bot_score += 1
			print(f'Your Score : {player_score}\t\tComputer Score : {bot_score}')
			print('<---------------------------------------------------->')
			n -=1

		if player_score==bot_score:
			print('Match is Tied !!!')
		elif player_score>bot_score:
			print('Congratulations !!! You Won The Game ...')
		else:
			print('Opps !!! You Lost The Game ...')
		print(f'Your Final Score : {player_score}\t\tComputer Final Score : {bot_score}')
		print('Game Over !!! Thank You...')
		input('Press Enter. To Exit...')
	else:
		print('Game Ended...')
		input('Press Enter. To Exit...')


main()


