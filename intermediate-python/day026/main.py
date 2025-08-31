import pandas

dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

characters = {row.letter:row.code for (index,row) in dataframe.iterrows()}

go_on = True

while go_on:
    word = input("Input a word: ").upper()
    if word == "OFF":
        break
    result = [characters[char] for char in word if char in characters]
    print(result)
    