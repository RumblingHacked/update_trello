import globals

trello_ac_all = []

for card in globals.list_completed.list_cards():
    trello_ac_all.append(card.name)

for card in globals.list_area_codes.list_cards():
    if card.name in trello_ac_all:
        print(card.name + " Duplicate Area Codes List")
    else:
        trello_ac_all.append(card.name)

for card in globals.list_in_progress.list_cards():
    if card.name in trello_ac_all:
        print(card.name + " Duplicate In Progress List")
    else:
        trello_ac_all.append(card.name)

for area_code in globals.area_codes_all:
    if area_code not in trello_ac_all:
        globals.list_area_codes.add_card(name=area_code, desc='Python Script added missing Area Codes')

print(len(globals.list_area_codes.list_cards()))
print(len(globals.list_in_progress.list_cards()))
print(len(globals.list_completed.list_cards()))