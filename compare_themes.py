import json

with open('author1_theme.json', 'r') as f: 
    jenny = json.load(f)

with open('author2_theme.json', 'r') as f: 
    fitz = json.load(f)

counter = 0

for theme in jenny:
    for subject in fitz:        
        if theme == subject:
            counter += 1
            print (theme)

percentage_matching = int((counter / len(jenny)) * 100)

print(f"Number of matching subjects:", counter)
print(f"Percentage of matching subjects: {percentage_matching}%")