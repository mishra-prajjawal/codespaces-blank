import nltk
from nltk.tokenize import word_tokenize

text = """A voivodeship ( Polish: województwo [vɔjɛˈvut͡stfɔ]; plural: województwa) is the highest-level administrative division of Poland, corresponding to a province in many other countries. The term has been in use since the 14th century and is commonly translated into English as "province".The Polish local government reforms adopted in 1998, which went into effect on 1 January 1999, created sixteen new voivodeships. These replaced the 49 former voivodeships that had existed from 1 July 1975, and bear a greater resemblance (in territory, but not in name) to the voivodeships that existed between 1950 and 1975."""
text.replace('"','`')
tokens = word_tokenize(text)
json = {}
json["params"] = []
json["data"] = {}
for i in range(len(tokens)):
    json["data"][tokens[i]] = i
    json["params"].append(tokens[i])
print(json)
print(len(json["params"]), " Total parameters")

user_input = input("Enter text: ")
def encoder(input):
    if input.split() ==1 :
        return json["data"][i]
    else:
        for i in input.split():
            if i in json["params"]:
                return json["data"][i]
        return "Not found"

print(encoder(user_input))