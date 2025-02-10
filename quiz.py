import sqlite3

def fetch_questions():
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions")
    questions = cursor.fetchall()
    conn.close()
    return questions

def start_quiz():
    questions = fetch_questions()
    score = 0

    for q in questions:
        print(f"\n{q[1]}")
        print(f"1. {q[2]}  2. {q[3]}  3. {q[4]}  4. {q[5]}")
        answer = input("Enter the correct option number: ")

        if q[int(answer) + 1] == q[6]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {q[6]}\n")

    print(f"Quiz Over! Your Score: {score}/{len(questions)}")

if __name__ == "__main__":
    start_quiz()
