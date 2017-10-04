import json
import csv

path = '/some/path'
f = open("test.txt", "r") #opens file with name of "test.txt"

print(f.read())
myJson = f.read()
json.loads(myJson)

emails = myJson['emails']
activities = myJson['activities']

#flatten 'user' in emails
for email in emails:
    if email['user'] != null:
        email['user_id'] = myJson['user']['id']
        email['user_first_name'] = myJson['user']['first_name']
        email['user_last_name'] = myJson['user']['last_name']
        email['user_name'] = myJson['user']['name']
        email['user_employee_id'] = myJson['user']['employee_id']
        email['user'] = ""

#flatten 'user' in activities
for activity in activities:
    if activity['user'] != null:
        activity['user_id'] = myJson['user']['id']
        activity['user_first_name'] = myJson['user']['first_name']
        activity['user_last_name'] = myJson['user']['last_name']
        activity['user_name'] = myJson['user']['name']
        activity['user_employee_id'] = myJson['user']['employee_id']
        activity['user'] = ""

myCSV = open(path, 'w')
csvwriter = csv.writer(myCSV)
count = 0

# create a set to check if keys exist alongside the columns array
# iterate over activities keys, if doesn't exist in set, add to set and add to columns
columns = [""] + emails.keys()
csvwriter.writerow(columns)

for email in emails:
      if count == 1:
          csvwriter.writerow(["email"] + email.values())
      else:
          csvwriter.writerow([""] + email.values())
      count += 1

count = 0

for activity in activities:
    if count == 1:
        csvwriter.writerow(["activities"] + activity.values())
    else:
        csvwriter.writerow([""] + activity.values())
    count += 1