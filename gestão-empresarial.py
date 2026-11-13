



def verificar_estoque():
    

    print("Quantidade de produtos: ")
    for nome_produto,quantidade in produtos.items():
        print(nome_produto,quantidade)

def cadastrar_produto():
    nome_produto = input("qual nomedo produto que deseja  registrar?")
    quantidade = int(input("Qual a quantidade do  produto  a ser  registrado?"))
    produtos[nome_produto] = quantidade

    for  nome_produto,quantidade in produtos.items():
        print(nome_produto,quantidade)

def consultar_funcionarios():
    print("Lista de funcionários: ")
    for nome_funcionarios,dados  in funcionarios.items():
        print(nome_funcionarios,dados)

def realizar_logout():
    print("saindo do sistema!")



produtos = {
    "garrafas": 1500,
    "canetas": 6000,
    "lapis" : 20000
}


funcionarios = {
    "Ana": {
        "cpf": "123.456.789-00",
        "cargo": "vendedora",
        "salario": 2500,
        "senha":"123abx"
    },
    "Carlos": {
        "cpf": "987.654.321-00",
        "cargo": "estoquista",
        "salario": 2200,
        "senha":"4050"
    },
    "Gustavo": {
        "cpf":"083.842.149-05",
        "cargo": "dev junior",
        "salario":4000,
        "senha": "3540"
    }
}

nome = input("Nome: ")
if nome not in funcionarios:
    print("Funcionário não encontrado!")
    exit()

tentativas = 3
while tentativas > 0:
    senha = input("Senha: ")
    if senha == funcionarios[nome]["senha"]:
        break 
    tentativas -= 1
    print(f"Senha errada! Restam {tentativas} tentativas.")
else:
   
    print("Acesso bloqueado!")
    exit()

cargo = funcionarios[nome]["cargo"]
print(f"Bem-vindo ao sistema, {nome}! ({cargo})")




print("bem vindo ao sistema da empresa")

print("1-verificar estoque de produtos")
print("2-cadastrar produtos")
print("3-consultar funcionarios")
print("4-realizar logout")

pergunta = {
    "1": verificar_estoque,
    "2": cadastrar_produto,
    "3": consultar_funcionarios,
    "4": realizar_logout
}


escolha = input("Qualé sua escolha?")
if escolha in pergunta:
    pergunta[escolha]()
else:
    print("não existe essa opção")



    







