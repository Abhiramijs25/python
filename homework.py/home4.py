web_development = ["meera","aryan","veena"]

data_science    = ["rohit","rahul","farhana"]

UI_UX_design    = ["ganga","anujith","rakshith"]

all_participants = [web_development,data_science,UI_UX_design]
print(all_participants)

web_development.append("aravind")
print(web_development)

data_science.insert(1,"vidya")
print(data_science)

UI_UX_design.remove("rakshith")
print(UI_UX_design)

new_data_science = data_science.copy()
print(new_data_science)

data_science.clear()
print(data_science)

print(web_development[0:2])

name_lengths = [len(name) for name in new_data_science]
print(name_lengths)

if "asha" in web_development or "asha" in new_data_science or "asha" in UI_UX_design:

        print("Asha is in one of the workshops")
else:
    print("Asha is not in any workshop")

tuple_list = (web_development[0], new_data_science[0], UI_UX_design[0])
print(tuple_list)