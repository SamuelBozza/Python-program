'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''
registro = dict()
final = list()
mulheres = list()
média = 0
while True:
        registro['nome'] = str(input('Nome: '))
        registro['sexo'] = str(input('Sexo: [M/F] '))
        while registro['sexo'] not in 'MmFf':
            print('ERRO! Por favor, digite apenas M ou F.')
            registro['sexo'] = str(input('Sexo: [M/F] '))
        registro['idade'] = int(input('Idade: '))
        if registro['sexo'] in 'Ff': # SE FEMININO
            mulheres.append(registro['nome'])
        média += registro['idade']
        final.append(registro.copy())
        registro.clear()
        continuar = str(input('Quer continuar? [S/N] '))
        while continuar not in 'SsNn':
            print('ERRO! Responda apenas S ou N!')
            continuar = str(input('Quer continuar? [S/N] '))
        if continuar in 'Nn':
            break
print('-='*30)
print(f'A) Ao todo temos {len(final)} pessoas cadastradas.')
média = média / len(final)
print(f'B) A média de idade é de {média:.2f} anos.')
print(f'C) As mulheres cadastradas foram {mulheres}')
print('D) A lista de pessoas com idade acima da média:')
for p in final:
    if p['idade'] >= média:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v} ;', end='')
        print()
print('<< FIM DO PROGRAMA >>')