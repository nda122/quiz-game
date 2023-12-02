import csv
from random import shuffle
fields = []
rows = []
score = 0
def load_questions(filename = "quiz_questions.csv"):
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        global fields, rows
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)



def ask_question(question):
    print(question[0])
    for i in range(4):
        print(question[i+1])
    ans = input("Enter you answer: ").strip()
    if ans == question[-1]:
        print('Correct!')
        global score
        score +=1
    else:
        print('Wrong answer :(')



def run_quiz():
    shuffle(rows)
    for i in rows:
        ask_question(i)


if __name__ == "__main__":
    load_questions()
    run_quiz()
    print("Your score:", score)
    score = 0


    