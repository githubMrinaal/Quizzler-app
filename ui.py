THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window =  Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white",highlightthickness=0)
        self.question_text = self.canvas.create_text(150,125,text="Some question text",fill=THEME_COLOR,font=("Arial", 20, "italic"),width=280)
        self.canvas.grid(row=1,column=0,columnspan=2)
        
        self.score_label = Label(text="Score: 0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1,pady=10)

        correct_image = PhotoImage(file='d:/Python 100 days/quizler-app/images/true.png')
        self.correct = Button(image=correct_image,highlightthickness=0,command=self.correct_command)
        self.correct.grid(row=2,column=0,padx=10,pady=10)

        wrong_image = PhotoImage(file='d:/Python 100 days/quizler-app/images/false.png')
        self.wrong = Button(image=wrong_image,highlightthickness=0,command=self.wrong_command)
        self.wrong.grid(row=2,column=1,padx=10,pady=10)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the game")
            self.correct.config(state="disabled")
            self.wrong.config(state="disabled")
    def correct_command(self):
        true = "True"
        is_right = self.quiz.check_answer(true)
        self.give_feedback(is_right)

    def wrong_command(self):
        false = "False"
        is_right = self.quiz.check_answer(false)
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        
