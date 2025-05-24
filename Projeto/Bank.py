import time

# Declarando variaveis

Menu_init = """
________________________________________________________

Seja bem vindo ao IBank

________________________________________________________

Já identificamos seu scan facil e acessamos sua conta

Escolha um transação:

[1] - Depositar
[2] - Sacar
[3] - Exibir extrato
[4] - Sair
________________________________________________________

Sua escolha: """

saldo = 0
n_max_saque = 3
menu = 0
extrato = ""

# Inicio do código
while True: 
    if  menu == 0:
        menu = int(input(Menu_init))
        while menu != 4:
            while menu > 4 or menu <1:
                if menu == 0: 
                   menu = int(input(Menu_init))
                else:   
                    print('Reposta inválida: digite escolha uma ação entre 1 e 4') 
                    menu =  int(input('Sua escolha: '))

       ######### Primeira opção

            if  menu == 1:
                print("""

________________________________________________________


                      DEPOSITO
                      

________________________________________________________

               """)
                deposito = float(input("Qual valor será depositado? "))
                print(f'Depositando.... \n')
                time.sleep(1)
                saldo = saldo + deposito
                extrato += f'Depósito: R$ {deposito:.2f}\n'
                while True:
                    resposta = input('Deseja ver o seu saldo?  [S/N]  \n').upper()
                    if resposta == 'S':
                       print(f'Seu saldo é de R$ {saldo:.2f}\n')
                       break
                    if resposta == 'N':
                       break
                while True:
                    resposta = input('Deseja voltar ao Menu?  [S/N] \n').upper()
                    if resposta == 'S':
                       menu = 0
                       print('Voltando ao menu \n')
                       time.sleep(1)
                       break
                    if resposta == 'N':
                       menu = 4
                       break
                   
            elif    menu == 2:
                    print("""

________________________________________________________


                      SAQUE
                      

________________________________________________________

               """)
                    print(f'Saldo atual: {saldo}\n')
                    saque = float(input("Qual valor será sacado? "))
                    while saque > saldo:
                        print ('Saldo insuficiente escolha um valor menor')
                        saque = float(input("Qual valor será sacado? "))
                    if  n_max_saque == 0:
                        print('Você excedeu seu limite de saques diários, por favor volte amanhã \n')
                        while True:
                            resposta = input('Deseja voltar ao Menu?  [S/N] \n').upper()
                            if  resposta == 'S':
                                menu = 0
                                print('Voltando ao menu \n')
                                time.sleep(1)
                                break
                            if  resposta == 'N':
                                menu = 4
                                break
                    else:
                        print('Sacando....\n')
                        time.sleep(1)
                        saldo = saldo-saque
                        n_max_saque = n_max_saque - 1
                        extrato += f'Saque: R$ {saque:.2f}\n'
                        while True:
                            resposta = input('Deseja ver o seu saldo?  [S/N]  \n').upper()
                            if  resposta == 'S':
                                print(f'Seu saldo é de R$ {saldo:.2f}\n')
                                break
                            if resposta == 'N':
                                break
                        while True:
                            resposta = input('Deseja voltar ao Menu?  [S/N] \n').upper()
                            if  resposta == 'S':
                                menu = 0
                                print('Voltando ao menu \n')
                                time.sleep(1)
                                break
                            if  resposta == 'N':
                                menu = 4
                                break
            elif menu == 3:
                if extrato == '':
                   print('Não houve nenhuma transação até o momento \n')
                print(extrato, f'__________________________\n \nSaldo Atual:  {saldo:.2f}') 
                while True:
                    resposta = input('Deseja voltar ao Menu?  [S/N] \n').upper()
                    if resposta == 'S':
                       menu = 0
                       print('Voltando ao menu \n')
                       time.sleep(1)
                       break
                    if resposta == 'N':
                       menu = 4
                       break


    print("""
_________________________________________________________________          

Obrigado por usar nossos serviços 
          
Volte sempre!
_________________________________________________________________          
          """)
    break
        


