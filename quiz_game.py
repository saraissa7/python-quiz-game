import random

def ask_question(q):
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    answer = input("Your answer (A/B/C/D): ").strip().lower()
    return answer

print("🌟 Welcome to the Ultimate Quiz Challenge! 🌟")
print("Test your knowledge and choose the correct answer.\n")

playing = input("Do you want to play? (yes/no): ")

if playing.lower() != "yes":
    quit()

score = 0

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Paris", "B) Rome", "C) Berlin", "D) Madrid"],
        "answer": "a"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "b"
    },
    {
        "question": "How many continents are there?",
        "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
        "answer": "c"
    },
    {
        "question": "Which ocean is the largest?",
        "options": ["A) Atlantic", "B) Pacific", "C) Indian", "D) Arctic"],
        "answer": "b"
    },
    {
        "question": "Which animal is the fastest on land?",
        "options": ["A) Lion", "B) Tiger", "C) Cheetah", "D) Horse"],
        "answer": "c"
    },
    {
        "question": "What is the largest mammal?",
        "options": ["A) Elephant", "B) Blue Whale", "C) Shark", "D) Giraffe"],
        "answer": "b"
    },
    {
        "question": "What is the capital of Italy?",
        "options": ["A) Milan", "B) Rome", "C) Venice", "D) Naples"],
        "answer": "b"
    },
    {
        "question": "Which gas do humans breathe?",
        "options": ["A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide", "D) Helium"],
        "answer": "a"
    },
    {
        "question": "How many legs does a spider have?",
        "options": ["A) 6", "B) 8", "C) 10", "D) 12"],
        "answer": "b"
    },
    {
        "question": "What color do you get from red and white?",
        "options": ["A) Pink", "B) Purple", "C) Orange", "D) Brown"],
        "answer": "a"
    }
]

random.shuffle(questions)

for q in questions:
    answer = ask_question(q)
    if answer == q["answer"]:
        print("Correct! 🎉")
        score += 1
    else:
        print(f"Wrong! Correct answer was {q['answer'].upper()}.")

total = len(questions)
print("\nQuiz finished!")
print(f"You got {score} out of {total}")
print(f"Your score: {(score/total)*100:.2f}%")