# fic = open('text_1.txt', "r")
# lines = fic.readlines()
# 
# print(lines)
# 
# fic.close()

#----------------------------------

# fic = open('text_1.txt', "r")
# lines = list(fic)
# fic.close()

#----------------------------------

fic = open('text_1.txt', "r")
lines = []

for line in fic:
    lines.append(line)

fic.close()

#--------------------------------

lines1 = [s.rstrip('\n') for s in lines]
print(lines1)





