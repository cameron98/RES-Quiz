"""
RES quiz for use in college stem days.

Capabilities must be:
Display a question within a window that can change
Display multiple buttons with multiple choice answers
Display a score

"""
import tkinter as tk
import random, time, threading, queue
from sys import exit

global quiz, correct, SCORE, question, display



class Quiz(threading.Thread):
        

    def show(self, question):
        self.question = quiz[question][0]
        self.correct = quiz[question][1]
        self.incorrectA = quiz[question][2]
        self.incorrectB = quiz[question][3]
        self.ref = quiz[question][4]
        questionDisplay.config(text=self.question)
        correctButton = "answer" + str(self.ref[0])
        eval(correctButton).config(text=self.correct, command=lambda : check(True))
        incorrect1 = "answer" + str(self.ref[1])
        eval(incorrect1).config(text=self.incorrectA, command= lambda : check(False))
        incorrect2 = "answer" + str(self.ref[2])
        eval(incorrect2).config(text=self.incorrectB, command= lambda : check(False))
        return self.correct

    def run(self):
        while True:
            
            if questionQueue.qsize() >= 1:
                time.sleep(1)
                display.show(questionQueue.get())

            else:
                pass
            
        

    

def check(button):
    global SCORE, question, display, Quiz, answer1
    if button == True:
        SCORE += 1
        score.config(text="Score: " + str(SCORE))
        questionDisplay.config(text="CORRECT!")
    else:
        questionDisplay.config(text="INCORRECT!")
    question += 1
    questionQueue.put(question)

def EXIT():
    window.destroy()
    exit()


BGcolour = "#ff6600" #Background colour
Bcolour = "#ff7c00" #Button colour
SCORE = 0 #Score variable
correct = "" #text for button
question=0 #Current question
questionQueue = queue.Queue()



#for questions list, 0 is question, 1 is correct answer, 2 and 3 are other options
question1 = ["The RES building was originally an egg farm... but in what year was it built?", "1930", "1890", "1945"]
question2 = ["How many chickens did the egg farm hold?", "50,000", "2,500", "25,000"]
question3 = ["How many visitors has RES had since 2004?", "Over 20,000", "3,000", "15,000"]
question4 = ["What does borehole cooling use to cool the RES building?", "Water", "Air", "Oil"]
question5 = ["What are the solar panels at RES used for?", "Electricity and Heating", "Electricity", "To get more sunlight in"]
question6 = ["How many meters squared are the solar panels at RES?", "170", "45", "250"]
question7 = ["How long does it take to earn back the cost of the solar panels?", "8 years", "2 years", "15 years"]
question8 = ["What is the best direction for solar panels to face?", "South", "East", "West"]
question9 = ["What is the scientific name for a solar panel?", "Photovoltaic Cell", "Solar Transformer", "Solar Farm"]
question10 = ["How tall is RES's wind turbine from the floor to the tip?", "50m", "30m", "120m"]
question11 = ["How many houses could the RES turbine power per year?", "30-40", "5-10", "60-70"]
question12 = ["Which is the fastest growing energy market?", "Wind", "Coal", "Solar"]
question13 = ["How tall is a typical turbine RES installs?", "125m", "35m", "70m"]
question14 = ["What proportion of the time does a wind turbine generate electricity?", "70 - 90%", "50%", "10 - 25%"]
question15 = ["How many cubic meters of water can the RES heat store hold?", "1400", "120", "2600"]
question16 = ["What is the name for organic material used as fuel?", "Biomass", "Wood", "Oil"]
question17 = ["What is the other name for 'miscanthus', the crop RES grows?", "Elephant Grass", "Hippo Weed", "Bamboo"]
question18 = ["How efficient at burning fuel is the biomass heater at RES?", "90%", "12%", "47%"]

n = 1
quiz = []
while n <= 18:  #adds a radomly generated list of numbers from 1-3 for buttons
    numbers = [1,2,3]
    ref = []
    ref.append(numbers.pop(random.randint(0,2)))
    ref.append(numbers.pop(random.randint(0,1)))
    ref.append(numbers.pop())
    eval("question" + str(n)).append(ref)
    quiz.append(eval("question" + str(n)))
    n+=1
        

#code to find monitor resolutions
res = tk.Tk()
Sheight = res.winfo_screenheight()
Swidth = res.winfo_screenwidth()
res.destroy()
res.mainloop()

#create window for quiz
window = tk.Tk()
window.title("RES Quiz")
window.attributes('-fullscreen', True)
window.state("zoomed") #maximises window
window.configure(background=BGcolour) #orange background colour

#Insert logo in top middle of screen
pic = tk.PhotoImage(file="C:\\Users\\cameron\\Documents\\Python\\RES Quiz\\logo.gif")
logo = tk.Label(image=pic)
logo.place(rely=0.03, relx=0.44)

questionDisplay = tk.Label(window, font=("Arial", 20), text="QUESTION", bg='#ffb262', height=9, width=76)
questionDisplay.place(relx=0.05, rely=0.25)


score = tk.Label(window, text="Score: " + str(SCORE), bg=BGcolour, font=("Arial", 18))
score.place(rely=0.18, relx=0.45)

answer1 = tk.Button(window, text="ANSWER1", bg=Bcolour, height=10, width=30, command= lambda : check("answer1"))
answer1.place(relx=0.05, rely=0.72)

answer2 = tk.Button(window, text="ANSWER2", bg=Bcolour, height=10, width=30, command= lambda : check("answer2"))
answer2.place(relx=0.421, rely=0.72)

answer3 = tk.Button(window, text="ANSWER3", bg=Bcolour, height=10, width=30, command= lambda : check("answer3"))
answer3.place(relx=0.785, rely=0.72)

close = tk.Button(window, text="Exit", bg=Bcolour, height = 3, width=10, command=EXIT)
close.place(relx=0.9, rely=0.05)



display = Quiz()
correct = display.show(question)
display.start()


        
        
window.mainloop()

