import re


pattern = r"mul\(\d+,\d+\)"
result = 0
with open('./data/inputs.txt') as fichier:
  
    occurence = []
    for ligne in fichier:
        occurence.extend(re.findall(pattern,ligne))

for item in occurence:
    tab = re.findall(r'-?\d+\.?\d*',item)
    result += int(tab[0])*int(tab[1])
    

print(result)
