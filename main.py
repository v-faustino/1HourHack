import requests
from art import *
import random
import nltk
# Download the words corpus if you haven't already
nltk.download('words')
from nltk.corpus import words


def getRhymes(word):
    url = f"https://api.datamuse.com/words?rel_rhy={word}"
    response = requests.get(url)
    if response.status_code != 200:
        return []
    
    data = response.json()
    rhymes = [item['word'] for item in data]
    return rhymes

def getWordByLength(length):
    rhymes = 0
    while rhymes == 0:
        word_list = [word.lower() for word in words.words() if len(word) == length]
        word = random.choice(word_list)
        rhymes = len(getRhymes(word))

    return word

# Hard code some rhymes cuz api is being goofy
hardRhymes = {"angel": "hill"}
hardestRhymes = ["orange", "silver", "woman", "angel", "artist", "pneumonia", "biscuit"]

# Credit: https://gist.github.com/SethVandebrooke/14e98f5acf1f2e18bef52979ca5d4389
# Slightly altered

topHatMen = ["""
     _________________
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
 ___|             ____|___
|_________________________|
    |   --\     /--   |
    |   (-)     (-)   |
    \                 /
     |       ^^      |
     \    \______/   /
      \_____________/
""",
"""
     _________________
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
 ___|             ____|___
|_________________________|
    |    _       _    |
    |   (-)     (-)   |
    \                 /
     |       ^^      |
     \    \______/   /
      \_____________/
""",
"""
     _________________
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
 ___|             ____|___
|_________________________|
    |    _       _    |
    |   (-)     (-)   |
    \                 /
     |       ^^      |
     \    ________   /
      \_____________/
""",
"""
     _________________
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
 ___|             ____|___
|_________________________|
    |   --\     /--   |
    |   (-)     (-)   |
    \                 /
     |       ^^      |
     \    /------\   /
      \_____________/
""",
"""
     _________________
    |                 |
    |                 |
    |                 |
    |                 |
    |                 |
 ___|             ____|___
|_________________________|
    |   --\     /--   |
    |   (-)     (-)   |
    \                 /
     |       ^^      |
     \       OO      /
      \_____________/
"""]

tprint("RhymeMaster")
print("I am the Rhyme Master, the king of the flow. To best me in battle, your rhymes must all glow. \nMy words strike terror, my verses inspire. Cross me and tremble — I’m feared like fire.")
print("Let’s all begin without further ado. Show me your skills — prove what you can do.")

lengths = [5, 6, 7, 8]
correct = 0

for roundNum in range(5):
    print(topHatMen[roundNum])
    
    if roundNum == 4:
        word = random.choice(hardestRhymes)
    
        print("You’ve yet to best me, no victory yet. These words are the hardest, a true test, I bet.")
    else:
        word = getWordByLength(lengths[roundNum])

    answer = input(f"\nRound {roundNum+1} - What rhymes with {word}: ")
    if answer.lower() in getRhymes(word):
        print("Correct!")
        correct += 1
    else:
        print("Incorrect!")

    print(f"{correct}/5")

    
    

