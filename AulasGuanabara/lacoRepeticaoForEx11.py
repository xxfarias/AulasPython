somaIdade = 0
homemVelho = ''
idadeHomemVelho = 0
mulheresAbaixo = 0
for c in range (1,5):
    print(f'----- {c}ª Pessoa -----')
    nome = str(input(f'Digite o nome da pessoa {c}: ')).strip()
    idade = int(input(f'Digite a idade da pessoa {c}: '))
    sexo = str(input(f'Digite o sexo da pessoa {c} (M/F):')).strip().upper()
    somaIdade = somaIdade + idade
    if sexo == 'M' and idade >= idadeHomemVelho:
        idadeHomemVelho = idade
        homemVelho = nome
    if sexo == 'F' and idade < 20:
        mulheresAbaixo = mulheresAbaixo + 1
mediaIdade = somaIdade / 4
print(f'A média de idade foi de {mediaIdade}. \nO homem mais velho é o {homemVelho}\nTem {mulheresAbaixo} mulheres abaixo dos 20 anos.')    