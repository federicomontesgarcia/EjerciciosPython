data = ["Línea 1", "Línea 2", "Línea 3", "Línea 4", "Línea 5"]

# fic = open("text_1.txt", "w")
# 
# for line in data:
    # fic.write(line)
    # fic.write("\n")
    # 
# fic.close()

#----------------------------------

# fic = open("text_2.txt", "w")
# 
# for line in data:
    # print(line, file=fic)
    # 
# fic.close()

#---------------------------------

fic = open("text_3.txt", "w")
fic.writelines("%s\n" % s for s in data)
fic.close()