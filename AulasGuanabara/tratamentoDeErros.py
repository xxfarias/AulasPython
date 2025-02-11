# Tratamento de erros e excessões
try:
    a = int(input("Numerador: "))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('\033[31;1mTivemos um problema com os tipos de dados que você digitou.\033[m')
except ZeroDivisionError:
    print('\033[31;1mNão é possivel dividir por zero!\033[m')
except KeyboardInterrupt:
    print(f'O usuário preferiu não infomar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'\033[32;1mO resultado é {r:.1f}\033[m')
finally:
    print('Volte sempre! Muito obrigado!')