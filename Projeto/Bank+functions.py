import time

# Variáveis globais
saldo = 0
n_max_saque = 3
extrato = ""
usuarios = []

# Função para criar um novo usuário
def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    cpf = input("Digite o CPF do usuário: ")
    usuarios.append({'nome': nome, 'cpf': cpf})
    print("Usuário cadastrado com sucesso!\n")

# Função para listar todos os usuários
def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.\n")
    else:
        print("Usuários cadastrados:")
        for user in usuarios:
            print(f"Nome: {user['nome']}, CPF: {user['cpf']}")
        print()

# Função para consultar usuário pelo CPF
def consultar_usuario():
    cpf = input("Digite o CPF do usuário: ")
    for user in usuarios:
        if user['cpf'] == cpf:
            print(f"Usuário encontrado: Nome: {user['nome']}, CPF: {user['cpf']}\n")
            return
    print("Usuário não encontrado.\n")

# Função para depósito
def depositar():
    global saldo, extrato
    print("\n--- DEPÓSITO ---\n")
    deposito = float(input("Qual valor será depositado? "))
    print("Depositando...\n")
    time.sleep(1)
    saldo += deposito
    extrato += f'Depósito: R$ {deposito:.2f}\n'
    mostrar_saldo()

# Função para saque
def sacar():
    global saldo, n_max_saque, extrato
    print("\n--- SAQUE ---\n")
    print(f'Saldo atual: R$ {saldo:.2f}')
    if n_max_saque == 0:
        print("Você excedeu seu limite de saques diários. Volte amanhã.\n")
        return
    saque = float(input("Qual valor será sacado? "))
    while saque > saldo:
        print("Saldo insuficiente. Escolha um valor menor.")
        saque = float(input("Qual valor será sacado? "))
    print("Sacando...\n")
    time.sleep(1)
    saldo -= saque
    n_max_saque -= 1
    extrato += f'Saque: R$ {saque:.2f}\n'
    mostrar_saldo()

# Função para exibir extrato
def exibir_extrato():
    print("\n--- EXTRATO ---\n")
    if not extrato:
        print("Não houve nenhuma transação até o momento.\n")
    else:
        print(extrato)
    print(f"Saldo atual: R$ {saldo:.2f}\n")

# Função para mostrar saldo
def mostrar_saldo():
    resposta = input("Deseja ver o seu saldo? [S/N] ").upper()
    if resposta == 'S':
        print(f"Seu saldo é de R$ {saldo:.2f}\n")

# Função principal
def main():
    menu = 0
    Menu_init = """
________________________________________________________

Seja bem-vindo ao IBank

________________________________________________________

Escolha uma transação:

[1] - Depositar
[2] - Sacar
[3] - Exibir extrato
[4] - Criar novo usuário
[5] - Listar todos os usuários
[6] - Consultar usuário
[7] - Sair
________________________________________________________

Sua escolha: """

    while True:
        time.sleep(1)
        try:
            menu = int(input(Menu_init))
            if menu == 1:
                depositar()
            elif menu == 2:
                sacar()
            elif menu == 3:
                exibir_extrato()
            elif menu == 4:
                criar_usuario()
            elif menu == 5:
                listar_usuarios()
            elif menu == 6:
                consultar_usuario()
            elif menu == 7:
                print("\nObrigado por usar nossos serviços. Volte sempre!\n")
                break
            else:
                print("Opção inválida! Digite uma opção de 1 a 7.\n")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.\n")

if __name__ == "__main__":
    main()
