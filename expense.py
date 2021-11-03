from PyInquirer import prompt, Separator
from utils import get_users, generate_choices, has_header
import csv
import re

spenders = get_users()
filename = 'expense_report.csv'

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
        "validate": lambda answer: 'Amount must be a number' \
            if not re.search(r'^[-+]?[0-9]+$', answer) else True
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
        "validate": lambda answer: 'Label must be a string' \
            if type(str(answer)) != str else True
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": spenders,
    },
    {
        "type":"checkbox",
        "name":"people involved",
        "message":"New Expense - People involved: ",
        "choices": generate_choices(),
        "validate": lambda answer: 'You must choose at least one person.' \
            if len(answer) == 0 else True
    }

]

fieldnames = ['amount', 'label', 'spender', 'people involved']

def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
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


