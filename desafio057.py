# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto

sexo = input('Informe seu sexo [M/F]: ').strip().upper()[0]
while sexo != 'F' and sexo != 'M':
    sexo = input('Dados inválidos. Por favor, informe seu sexo: ').strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')