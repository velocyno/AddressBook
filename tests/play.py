import json

file = open("../test_input_data/qa.json")

data = json.load(file)

print(data["session_email"])
print(data["dict_add_address"]["First name:"])

