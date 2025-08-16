import os
import json


initialize_data = {
    "expenses": [
        {
            "date": "",
            "amount": -1,
            "category": "",
            "description": ""
        }
    ]
}


def initialize_file():
    if not os.path.exists('expenses.json'):
        with open('expenses.json', 'w') as file:
            json.dump(initialize_data,file, indent=4)


def add_expense(date, amount, category, description):
    with open('expenses.json', 'r') as file: # open to append 'a'
        data = json.load(file) # load the existing data
    new_expense = {
        "date": date,
        "amount": amount,
        "category": category,
        "description": description
    }
    data['expenses'].append(new_expense)
    with open('expenses.json', 'w') as file:
        json.dump(data, file, indent=4)

initialize_file()
add_expense("12/03/2025", 200, "leisure", "")
