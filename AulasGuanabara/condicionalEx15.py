cores = {'verde':'\033[1;32m', 'vermelho':'\033[1;31m', 'amarelo':'\033[1;33m', 'limpa':'\033[m'}   
print('Calculadora de IMC')
peso = float(input('Digite o seu peso:'))
altura = float(input('Digite a sua altura:'))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'{cores["vermelho"]}Abaixo do peso!{cores["limpa"]} Seu IMC é de {imc:.2f}')
elif imc >= 18.5 and imc < 25:
    print(f'{cores["verde"]}Peso ideal!{cores["limpa"]} Seu IMC é de {imc:.2f}')
elif imc >= 25 and imc < 30:
    print(f'{cores["amarelo"]}Sobrepeso!{cores["limpa"]} Seu IMC é de {imc:.2f}')
elif imc >= 30 and imc < 40:
    print(f'{cores["vermelho"]}Obesidade!{cores["limpa"]} Seu IMC é de {imc:.2f}')
else:
    print(f'{cores["vermelho"]}Obesidade Mórbida!{cores["limpa"]} Seu IMC é de {imc:.2f}')
    