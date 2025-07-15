import json
import csv
import uuid


with open('input.json', 'r', encoding='utf-8-sig') as file:
  json_data = json.load(file)

with open('contact-list.csv', 'w', newline='', encoding='utf-8-sig') as file:
  writter = csv.writer(file)
  
  writter.writerow([
    "id",
    "name",
    "email",
    "identifier",
    "phone_number",
    "ip_address"
  ])
  
  count = 1
  for data in json_data["records"]:
    print(data["name"])
    row = [
      count,
      data["name"],
      '',
      str(uuid.uuid4()),
      data["number"],
      ''
    ]
    writter.writerow(row)
    count += 1

