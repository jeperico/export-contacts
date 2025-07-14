import json
import csv

with open('test.json', 'r', encoding='utf-8') as file:
  json_data = json.load(file)

with open('contact-list.csv', 'w', newline='', encoding='utf-8') as file:
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
    print(data)
    row = [
      count,
      data["name"],
      '',
      'identifier',
      data["number"],
      ''
    ]
    writter.writerow(row)
    count += 1

print(data)
