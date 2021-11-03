import csv

user_filename = 'user_report.csv'
expense_filename = 'expense_report.csv'

def get_users():
  users = []
  with open(user_filename) as csvfile:
      reader = csv.DictReader(csvfile,  delimiter = ",")
      for row in reader:
          users.append(row['Name'])
  return users

def get_involved_users(user):
  users = []
  with open(expense_filename) as csvfile:
    reader = csv.DictReader(csvfile,  delimiter = ",")
    for row in reader:
      if row['spender'] == user:
        users.append((row['people involved'], row['amount']))

  return users

def generate_choices():
  spenders = get_users()
  result = []
  for user in spenders:
    d = {'name': user}
    result.append(d)
  return result

def has_header(filename, fieldnames):
    with open(filename, 'r') as f:
        d_reader = csv.DictReader(f)

        #get fieldnames from DictReader object and store in list
        headers = d_reader.fieldnames
        if headers == None:
            return False

        if headers == fieldnames:
            return True
        else:
            return False