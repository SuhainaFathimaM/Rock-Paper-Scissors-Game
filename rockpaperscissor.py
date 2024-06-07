from tkinter import *
import random as rd

class RockPaperScissors:
    def __init__(self,master):
        self.master = master
        master.title("Rock Paper Scissors")

        self.choices = ["rock","paper","scissors"]
        self.userchoice = None
        self.computerchoice = None
        self.result = None
        self.userscore = 0
        self.computerscore = 0
        self.gamehistory = []

        self.title_label = Label(master,text="Rock Paper Scissors",font=("Arial",24))
        self.title_label.pack(pady=20)

        self.userchoice_label=Label(master,text="Your Choice:",font=("Arial",16))
        self.userchoice_label.pack()

        self.computerchoice_label=Label(master,text="Computer Choice:",font=("Arial",16))
        self.computerchoice_label.pack()

        self.result_label=Label(master,text="",font=("Arial",18))
        self.result_label.pack(pady=20)

        self.score_label=Label(master, text=f"Score: You: {self.userscore} | Computer: {self.computerscore}",font=("Arial",14))
        self.score_label.pack()

        self.rockbutton=Button(master, text="Rock", command=lambda:self.choose("rock"),width=10, height=2)
        self.rockbutton.pack(side="left",padx=10)

        self.paperbutton=Button(master, text="Paper", command=lambda:self.choose("paper"),width=10, height=2)
        self.paperbutton.pack(side="left",padx=10)

        self.scissorbutton=Button(master, text="Scissors", command=lambda:self.choose("scissors"),width=10, height=2)
        self.scissorbutton.pack(side="left",padx=10)

        self.resetbutton=Button(master, text="Play Again", command=self.reset,width=10,height=2,fg="red")
        self.resetbutton.pack(side="left",padx=10)

        self.historybutton=Button(master, text="View History", command=self.showhistory,width=10, height=2,fg="green")
        self.historybutton.pack(side="left",padx=10)

    def choose(self, choice):
        self.userchoice=choice
        self.computerchoice=rd.choice(self.choices)
        self.determinewinner()
        self.updatelabels()

    def determinewinner(self):
        if self.userchoice == self.computerchoice:
            self.result="It's a tie!"
        elif (
            (self.userchoice == "rock" and self.computerchoice == "scissors") or
            (self.userchoice == "paper" and self.computerchoice == "rock") or 
            (self.userchoice == "scissors" and self.computerchoice == "paper")
        ):
            self.result = "You Win!"
            self.userscore += 1
        else:
            self.result="Computer wins!"
            self.computerscore += 1
        self.gamehistory.append(
            f"Round: {len(self.gamehistory)+1}- You: {self.userchoice} | Computer: {self.computerchoice}"
        )

    def updatelabels(self):
        self.userchoice_label.config(text=f"Your choice: {self.userchoice}")
        self.computerchoice_label.config(text=f"Computer choice: {self.computerchoice}")
        self.result_label.config(text=self.result)
        self.score_label.config(text=f"Score: You: {self.userscore} | Computer: {self.computerscore}")

    def updatehistory(self):
        pass

    def showhistory(self):
        historywindow=Toplevel(self.master)
        historywindow.title("Game History")

        historytext=Text(historywindow,height=10,width=50,wrap=WORD, state=DISABLED)
        historytext.pack(pady=10)

        for roundresult in self.gamehistory:
            historytext.config(state=NORMAL)
            historytext.insert(END, roundresult+"\n")
            historytext.config(state=DISABLED)

    def reset(self):
        self.userchoice=None
        self.computerchoice=None
        self.result=None
        self.userscore=0
        self.computerscore=0
        self.gamehistory=[]
        self.updatelabels()

root=Tk()
root.geometry("500x400")
game=RockPaperScissors(root)
root.mainloop()


