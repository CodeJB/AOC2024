import re


pattern = r"mul\(\d+,\d+\)"
pattern_dont = r"don't\(\)"
pattern_do = r"do\(\)"
result = 0

with open('./data/inputs.txt') as fichier:
    occurence = []
    for ligne in fichier:
        print("je passe là")
        print(return item. for item in re.findall(pattern_dont,ligne))
       

for item in occurence:
    tab = re.findall(r'-?\d+\.?\d*',item)
    result += int(tab[0])*int(tab[1])
    
