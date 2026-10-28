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
    [0,0,0], #Porta A
    [1,2,2], #Porta B
]

def mostrarsetores(setores):
    print("="*30)
    print("SETORES (SEGUROS) DISPONIVEIS")
    print("-- Livres = 0 --")
    print("-- Bloqueados = 1 --")
    print("-- Em uso = 2 --")
    print("="*30)
    print(f"{setores[0]}")
    print(f"{setores[1]}")

def menu1():
    print("="*30)
print("--- Cadastros de Funcionários ---")
for nome in funcionarios:
    print(f"==>{nome}")
newfuncionario = input("Coloque seu nome para o cadastro: ")

if newfuncionario != "":
    funcionarios = funcionarios + [newfuncionario]
    print(f"Bem-vindo(a),{newfuncionario},seu cadastro foi realizado com sucesso!")

