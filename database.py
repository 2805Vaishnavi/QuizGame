import sqlite3

# Connect to database
conn = sqlite3.connect("quiz.db")
cursor = conn.cursor()

# Create questions table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        option1 TEXT NOT NULL,
        option2 TEXT NOT NULL,
        option3 TEXT NOT NULL,
        option4 TEXT NOT NULL,
        answer TEXT NOT NULL
    )
''')

# Insert sample questions
cursor.execute('''
    INSERT INTO questions (question, option1, option2, option3, option4, answer)
    VALUES
    ("What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", "Paris"),
    ("Which programming language is this quiz written in?", "C", "Java", "Python", "Go", "Python")
''')

conn.commit()
conn.close()

