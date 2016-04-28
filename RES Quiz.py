"""
RES quiz for use in college stem days.

Capabilities must be:
Display a question within a window that can change
Display multiple buttons with multiple choice answers
Display a score

"""
import tkinter as tk

Bcolour = "#ff6600"

class answers:
    def __init__(self, correct, ans, number):
        self.correct = correct
        self.ans = ans
        self.number = number

    def button(self):
        self.tkbutton = tk.Button(window, text=self.ans, bg='#ff7c00')
        self.tkbutton.grid(row=4, column=self.number, columnspan=1, pady=20, ipadx=Swidth/10, ipady=Sheight/12)
        


#code to find monitor resolutions
res = tk.Tk()
Sheight = res.winfo_screenheight()
Swidth = res.winfo_screenwidth()
res.destroy()
res.mainloop()

#create window for quiz
window = tk.Tk()
window.title("RES Quiz")
window.attributes('-topmost', True)
window.state("zoomed") #maximises window
window.configure(background=Bcolour) #orange background colour

#Insert logo in top middle of screen
pic = tk.PhotoImage(file="C:\\Users\\cameron\\Documents\\Python\\RES Quiz\\logo.gif")
logo = tk.Label(image=pic)
logo.grid(row=1, column=1, padx=Swidth/2-71, pady=Sheight/10-34)

question = tk.Label(window, text="QUESTION", bg='#ffb262')
question.grid(row=3, column=1, ipady=Sheight/6, ipadx=Swidth/2-60, padx=30)

score = tk.Label(window, text="Score: ", bg=Bcolour, font=("Arial", 18))
score.grid(row=2, column=1)

answer1 = answers(True, "ANSWER1", 1)
answer1.button()

answer2 = answers(True, "ANSWER2", 2)
answer2.button()
print(answer2.number)

answer3 = answers(True, "ANSWER3", 3)
answer3.button()

window.mainloop()


