from PyInquirer import prompt
from utils import has_header
import csv
import re

filename = 'user_report.csv'

user_questions = [
    {
        "type":"input",
        "name":"Name",
        "message":"New User - Name: ",
        "validate": lambda answer: 'Name must be a string' \
            if type(str(answer)) != str else True
    },
    {
        "type":"input",
        "name":"Age",
        "message":"New User - Age: ",
        "validate": lambda answer: 'Age must be a number' \
            if not re.search(r'^[-+]?[0-9]+$', answer) else True
    },
]

def add_user():
    infos = prompt(user_questions)
    fieldnames = ['Name', 'Age']

    try:
        with open(filename, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not has_header(filename, fieldnames):
                writer.writeheader()
            writer.writerow(infos)
    except IOError:
        print("I/O error")
        raise

    print("Expense Added !")
    return True