import sqlite3
import csv

simplified = set()
studied = set()

# Grab all individual characters from my flashcard db. It's the full DB, so it
# will have any individual characters stored there. Not just in my character
# study category
with sqlite3.connect('./data/pleco-flashcard-backup_191003.pqb') as db:
    c = db.cursor()
    for simp, trad in c.execute(
            "SELECT hw,althw FROM pleco_flash_cards WHERE LENGTH(hw)=1"):
        simplified.add(simp)

# Grab all the chars from the 3000 list I found online
with open('./data/3000-most-common.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        character = row[0]
        simplified.add(character)

# Grab all the chars that are currently in my character study list
with open('./data/chars_2019-10-03.txt') as f:
    for line in f:
        studied.add(line[0])

for character in simplified.difference(studied):
    print(character)

print('ALL: {}'.format(len(simplified)))
print('STUDIED: {}'.format(len(studied)))
print(len(simplified - studied))
