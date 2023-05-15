ent = str(input('Digite uma letra:  ')).upper().strip()
nomes = "A" or "B" or "Z"
while ent != nomes:
    ent = str(input('Digite uma letra:  ')).upper().strip()
else:
    ihala = str(input('Obrigado! Deseja continuar?? S/N')).upper().strip()
    if ihala == "S":
        ent = str(input('Digite uma letra:  '))
        while ent != nomes:
            ent = str(input('Digite uma letra:  '))
        else:
            print('OK, vlw ;)')