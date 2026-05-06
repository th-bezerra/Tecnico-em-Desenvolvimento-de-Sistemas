# Primeira Forma
for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print()

#Segunda Forma
print("\n \n \n \n \n")
for i in range(1,6,-1):
    print("*"-i)