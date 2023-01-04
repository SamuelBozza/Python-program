#CRIANDO AS LISTAS/DICIONARIO QUE VAI GUARDAR OS DADOS.
registro = dict()
final = list()
mulheres = list()
média = 0 #DEFININDO A MÉDIA DAS IDADES PARA 0
while True:
        registro['nome'] = str(input('Nome: ')) #ARMAZENAR O NOME NO DICIONARIO 'REGISTRO'
        registro['sexo'] = str(input('Sexo: [M/F] ')) #ARMAZENAR O SEXO NO DICIONARIO 'REGISTRO'
        while registro['sexo'] not in 'MmFf': #FAZENDO REPETIÇÃO PARA O SEXO SÓ ACEITAR 'M' ou 'F'
            print('ERRO! Por favor, digite apenas M ou F.')
            registro['sexo'] = str(input('Sexo: [M/F] '))
        registro['idade'] = int(input('Idade: '))
        if registro['sexo'] in 'Ff': # SE FEMININO O NOME DA PESSOA SERA ARMAZENADO NA LISTA DE MULHERES.
            mulheres.append(registro['nome'])
        média += registro['idade'] #ADICIONANDO A IDADADE REAL NA MÉDIA
        final.append(registro.copy()) #FAZENDO UMA CÓPIA DO REGISTRO PARA PODER RESETA-LO
        registro.clear() #LIMPANDO O REGISTRO ATUAL PARA ENTRAR O PRÓXIMO
        continuar = str(input('Quer continuar? [S/N] ')) #OPÇÃO DE CONTINUAÇÃO
        while continuar not in 'SsNn': #FAZENDO A CONTINUAÇÃO SÓ ACEITAR 'S' OU 'N'
            print('ERRO! Responda apenas S ou N!')
            continuar = str(input('Quer continuar? [S/N] '))
        if continuar in 'Nn': #SE A CONTINUAÇÃO FOR IGUAL A 'N' O PROGRAMA VAI PARAR.
            break
#PRINT DOS RESULTADOS
print('-='*30)
print(f'A) Ao todo temos {len(final)} pessoas cadastradas.')
média = média / len(final) #PEGANDO A IDADE DE TODOS OS REGISTROS (JA SOMADO) E DIVIDINDO PELO TOTAL DE REGITROS.
print(f'B) A média de idade é de {média:.2f} anos.')
print(f'C) As mulheres cadastradas foram {mulheres}')
print('D) A lista de pessoas com idade acima da média:')
for p in final: #SE A IDADE FOR MAIOR QUE A MÉDIA QUE JA FOI DEFINIDA, OS REGISTOS DE TAL PESSOA SERÃO EXIBIDOS.
    if p['idade'] >= média:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v} ;', end='')
        print()
print('<< FIM DO PROGRAMA >>')