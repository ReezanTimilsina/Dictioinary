import json
from difflib import get_close_matches
print("\t-----JAYA JINENDRA-----\n")
data=json.load(open("dictionary.json"))

def translate(word):
    if word in data:
        return (data[word])
    elif len(get_close_matches(word,data.keys()))>0:
        print("Did you mean %s instead" % get_close_matches(word, data.keys())[0])
        decide = input("Press y for yes and n for no:\t")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]

        elif decide == "n":
            print("The word doesn't exist")
            print("congrats you have developed a new word")
            print("Waaaaaaaaauuuuuuuuuuu!!!!!!!!")
        else:
            print("Please press y or n. Not any other key idiot")
    else:
        print("The word doesn't exist")
        print("congrats you have developed a new word")
        print("Waaaaaaaaauuuuuuuuuuu!!!!!!!!")

z=True
while z==True:
    word = input("Enter word you want to search:\t ")
    output = translate(word.lower())
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
    print("\n")
    w=input('''want to search another word????\n Press y or n:\t''')
    if w=="y":
        z=True
    else:
        z=False


