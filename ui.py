from quiz_brain import QuizBrain
from tkinter import *

THEME_COLOR = "#375362"


class UserInterface:

    def __init__(self, quizz_brain: QuizBrain):
        self.quiz = quizz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="question goes here",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=1, row=2, columnspan=2, padx=20, pady=20)

        right_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_img, command=self.right_button_pressed)
        self.right_button.grid(column=1, row=3)

        wrong_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_img, command=self.wrong_button_pressed)
        self.wrong_button.grid(column=2, row=3)

        self.score_label = Label(text="Score: 0 ", fg="white", bg=THEME_COLOR, font=("Arial", 20, "bold"))
        self.score_label.grid(column=2, row=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached end of the quiz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right_button_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong_button_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
