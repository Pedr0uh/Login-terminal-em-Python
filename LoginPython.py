login = ""
senha = ""
tentativa = 0  # contador global

def main():
    inicio()

def inicio():
    while True:  # loop para manter o menu ativo
        print(r"""
__________________________________________________________________________

-------------------------------------------------------------------------
|      ____   _____  __  __     _   _   ___   _   _   ____     ____      |
|     |  _ ) |  ___||  \/  |   | | | | |_ _| | \ | | |  _ \   / __ \     |
|     | | )| | |_   |      |   | | | |  | |  |  \| | | | \ | | |  | |    |
|     |  _ \ |  _|  | |\/| |   | | | |  | |  |     | | | | | | |  | |    |
|     | |_) || |___ | |  | |   | |_| |  | |  | |\  | | |_/ | | |__| |    |
|     |____/ |_____||_|  |_|    \___/  |___| |_| \_| |____/   \____/     |
|                                                                        |
-------------------------------------------------------------------------
__________________________________________________________________________
""")
        print(r"""Escolha uma opção:

    1 - Fazer Login

    2 - Criar Login
""")
        escolha = input("Digite a opção: ")
        match escolha:
            case "1": fazerLogin()
            case "2": criarLogin()
            case _: print("Opção inválida!")

def criarLogin():
    global login, senha
    print("\n")
    login = input("Crie seu usuário: ")
    senha = input("Crie sua senha: ")
    print("Cadastro realizado com sucesso!\n")

def fazerLogin():
    global tentativa
    global login, senha

    while tentativa < 5:
        entradaLogin = input("Digite seu usuário: ")
        entradaSenha = input("Digite sua senha: ")

        if entradaLogin == login and entradaSenha == senha:
            print(f"Bem vindo {login}!\n")
            home()
            return  # sai da função
        else:
            tentativa += 1
            print(f"Usuário ou senha incorretos. Tentativa {tentativa}/5\n")

    print("Número de tentativas excedido! Voltando ao menu.\n")
    tentativa = 0  # reseta para poder tentar de novo

def home():
    print("\nBazinga\n")
    import sys
    sys.exit()
    
if __name__ == "__main__":
    main()
