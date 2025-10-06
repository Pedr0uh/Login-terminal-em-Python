import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1", # temos que aprender como esconder host e senha
    user="aluno",
    password="toor",
    database="HospiBuy",
    port="3306"
)

cursor = conn.cursor(dictionary=True)

login = ""  # variavel login vazia
senha = ""  # variavel senha vazia
nome = ""
tentativa = 0  # contador global para tentativas


def main():

    print("Conectando com o Banco...")

    if conn.is_connected():
        print("\nConectado com o banco com sucesso!")
    else:
        print("\nFalha em conectar com o banco")

    inicio()


def inicio():

    """
    cpf_teste = "12345678900"
    nome_teste = "Pedro Teste"
    num_acess_teste = 0
    senha_teste = "1234"

    query = "INSERT INTO usuarios (CPF, nome, num_acesso, senha) VALUES (%s, %s, %s, %s)"
    valores = cpf_teste, nome_teste, num_acess_teste, senha_teste

    cursor.execute(query, valores) = digitar valores para query do SQL

    conn.commit() = para salvar no banco de dados

    cursor.execute("SELECT * FROM usuarios;") = query para mostrar os dados da tabela
    dadosUsuarios = cursor.fetchall() = guardei o comando fetchall em uma tabela, que mostra os dados da query
    (todas as linhas, fetchone para uma linha só)

    print(dadosUsuarios) dei print para mostrar o valor da variavel que é o fetchall

    """

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
        match escolha: # match para "escolha e caso" ligado a variavel escolha
            case "1": # caso a variavel seja 1
                fazerLogin()
            case "2": # caso a variavel seja 2
                criarLogin()
            case "3": # caso a variavel seja 3
                home()
            case _: # caso a variavel não seja nenhuma das opções
                print("Erro! Opção inválida!")


def criarLogin():

    global login, senha, nome


    cnes = input("\nInsira o CNES do Hospital (sem caracteres)")
    cnpj = input("Insira o CNPJ do Hospital (sem caracteres): ")
    nomeHospital = input("Insira o nome do Hospital: ")
    telefone = input("Insira um telefone de contato: ")
    email = input("Insira um email principal: ")
    cpfADM = input("Insira o CPF do administrador: ")
    nomeADM = input("Insira o nome do administrador: ")
    senha = input("Crie uma senha para o login do adminstrador: ")

    query = "INSERT INTO hospitais (CNES, CNPJ, nome, telefone, email, cpfADM, nomeADM, senha) VALUES (s%, s%, s%, s%, s%, s%, s%, s%)"
    valores = cnes, cnpj, nomeHospital, telefone, email, cpfADM, nomeADM, senha


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
    print(r"""
-- O que deseja fazer hoje? -- 

    1 - Verificar Estoque    
    2 - Comprar Itens
    3 - Descarte de Itens
    4 - Sair 
    """)

    opcao = input("Escolha a opção: ")

    while True:
        match opcao:
            case "1":
                estoque()
            case "2":
                compras()
            case "3":
                descarte()
            case "4":
                sair()
            case _:
                print("Erro! Tente novamente")

def estoque():
    print("\nEstoque aqui!\n")
    home()
    return

def compras():
    print("\nCompras aqui!\n")
    home()
    return

def compras():
    print("\nCompras aqui!\n")
    home()
    return

def descarte():
    print("\nDescarte aqui!\n")
    home()
    return

def sair():
    print("\nEncerrando Programa...\n")
    import sys
    sys.exit()

if __name__ == "__main__":
    main()
