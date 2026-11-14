#Cadastro e Matriz por: Ana Gabriely 
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