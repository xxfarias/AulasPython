# Etapa 1
banda = []
print("Etapa 1: ", banda)
# Etapa 2
banda.append("John Lennon")
banda.append("Paul McCartney")
banda.append("George Harrison")
print("Etapa 2: ", banda)
# Etapa 3
for members in range(2):
    banda.append(input("Novo membro: "))
print("Etapa 3: ",banda)
# Etapa 4
del banda[-1]
del banda[-1]
print("Etapa 4: ", banda)
# Etapa 5
banda.insert(0, "RingoStarr")
print("Etapa 5:", banda)
print("The Beatles:",len(banda))