from gtts import gTTS
from playsound import *
import random
n = random.randint(1, 99)
print(n)

chance = int(input("How many opportunities do you want to defeat me : "))
i = 1
while i <= chance:
    print("Chance no. :", i)
    guess = int(input("Enter an integer from 1 to 99: "))
    if guess < n:
        print("Guess is low So,You Lose this time: Try Again \U0001F62D")
        lose = gTTS("Guess is low So,You Lose this time: Please, Try Again")
        lose.save('lose.mp3')
        playsound('lose.mp3')
        print("Remaining Chance :",chance-i)


    elif guess > n:
        print("guess is high So, You Lose : Try Again \U0001F62D")
        #print(u"\u0906\u092A\u0928\u0947 \u0905\u0927\u093F \u0905\u0928 ")
        loose = gTTS("Guess is high So,You Lose this time: Please, Try Again")
        loose.save('loose.mp3')
        playsound('loose.mp3')
        print("Remaining Chance :",chance-i)

    else:
        print("You WIN in", i, "chance")
        win = gTTS('Congratulations ! You WIN !!')
        win.save('mygame.mp3')
        playsound('mygame.mp3')
        #print("You WIN in",i,"chance")
        #print(u"\u092C\u0927\u093E\u0908 \u0939\u094A \u0906\u092A \u091C\u0940\u0924 \u0917\u090D \u0964 \U0001F600")

        break
    print()
    i = i+1
