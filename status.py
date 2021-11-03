import csv
from utils import get_users, get_involved_users

user_filename = 'user_report.csv'


def list_users():
  users = get_users()
  involved = []
  for user in users:
    involved_users = get_involved_users(user)
    for e in involved_users:
      involved.append(e[0])
    for e in involved_users:
      if e == []:
        continue
      n = len(e[0])
      amount = e[1]
      i = int(amount)/n
      for u in involved:
        # print(u + 'owes' + str(amount/n) + 'to' + user)
        print("{} owes {} to {}.".format([i], i, user))

  return

list_users()