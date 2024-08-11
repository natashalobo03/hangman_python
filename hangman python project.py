stages =['''
 +---+
 |   |
 0   |
/|\  |
/ \  |
     |
========
''','''
 +---+
 |   |
 0   |
/|\  |
/    |
     |
========
''','''
 +---+
 |   |
 0   |
/|\  |
     |
     |
========
''','''
 +---+
 |   |
 0   |
/|   |
     |
     |
========
''','''
+---+
 |   |
 0   |
 |   |
     |
     |
========
''','''
+---+
 |   |
 0   |
     |
     |
     |
========
''','''
+---+
 |   |
     |
     |
     |
     |
========
''']

#step 01:creating a word list
word_list=["dangal","kgf","bahubali","chichore","animal","dunki","drishyam"]
player_lives=6

#step 02:randomly choosing a word from the word_list and assigning it to a variable called choosen_word
import random
choosen_word = random.choice(word_list)
print(choosen_word)

#step 03:creating as many blanks as letters in choosen_word
word_length=len(choosen_word)
blanks= ""
for p in range(word_length):
  blanks +="_"
print(blanks)

gameOver =False
correct_alphabets=[]

#step 04:asking the user to guess a letter and assigning their answer to a variable called guess
while not gameOver:
  guess=input("Guess a letter:").lower()
  display =""
  
#step 05:check if the user input matches with the choosen_word
  for letter in choosen_word:
    if letter ==guess:
      display+=letter
      correct_alphabets.append(letter)
    elif letter in correct_alphabets:
      display+=letter
    else:
      display+="_"

  print(display)
  
#step 06:if the user input is not in the choosen_word then reduce the player's lives by 1
  if guess not in choosen_word:
    player_lives-=1
    if player_lives==0:
      gameOver=True
      print("You loose")
      
#step 07:if the user input is in the choosen_word then print the letter
  if "_" not in display:
    gameOver =True
    print("You won")
    
#step 08:print the hangman stages
  print(stages[player_lives])