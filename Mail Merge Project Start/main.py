with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()

f = open("./Input/Names/invited_names.txt", "r")
list = f.readlines()

for items in list:
    name = items.strip()
    x = letter.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_to_{name}.txt", mode='w') as card:
        card.write(x)


#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp