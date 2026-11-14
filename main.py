#Cadastro e Matriz por: Ana Gabriely 
import time
import random
helperyou = {
    "nome":"helperyou.tech",
    "versao":"0.0.1",
    "slogan":"A Plataforma que oferece um help em seus primeiros passos tech.",
    "data":"Fundada: 28/09/2026."
}

funcionarios = ["Jose Cardoso","Julia Lima"]
username = ["josecardoso98","julialima23"]
setores = [
    [1,1,1], #Porta A
    [0,2,2], #Porta B
]

def mostrarsetores(setores):
    print("="*30)
    print("SETORES (SEGUROS) DISPONIVEIS")
    print("-- Livres e seguros = 1 --")
    print("-- Bloqueados(uso-não-recomendado) = 0 --")
    print("-- Em uso = 2 --")
    print("="*30)
    print(f"{setores[0]}")
    print(f"{setores[1]}")

def menu1():
    print("="*30)
    print("--- Cadastros de Funcionários ---")
    print("== Funcionários Cadastrados ===")
for nome in funcionarios:
    print(f"==>{nome}")
newfuncionario = input("Coloque seu nome para o cadastro: ")
while True:
    if newfuncionario != "":
        print(f"Funcionário{newfuncionario} cadastrado com sucesso!")
        funcionarios.append(newfuncionario)
        break
    else:
        print("Por favor, coloque caracteres e/ou nomes válidos!")
        newfuncionario = input("Coloque seu nome para o cadastro: ")

def menu2():
    nomedaempresa = ""
    codigo_empresa =""
    senha_empresa = ""
    while True:
        print("="*30)
        print("")
        print("Olá, antes de começar")
        print("gostaria que respondesse com uma das opções: ")
        print("")
        print("==LEMBRETE== \n> Você não tem nenhum cadastro em nossa plataforma.\n é recomendado o uso da opção [1].")
        print("[1] Primeira vez usando a HelperYou.")
        print("[2] Faço parte da HelperYou.")
        print("[3] Sair.")
        print("="*30)
        while True:
            opcao = input("Selecione apenas uma das opções acima (1,2, ou 3!:").strip()
            if opcao == "1" and opcao == "2"  and opcao == "3":
                break
            else:
                print("Selecione apenas o que se pede! \n[Erro: Caractere invalido!]")
            if opcao == "3":
                print("\nObrigada por utilizar a HelperYou! Até logo!")
                break
            if opcao == "1":
                print("="*30)
                print("Seja bem-vindo!")
                print("="*30)
                print("Realizaremos o cadastro da sua empresa agora mesmo!")
                print("="*30)
                while True:
                    numerodecadastro = random.randit(100,999999)
                    emailempresa = input ("> Insira o email empresarial: ").strip()
                    nomeadaempresa = input("> Nomeie sua empresa: ").strip()
                    codigo_empresa = input("> Crie um codigo: ").strip()
                    senha_empresa = input("> Crie uma senha: ").strip()

                    if nomedaempresa != "" and codigo_empresa !="" and emailempresa !="" and senha_empresa !="":
                        dadosempresa = {
                            'nome da empresa > ': nomeadaempresa,
                            'senha >': senha_empresa
                        }
                        print("")
                        print(f"==Empresa [{nomeadaempresa}] Cadastrada com Sucesso.==")
                        print(f"== Numero de Cadastro [{numerodecadastro}] ==")
                        print("")
                        print(f"> Dados da Empresa [{dadosempresa}] <")
                        print("")
                        time.sleep(2)
                        break

                    else:
                        print("")
                        print("== Algo deu errado ! ==")
                        print("")
            elif opcao == "2":
                if nomeadaempresa == "":
                    print("\n[Erro: Nenhuma empresa cadastrada no momento!]")
                    print("\nRealize o cadastro na opção [1] primeiro.")
                    time.sleep(2)
                    continue

                while True:
                    print("="*20)
                    print("\n>Seja bem-vindo novamente! \n>Realize a verificação de 3 etapas.")
                    print("")
                    print("="*20)
                    helperyoucode = "helpertech123"
                    numerodecadastro2 = random.randint(100,999999)
                    codigo_empresa2 = input(" > Insira seu código: ")
                    senha_empresa2 = input(" > Insira sua senha: ")

                    verificacao_helperyou = input(f"> Enviamos um código para o email [{emailempresa}.\n> Coloque-o: ]")
                    if codigo_empresa2 == codigo_empresa and senha_empresa2 == senha_empresa and verificacao_helperyou == helperyoucode:
                        print("Procurando...")
                        time.sleep(2)
                        print("")
                        print(f"= Empresa [{nomedaempresa}] encontrada!")
                        time.sleep(1)
                        print(f"= Numero de cadastro [{numerodecadastro2}]")
                        time.sleep(3)
                        print("== Registro realizado com sucesso ==")
                        time.sleep(1)
                        break
