import tkinter as tk
from tkinter import messagebox
import random

# Sample questions and answers
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Jupiter", "Mars", "Venus"],
        "answer": "Jupiter"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["Harper Lee", "J.K. Rowling", "Ernest Hemingway", "Mark Twain"],
        "answer": "Harper Lee"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Au", "Ag", "Gd", "Ga"],
        "answer": "Au"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"],
        "answer": "Leonardo da Vinci"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")

        self.score = 0
        self.questions = random.sample(quiz_data, len(quiz_data))
        self.question_index = 0

        self.question_label = tk.Label(root, text="", font=("Arial", 16))
        self.question_label.pack(pady=20)

        self.option_vars = [tk.StringVar(value="") for _ in range(4)]
        self.option_buttons = []
        for var in self.option_vars:
            button = tk.Radiobutton(root, text="", variable=var, value=var.get(), font=("Arial", 14))
            button.pack(anchor="w")
            self.option_buttons.append(button)

        self.next_button = tk.Button(root, text="Next", command=self.next_question, font=("Arial", 14))
        self.next_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        if self.question_index < len(self.questions):
            question_data = self.questions[self.question_index]
            self.question_label.config(text=question_data["question"])
            for i, option in enumerate(question_data["options"]):
                self.option_vars[i].set(option)
                self.option_buttons[i].config(text=option, value=option, variable=self.option_vars[i])
        else:
            self.end_quiz()

    def next_question(self):
        selected_answer = None
        for var in self.option_vars:
            if var.get():
                selected_answer = var.get()
                break

        correct_answer = self.questions[self.question_index]["answer"]
        if selected_answer == correct_answer:
            self.score += 1

        self.question_index += 1
        self.load_question()

    def end_quiz(self):
        messagebox.showinfo("Quiz Finished", f"Your score is {self.score} out of {len(self.questions)}.")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
