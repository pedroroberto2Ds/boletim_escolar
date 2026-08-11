QTD_NOTAS = int(input("Digite a quantidade de notas: "))
notas = []

for i in range (QTD_NOTAS):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

total_notas=0
for notas in notas:
        total_notas+=nota

media = total_notas / len(notas)

if media(nota > 0 and nota < 10):
    nota.append(nota)

    if media >=7:
        print ("Desempenho Satisfatorio")
else:
    print ("Desempenho Insatisfatorio")