import random

# Sample questions and answers
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A) Earth", "B) Jupiter", "C) Mars", "D) Venus"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A) Harper Lee", "B) J.K. Rowling", "C) Ernest Hemingway", "D) Mark Twain"],
        "answer": "A"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["A) Au", "B) Ag", "C) Gd", "D) Ga"],
        "answer": "A"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["A) Vincent van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Michelangelo"],
        "answer": "C"
    }
]

def generate_quiz(quiz_data):
    score = 0
    questions = random.sample(quiz_data, len(quiz_data))  # Randomize the order of questions

    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for option in q["options"]:
            print(option)
        
        answer = input("Your answer (A, B, C, or D): ").strip().upper()
        
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")

    print(f"Quiz finished! Your score is {score} out of {len(questions)}.")

# Run the quiz
generate_quiz(quiz_data)
