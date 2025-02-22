import random
import string
from words import words
from hangman_visual import lives_visual_dict

def get_valid_word(word):
    word = random.choice(words) #randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guseed


    lives = 7

    #getting user input
    while len(word_letters) > 0 and lives > 0 :
          #letters used
          print("You have", lives, " lives left and you have used these letters: "," ".join(used_letters))
   
          #what curent word is (ie W - R D)
          word_list = [letter if letter in used_letters else '-' for letter in word]
          print(lives_visual_dict[lives])
          print("Current word: "," ".join(word_list))


          user_letter = input("Guess a letter: ").upper()
          if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
              word_letters.remove(user_letter)
              print("")

            else:
                lives = lives - 1 #takes away a life if worng 

          elif user_letter in used_letters:
             print("\n You have already used that character. Please try again.")

    else:
        print("Invald character. Please try again.")
  
    #gets here when len(word_letters) == 00 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print("You died, sorry. The word was ",word)
    else:
        print("You guessed the word ",word,"!!")

if __name__ == '__main__':
  hangman()