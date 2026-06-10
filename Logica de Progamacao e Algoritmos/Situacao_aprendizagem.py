# Situação de Aprendizagem
# O sistema deve permitir:
# - Cadastrar
# - Listar
# - Deletar

# Criação das listas
usuarios = []
jogos = []

# -----------------

# -------- Função Menu Usuários ---------
def menu_usuarios():
    opcao_menu_usuario = 0

    while(opcao_menu_usuario != 4):
        print()
        print(" ----- Menu Usuários -----")
        print("1 - Cadastrar Usuários")
        print("2 - Listar Usuários")
        print("3 - Deletar Usuários")
        print("4 - Voltar")

        opcao_menu_usuario = int(input("Escolha um opção: "))

        match opcao_menu_usuario:
            # Cadastrar Usuário

            case 1:
                nome = input("Digite um nome: ")
                senha = int(input("Digite uma senha apenas com Números: "))
                telefone = input("Digite um telefone: ")
                email = input("Digite um email: ")

                # Crianção do JSON dos Usuários (Chave: Valor)

                usuario = {
                    "nome": nome,
                    "senha": senha,
                    "telefone": telefone,
                    "email": email
                }

                # Adicionar o json no array

                usuarios.append(usuario)
                print(f"Usuário{usuario["nome"]} cadastrado com sucesso!")
            # Listar Usuários

            case 2:
                print("\n Lista de usuários: ")

                if(len(usuarios) == 0 ):
                    print("Nenhum usuário cadastrado! ")
                else:
                    for usu in usuarios:
                        print("---------")
                        print("Nome: ",usu["nome"])
                        print("Senha ",usu["senha"])
                        print("telefone: ",usu["telefone"])
                        print("email: ",usu["email"])

            # Deletar usuário
            
            case 3:
                nome_deletar = input("Digite o nome do usuário que deseja deletar :")
                encontrado = False

                for usu in usuarios:
                    if(usu["nome"] == nome_deletar):
                        usuarios.remove(usu)
                        encontrado = True
                        print("Usuário removido com Sucesso! ")

                if(encontrado == False):
                    print("Usuário não encontrado! ")

            # Voltar ao menu principal

            case 4:
                print("Voltando ao menu principal...")
                break
                
# ----------------------------------
# -------- Função Menu Jogos ---------

def menu_jogos():
    opcao_menu_jogo = 0

    while(opcao_menu_jogo != 5):
        print()
        print(" ----- Menu Jogos -----")
        print("1 - Cadastrar Jogo")
        print("2 - Listar Jogos")
        print("3 - Deletar Jogos")
        print("4 - Voltar")

        opcao_menu_jogo = int(input("Escolha um opção: "))

        match opcao_menu_jogo:

            # Cadastrar Jogo

            case 1:
                nome = input("Digite um nome de jogo: ")
                descricao = input("Digite uma descrição: ")
                valor = float(input("Digite um valor: "))

                # Crianção do JSON dos Usuários (Chave: Valor)

                jogo = {
                    "nome": nome,
                    "descricao": descricao,
                    "valor": valor
                }

                # Adicionar o json no array

                jogos.append(jogo)
                print(f"Jogo{jogo ["nome"]} cadastrado com sucesso!")

            # Listar Produtos

            case 2:
                print("\n Lista de Jogos: ")

                if(len(jogos) == 0 ):
                    print("Nenhum jogo cadastrado! ")

                else:
                    for pro in jogos:
                        print("---------")
                        print("Nome: ",pro["nome"])
                        print("descricao: ",pro["descricao"])
                        print("valor: ",pro["valor"])

            # Deletar Produto

            case 3:
                nome_deletar = input("Digite o nome do jogo que deseja deletar :")
                encontrado = False

                for pro in jogos:
                    if(pro["nome"] == nome_deletar):
                        jogos.remove(pro)
                        encontrado = True
                        print("Jogo removido com Sucesso! ")

                if(encontrado == False):
                    print("Jogo não encontrado! ")

            # Voltar ao menu principal

            case 4:
                print("Voltando ao menu principal...")
                break
            
# ---------------------------------
# ------- Menu Principal -------
opcao_menu = 0
while(opcao_menu != 3):

    print("----- Menu Sistema de Cadastro --------")
    print("Opções: ")
    print("1 - Usuários")
    print("2 - Jogos")
    print("3 - Sair")
    opcao_menu = int(input("Escolha uma opção: "))

    match opcao_menu:
        # Menu Usuários
        case 1:
            menu_usuarios()
        # Menu Produtos
        case 2:
            menu_jogos()
        case 3:
            print("Até Logo")
        case _:
            print("Opção Ínvalida!")