import json 

with open('author1.json', 'r') as f: 
    data = json.load(f)

value = data['docs'][0]['top_subjects']

with open("author1_theme.json", "w") as json_file:
    json.dump(value, json_file, indent=4)


with open('author2.json', 'r') as f: 
    data = json.load(f)

value = data['docs'][0]['top_subjects']

with open("author2_theme.json", "w") as json_file:
    json.dump(value, json_file, indent=4)