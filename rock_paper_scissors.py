# Rock, Paper, Scissors Game:
#Rock beats Scissors
#Scissors beats Paper
#Paper beats Rock

import random
while True: 
  print('\n')
  print('1. rock')
  print('2. scissors')
  print('3. paper')
  selection = int(input('Enter Throw: '))
  
  if (selection ==1):
    player_throw = 'rock'
  elif (selection == 2):
    player_throw = 'scissors'
  else:
    player_throw = 'paper'
    
  print('\n')
  print('Player throws', player_throw)
  
  throws = ['rock', 'paper','scissors']
  ai_throw = random.choice(throws)
  
  print('AI throws', ai_throw)
  
  if (player_throw == ai_throw):
    print('Its a Tie!')
  elif (player_throw == "rock"):
    if (ai_throw == 'paper'):
      print('Ai Wins!')
    elif (ai_throw == 'scissors'):
      print('Player Wins!') 
  elif (player_throw == 'paper'):
    if (ai_throw == 'scissors'):
      print('Ai Wins!')
    elif (ai_throw == 'rock'):
      print('Player Wins!')
  elif (player_throw == 'scissors'):
    if (ai_throw == 'rock'):
      print('Ai Wins!')
    elif (ai_throw == 'paper'):
      print('Player Wins!')
    