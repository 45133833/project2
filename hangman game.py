Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random

words=['car','bus','asmaa','blue','white','python']
letters=[]
word=words[random.randrange(len(words))]
print("Welcome in Hangman Game")


life=6
while life >0:
  guess=input('Enter a letter ')
  if word.__contains__(guess):
    print('Thats is correct. You guessed a letter')
    letters.append(guess)

    if letters.__len__()== word.__len__():
      print('congratulations!!! You guessed a word ',word)
      break

    else:
      letter=word.__len__()-letters.__len__()
      print('You have ',letter,'letters left')

  else:
    life -= 1
    print('00PS!!! You guessed wrong letter')
    if life==0:
      print('Game Over!!! the word is ',word)
        