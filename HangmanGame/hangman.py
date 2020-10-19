import random
import cv2
import time
from words import word_list

random.shuffle(word_list)
answer = list(word_list[0])
BLANK = "_"
# empty list called display
display = []
# adds the variable answer to display
display.extend(answer)

# iterates through the list display
for letter in range(len(display)):
    # replaces each index in the list with '_'
    display[letter] = BLANK
# the join command puts a space between each '_'
print(' '.join(display))


# counter stops the game once all letters have been guessed
count = 0

incorrect = 6

# keeps asking the user until all letters guessed
while count < len(answer) and incorrect > 0:
    img = cv2.imread('hangman' + str(6 - incorrect) + '.png')
    cv2.imshow('image', img)
    cv2.waitKey(1000)
    guess = input(" Type your letter: ")
    guess = guess.lower()
    print(count)


# iterates through the letters in answer
    for letter in range(len(answer)):
        # if the guessed letter matches a letter
        # in the answer
        if answer[letter] == guess:
            # replace the index of letter with
            # the actual letter they guessed
            display[letter] = guess
            count += 1
            # print out the new string with guessed letters in
            print(' '.join(display))
            print(f'You answered {count} correctly.')
    if guess not in display:
        incorrect -= 1
        print(f'Sorry, wrong guess. You have {incorrect} chances left.')

        if incorrect == 0:
            print('Sorry you lost. Goodbye.')
            img = cv2.imread('hangman6.png')
            cv2.imshow('image', img)
            cv2.waitKey(0)
            time.sleep(2)
            cv2.destroyAllWindows()
            exit()
    else:
        if count == len(answer):
            print("Well done, you guessed the word.")
            time.sleep(2)
            cv2.destroyAllWindows()
            exit()


















