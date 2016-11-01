from tkinter import*
score=0
scorelabel="Your Chance, current Score : 0"

def add1():
    
    if score+1>21:
        global labelError
        labelError['text']="You cannot exeed 21,Sorry"
    else:
        labelError['text']=""
        global scorelabel
        global score
        score+=1
        if score==21:
            label2['text']=scorelabel+"\nScore : 21 , You LOST, RESET GAME"
            return 
        
        
        scorelabel+="\n(you added 1)\nComputer Chance, current Score : "+str(score)
        label2['text']=scorelabel
        if (score+1)%4==0:
            score+=1
            scorelabel+="\n(computer added 1)"
        elif (score+2)%4==0:
            score+=2
            scorelabel+="\n(computer added 2)"            
        elif (score+3)%4==0:
            score+=3
            scorelabel+="\n(computer added 3)"
            
        scorelabel+="\nYour Chance, current Score : "+str(score)
        label2['text']=scorelabel

def add2():
    if score+2>21:
        global labelError
        labelError['text']="You cannot exeed 21,Sorry"
    else:
        labelError['text']=""
        global scorelabel
        global score
        score+=2
        if score==21:
            label2['text']=scorelabel+"\nScore : 21 , You LOST, RESET GAME"
            return 
        
        
        scorelabel+="\n(you added 2)\nComputer Chance, current Score : "+str(score)
        label2['text']=scorelabel
        if (score+1)%4==0:
            score+=1
            scorelabel+="\n(computer added 1)"
        elif (score+2)%4==0:
            score+=2
            scorelabel+="\n(computer added 2)"            
        elif (score+3)%4==0:
            score+=3
            scorelabel+="\n(computer added 3)"
            
        scorelabel+="\nYour Chance, current Score : "+str(score)
        label2['text']=scorelabel

def add3():
    if score+3>21: 
        global labelError
        labelError['text']="You cannot exeed 21,Sorry"
    else:
        labelError['text']=""
        global scorelabel
        global score
        score+=3
        if score==21:
            label2['text']=scorelabel+"\nScore : 21 , You LOST, RESET GAME"
            return 
        
        
        scorelabel+="\n(you added 3)\nComputer Chance, current Score : "+str(score)
        label2['text']=scorelabel
        if (score+1)%4==0:
            score+=1
            scorelabel+="\n(computer added 1)"
        elif (score+2)%4==0:
            score+=2
            scorelabel+="\n(computer added 2)"            
        elif (score+3)%4==0:
            score+=3
            scorelabel+="\n(computer added 3)"
            
        scorelabel+="\nYour Chance, current Score : "+str(score)
        label2['text']=scorelabel

def reset():
    global score
    global scorelabel
    score=0
    scorelabel="Your Chance, Score : 0"
    label2['text']=scorelabel
    labelError['text']=""
    

wn=Tk()
wn.geometry("800x600")
wn.title("Game")

frame1=Frame(wn)
frame2=Frame(wn)
frame1.pack()
frame2.pack()

label1=Label(frame1, text="Welcome to the \nGame You Can Never Win", font="Calibre 30")
label1.grid(row=0, columnspan=2)
label2=Label(frame1,text=scorelabel,font="Calibre 10",fg="green")
label2.grid(row=1,columnspan=2)

labelError=Label(frame1,text="",fg="red")
labelError.grid(columnspan=2)

button1=Button(frame2, text="Add 1", width=15, height=1, command=add1)
button1.grid(row=5, column=0)

button2=Button(frame2, text="Add 2",  width=15, height=1, command=add2)
button2.grid(row=5, column=1)

button3=Button(frame2, text="Add 3",  width=15, height=1, command=add3)
button3.grid(row=5, column=2)

button4=Button(frame2, text="Reset",  width=15, height=1, command=reset)
button4.grid(row=5, column=3)

Label3=Label(frame2,text="""\nRules :
    \n1. You have to Make Sure that Computer Lands on Score 21 to win.
    \n2. You can increase the score by a Min of 1 and Max of 3, same applies for the computer
    \n3.You and computer will take chances one by one
    \n4.You start first
    \n5.The one has no option but to Land on score 21, looses the game.
    \n6. YOU WILL ALWAYS LOOSE. DONT BREAK YOUR COMPUTER""",fg="red")
Label3.grid(row=7,columnspan=4)

wn.mainloop()
