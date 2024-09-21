import random

words = ("apple","mang","gra","s")
 

#dictionary of keys
hangman = {0: (" ",
               " ",
               " ",),
           
           1 : ("o",
                " ",
                " ",),

           2 : ("o",
                "|",
                " ",),

           3 : (" o",
                "/|",),

           4 : ( "o",
                "/|\\",
                " ",),

           5 : ("  o",
                " /|\\",
                " /",),

           6 : ("  o",
                " /|\\",
                " /\\",),
           } 

                                     
def display_man(wrong_guess):        
    for wrong in hangman[wrong_guess]:
        print(wrong)
    
def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
        print(" ".join(answer))    
                                                                          




def main():
    answer = random.choice(words)
    hint = ["_" for _ in answer]  # Hint as a list of underscores
    wrong_guess = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guess)
        display_hint(hint)
        guess = input("enter your guess: ").lower()

        if len(guess) != 1 or not guess.isalpha():
             print("Invalid input")
             continue
        
        if guess in guessed_letters:
             print("You already guessed this letter")
             continue
        guessed_letters.add(guess)
        

        if guess in answer:
             for i in range(len(answer)):
                  if answer[i] == guess:
                       hint[i] = guess 
        else:
             wrong_guess += 1
        if "_" not in hint:
             display_man(wrong_guess)
             display_answer(answer)
             print("You won!")
             is_running = False
        elif wrong_guess >= len(hangman) - 1:
             display_man(wrong_guess)
             display_answer(answer)
             print("You lost!")
             is_running = False
        
main()