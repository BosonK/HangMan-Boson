import random
import turtle
import time

word_list = ["One", "Cat", "Dog", "Frog", "Pig"]

secret_word = random.choice(word_list).lower()

wrongLetters = []
correctLetters = []

topFont = 70
print(f"The secret word is {secret_word}")
screenWord = ""
wrongguesses = 0

turtle.colormode(255)
screen = turtle.getscreen()
screen.setup(1600,800)
screen.bgcolor("pink")

t = turtle.getturtle()
t.shape("turtle")
t.color(255,255,255)
t.width(5)
t.penup()
t.speed(0)

def drawGallows():
    t.forward(250)
    t.right(90)
    t.forward(300)
    t.left(90)
    t.pendown()
    t.forward(450)
    t.backward(225)
    t.left(90)
    t.forward(650)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(90)
    t.penup()
    t.forward(10)
    t.pendown()

def drawHead():
    t.right(90)
    t.circle(48)

def drawBody():
    t.left(90)
    t.penup()
    t.forward(96)
    t.pendown()
    t.forward(200)
    t.backward(160)

def drawLeftArm():
    t.right(60)
    t.forward(60)
    t.backward(60)
    t.left(60)

def drawLeftHand():
    t.right(60)
    t.forward(60)
    t.right(60)
    t.forward(20)
    t.backward(20)
    t.penup()
    t.right(60)
    t.forward(20)
    t.backward(20)
    t.right(60)
    t.forward(20)
    t.backward(20)
    t.right(60)
    t.forward(20)
    t.backward(20)
    t.pendown()
    t.right(60)
    t.forward(20)
    t.backward(20)
    t.right(60)
    t.forward(20)
    t.backward(20)
    t.backward(60)
    t.left(60)

def drawRightArm():
    t.left(60)
    t.forward(60)
    t.backward(60)
    t.right(60)

def drawRightHand():
    t.left(60)
    t.forward(60)
    t.left(60)
    t.forward(20)
    t.backward(20)
    t.penup()
    t.left(60)
    t.forward(20)
    t.backward(20)
    t.left(60)
    t.forward(20)
    t.backward(20)
    t.left(60)
    t.forward(20)
    t.backward(20)
    t.pendown()
    t.left(60)
    t.forward(20)
    t.backward(20)
    t.left(60)
    t.forward(20)
    t.backward(20)
    t.backward(60)
    t.right(60)

def drawLeftLeg():
    t.forward(160)
    t.right(30)
    t.forward(100)
    t.backward(100)
    t.left(30)

def drawLeftShoe():
    t.right(30)
    t.forward(100)
    t.right(80)
    t.circle(7, -90)
    t.circle(12, -90)
    t.circle(7, -90)
    t.circle(12, -90)
    t.left(80)
    t.backward(100)
    t.left(30)

def drawRightShoe():
    t.left(30)
    t.forward(100)
    t.right(90)
    t.circle(7, 90)
    t.circle(12, 90)
    t.circle(7, 90)
    t.circle(12, 90)
    t.left(90)
    t.backward(100)
    t.right(30)

def drawRightLeg():
    t.left(30)
    t.forward(100)
    t.backward(100)
    t.right(30)

def drawLeftEye():
    t.penup()
    t.backward(265)
    t.right(90)
    t.forward(20)
    t.pendown()
    t.circle(8)
    t.penup()
    t.backward(20)

def drawRightEye():
    t.penup()
    t.right(180)
    t.forward(20)
    t.right(180)
    t.pendown()
    t.circle(8)
    t.penup()
    t.forward(20)

def drawSmile():
    t.left(90)
    t.forward(45)
    t.right(90)
    t.pendown()
    myLoc = t.position()
    for i in range (5):
        t.forward(5)
        t.right(10)
    t.penup()
    t.goto(myLoc)
    t.pendown()
    t.setheading(0)
    for i in range (5):
        t.forward(5)
        t.left(10)

def updateDrawing():
    if wrongguesses == 0:
        drawGallows()
    if wrongguesses == 1:
        drawHead()
    if wrongguesses == 2:
        drawBody()
    if wrongguesses == 3:
        drawLeftArm()
    if wrongguesses == 4:
        drawLeftHand()
    if wrongguesses == 5:
        drawRightArm()
    if wrongguesses == 6:
        drawRightHand()
    if wrongguesses  == 7:
        drawLeftLeg()
    if wrongguesses == 8:
        drawLeftShoe()
    if wrongguesses == 9:
        drawRightLeg()
    if wrongguesses == 10:
        drawRightShoe()
    if wrongguesses == 11:
        drawLeftEye()
    if wrongguesses == 12:
        drawRightEye()

    if wrongguesses == 13:
        drawSmile()

def drawWords():
    global screenWord
    bottom_rightScreenTurtle.clear()

    bottom_rightScreenTurtle.penup()
    bottom_rightScreenTurtle.goto(-700, -300)
    bottom_rightScreenTurtle.setheading(0)
    screenWord = ""

    bottom_rightScreenTurtle.pendown()
    for letter in secret_word:
        if letter in correctLetters:
            screenWord += letter + " "
        else:
            screenWord += "_" + " "

    bottom_rightScreenTurtle.write(screenWord, align = "left", font=("Arial", 80, "normal"))
    bottom_rightScreenTurtle.hideturtle()



def getGuess():

    theGuess = screen.textinput("Type 'quit' to end this game", "Enter a letter or type '$$' to guess the word.")

    return theGuess

def printWin_Lose(win):

    if win:
        top_rightScreenTurtle.clear()
        top_rightScreenTurtle.write("You Win!!!", align="left", font=("Arial", topFont, "normal"))
        time.sleep(1.5)
        top_rightScreenTurtle.hideturtle()
        top_rightScreenTurtle.clear()
    else:
        top_rightScreenTurtle.clear()
        top_rightScreenTurtle.write("Loser!", align= "left", font= ("Arial", topFont, "normal"))
        time.sleep(1.5)
        top_rightScreenTurtle.hideturtle()
        top_rightScreenTurtle.clear()

def writeErroMessage(msg):
    top_rightScreenTurtle.clear()
    top_rightScreenTurtle.write(msg, align= "left", font=("Arial", 50,"normal"))
    top_rightScreenTurtle.hideturtle()
    time.sleep(1)
    top_rightScreenTurtle.hideturtle()
    top_rightScreenTurtle.clear()

def getWordGuess():
    top_rightScreenTurtle.clear()
    playerWordGuess = screen.textinput("Guess the Word", "Enter your guess of the word")
    if playerWordGuess.lower() == secret_word:

        printWin_Lose(True)
        return False
    else:
        printWin_Lose(False)
        return False

def drawWrongLetter():
    top_rightScreenTurtle.clear()
    letterString = "Wrong Letters: "
    for i in wrongLetters:
        letterString += i + " "
        top_rightScreenTurtle.write(letterString, align="left", font=("Arial", topFont, "normal"))

top_rightScreenTurtle = turtle.Turtle()
top_rightScreenTurtle.shape("turtle")
top_rightScreenTurtle.color(138,3,3)
top_rightScreenTurtle.width(5)
top_rightScreenTurtle.speed(0)
top_rightScreenTurtle.penup()
top_rightScreenTurtle.goto(-700,250)
top_rightScreenTurtle.setheading(0)


bottom_rightScreenTurtle = turtle.Turtle()
bottom_rightScreenTurtle.shape("turtle")
bottom_rightScreenTurtle.color(0,0,0)
bottom_rightScreenTurtle.width(5)
bottom_rightScreenTurtle.speed(0)
bottom_rightScreenTurtle.penup()
bottom_rightScreenTurtle.goto(-700,-300)
bottom_rightScreenTurtle.setheading(0)

gameon = True

updateDrawing()
drawWords()
while gameon:
    t.hideturtle()
    top_rightScreenTurtle.hideturtle()
    bottom_rightScreenTurtle.hideturtle()
    if wrongguesses < 13:
        if "_" not in screenWord:
            printWin_Lose(True)
            gameone = False
            break

        else:
            drawWords()
            guess = getGuess()
            if guess == "quit":
                top_rightScreenTurtle.clear()
                writeErroMessage("Thank you for playing the game...")
                gameon = False
            elif guess == '$$':
                gameon = getWordGuess()
            elif len(guess) != 1:
                writeErroMessage("Please enter a single character. Guess again")
            elif guess.lower() not in "abcdefghijklmnopqrstuvwxyz":
                writeErroMessage("Please enter a letter. Guess again")
            else:
                if guess.lower() in secret_word.lower():
                    correctLetters.append(guess.lower())
                    drawWords()
                else:
                    if guess.lower() not in wrongLetters:
                        wrongguesses += 1
                        wrongLetters.append(guess.lower())
                        updateDrawing()
                        drawWrongLetter()
                    else:
                        writeErroMessage("Please guess a different letter")
                        drawWrongLetter()
                        continue
    else:
        printWin_Lose(False)
        time.sleep(1)
        gameon = False




