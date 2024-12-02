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
tour = 0
while len(col1)>0 and len(col2)>0:
    result += abs(int(min(col1))  - int(min(col2)))
    print('diff',abs(int(min(col1))  - int(min(col2))))
    print('result',result)
    col1.remove(min(col1))
    col2.remove(min(col2))



print(result)