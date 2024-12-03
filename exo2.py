import re

pattern = r"mul\(\d+,\d+\)"

pattern_dont = r"don't\(\)"
pattern_do = r"do\(\)"
result = 0

with open('./data/inputs.txt') as fichier:
    occurence = []
    donts_do = []
    
    contenu = fichier.read()
    
    for item in re.finditer(pattern_dont,contenu):
        donts_do.append({'type':'dont','pos':item.start()})
    for item in re.finditer(pattern_do,contenu):
        donts_do.append({'type':'do','pos':item.start()})

donts_do = sorted(donts_do,key=lambda x: x["pos"])
donts_do.append({'type': 'do', 'pos': len(contenu)})

precedent = 'do'  # Par défaut, les `mul()` sont activés
startIndex = 0
    
    # Parcourir les instructions
for current in donts_do:
    endIndex = current['pos']
    
    if precedent == 'do':  # Si les `mul()` sont activés
        # Extraire les `mul()` dans le bloc actif
        occurences = re.findall(pattern, contenu[startIndex:endIndex])
        for item in occurences:
            # Extraire les nombres de chaque `mul()`
            numbers = re.findall(r'\d+', item)
            result += int(numbers[0]) * int(numbers[1])
    
    # Mettre à jour le précédent état et la position de départ
    precedent = current['type']
    startIndex = endIndex

# Afficher le résultat
print(result)