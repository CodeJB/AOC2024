fichier = open('./data/inputs.txt')

col1 = []
col2 = []
for ligne in fichier:
    col1.append(ligne.strip().split()[0])
    col2.append(ligne.strip().split()[1])


print(len(col2))
result = 0


print('col1', len(col1))
print('col2 ', len(col2))
occurence = 0
for item in col1:
    occurence += int(item)*int(col2.count(item))
    

print(occurence)



