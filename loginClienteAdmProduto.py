#Uma empresa que vende instrumentos precisa de um sistema para administrar seus dados, incluindo dados de administrador, de clientes por acesso com contas e de compra e preço dos instrumentos.
import sqlite3
from sqlite3 import Error
vetIns = []
vetGuitarra = []
vetBateria = []
vetSaxofone = []
vetViolao = []
vetViolino = []

def selectAllUsuario():
    sql="SELECT * from tb_usuario"
    try:
        cur.execute(sql)
        registros = cur.fetchall()
        print("Consultando todos: ")
        for elemento in registros:
            print(elemento)
        print("Total de registros: ", len(registros))
    except Error as e:
        print('Mensagem de erro do select_all:')
        print(e)

def selectAllProduto():
    sql="SELECT * from tb_produto"
    try:
        cur.execute(sql)
        registros = cur.fetchall()
        print("\nSeu pedido: ")
        for elemento in registros:
            print(elemento)
        print("\nTotal de instrumento: ", len(registros))
    except Error as e:
        print("\nNão foi possível mostrar o seu pedido!")
        print(e)

def produtos():
    while True:
        op = int(input("\n|1 - Guitarra R$1200,00|\n|2 - Bateria R$5000,00|\n|3 - Saxofone R$2000,00|\n|4 - Violão R$300,00|\n|5 - Violino R$800,00|\n|6 - Sair|\n\nDigite a opção desejada: "))
        if op == 1:
            vetGuitarra.append("Guitarra")
            vetGuitarra.append(1200)
            vetIns.append(vetGuitarra)
        elif op == 2:
            vetBateria.append("Bateria")
            vetBateria.append(5000)
            vetIns.append(vetBateria)
        elif op == 3:
            vetSaxofone.append("Saxofone")
            vetSaxofone.append(2000)
            vetIns.append(vetSaxofone)
        elif op == 4:
            vetViolao.append("Violão")
            vetViolao.append(300)
            vetIns.append(vetViolao)
        elif op == 5:
            vetViolino.append("Violino")
            vetViolino.append(800)
            vetIns.append(vetViolino)
        elif op == 6:
            break
    pedido()

def precos():
    sql = "select sum(preco) from tb_produto"
    try:
        cur.execute(sql)
        precoTotal = cur.fetchone()
        print("\nPreço total: R$", precoTotal)
    except Error as e:
        print("Não foi possível somar os preços!")
        print(e)

def pedido():
    sql = "insert into tb_produto(instrumento, preco) values(?,?)"
    try:
        cur.executemany(sql, vetIns, )
        conexao.commit()
        print("\nPedido concluído com sucesso!")
    except Error as e:
        print("Não foi possível cadastrar o seu pedido!")
        print(e)
        conexao.rollback()
    selectAllProduto()
    precos()
    dlt = input("\n\nDeseja excluir algum pedido [s/n]? ")
    if dlt == 's' or dlt == 'S':
        deletar()
    else:
        print("Obrigado, volte sempre!")
        exit(0)

def deletar():
    sql="delete from tb_produto where instrumento=?"
    try:
        ins = input("Instrumento da exclusão: ")
        cur.execute(sql, (ins,))
        conexao.commit()
        print("\nExcluído com sucesso!\n\n")
        selectAllProduto()
        pedido()
    except Error as e:
        print("Não foi possível excluir!")
        print(e)
        conexao.rollback()

def updateNome():
    sql = "update tb_usuario set nome=? where senha=? AND email=?"
    n_nome = input("Novo nome: ")
    g_senha = input("Senha: ")
    p_email = input("Seu email: ")
    try:
        cur.execute(sql, (n_nome, g_senha, p_email))
        conexao.commit()
        print("\nSeu nome foi atualizado com sucesso!\n")
    except Error as e:
        print("Não foi possível atualizar o nome!")
        print(e)
        conexao.rollback()

def updateEmail():
    sql = "update tb_usuario set email=? where senha=? AND email=?"
    n_email = input("Novo email: ")
    g_senha = input("Senha: ")
    p_email = input("Seu email antigo: ")
    try:
        cur.execute(sql, (n_email, g_senha, p_email))
        conexao.commit()
        print("\nEmail atualizado com sucesso!\n")
    except Error as e:
        print("Não foi possível atualizar o email!")
        print(e)
        conexao.rollback()

def updateIdade():
    sql = "update tb_usuario set idade=? where senha=? AND email=?"
    n_idade = input("Nova idade: ")
    g_senha = input("Senha: ")
    p_email = input("Seu email: ")
    try:
        cur.execute(sql, (n_idade, g_senha, p_email))
        conexao.commit()
        print("\nIdade atualizada com sucesso!\n")
    except Error as e:
        print("Não foi possível atualizar a idade!")
        print(e)
        conexao.rollback()

def updateSenha():
    sql="update tb_usuario set senha=? where senha=? AND email=?"
    n_senha = input("Nova senha: ")
    g_senha = input("Senha antiga: ")
    p_email = input("Seu email: ")
    try:
        cur.execute(sql, (n_senha, g_senha, p_email))
        conexao.commit()
        print("\nSenha atualizada com sucesso!\n")
    except Error as e:
        print("Não foi possível atualizar senha!")
        print(e)
        conexao.rollback()

def updateMenu():
    opcao = int(input("\n|1 - Mudar senha|\n|2 - Mudar nome|\n|3 - Mudar email|\n|4 - Mudar idade|\n|5 - Fazer pedido|\n\nDigite a opção desejada: "))
    if opcao == 1:
        updateSenha()
        updateMenu()
    if opcao == 2:
        updateNome()
        updateMenu()
    if opcao == 3:
        updateEmail()
        updateMenu()
    if opcao == 4:
        updateIdade()
        updateMenu()
    elif opcao == 5:
        produtos()


def login():
    sql="SELECT * FROM tb_usuario WHERE email=? AND senha=?"
    p_email = input("Usuario: ")
    p_senha = input("Senha: ")
    try:
        cur.execute(sql, (p_email, p_senha))
        registro=cur.fetchone()
        if registro == None:
            print("\nUsuário ou senha inválidos!\n")
            login()
        else:
            print("\n\nBem vindo(a)!\n")
            updateMenu()
    except Error as e:
        print("Usuário ou senha inválidos!")
        print(e)
        conexao.rollback()

def cadastrar():
    sql="insert into tb_usuario(nome, idade, email, senha) values(?,?,?,?)"
    i_nome=input("Nome: ")
    i_idade=input("Idade: ")
    i_email=input("E-mail: ")
    i_senha=input("Senha: ")
    try:
        cur.execute(sql, (i_nome, i_idade, i_email, i_senha))
        conexao.commit()
        print("Dados inseridos corretamente!")
    except Error as e:
        print("Não foi possível inserir os dados!")
        print(e)
        conexao.rollback()

def cadastroAdm():
    sql = "insert into tb_adm(email, senha) values(?,?)"
    i_email = input("E-mail: ")
    i_senha = input("Senha: ")
    try:
        cur.execute(sql, (i_email, i_senha))
        conexao.commit()
        print("Dados inseridos corretamente!")
    except Error as e:
        print("Não foi possível inserir os dados!")
        print(e)
        conexao.rollback()

def loginAdm():
    sql = "SELECT * FROM tb_adm WHERE email=? AND senha=?"
    p_email = input("Usuario: ")
    p_senha = input("Senha: ")
    try:
        cur.execute(sql, (p_email, p_senha))
        registro = cur.fetchone()
        if registro == None:
            print("Usuário ou senha inválidos!")
        else:
            print("\n\nBem vindo(a)!\n\n")
            print("| ---------- Consulta de dados de usuários ---------- |\n\n")
            selectAllUsuario()
    except Error as e:
        print("Usuário ou senha inválidos!")
        print(e)
        conexao.rollback()

def parteAdm():
    while True:
        opc = int(input("\n|1 - Cadastro Adm|\n|2 - Login Adm|\n\nDigite a opção desejada: "))
        if opc == 1:
            cadastroAdm()
        elif opc == 2:
            loginAdm()
            break



if __name__ == '__main__':
    database = 'system.db'
    conexao=sqlite3.connect(database)
    try:
        cur = conexao.cursor()
        cur.execute('''create table if not exists tb_usuario(
            pk_cod integer primary key autoincrement,
            nome text not null,
            idade integer,
            email text not null unique,
            senha text not null)
         ''')
        cur.execute('''create table if not exists tb_produto(
            pk_cod integer primary key autoincrement,
            instrumento text,
            preco float)
         ''')
        cur.execute('''create table if not exists tb_adm(
             pk_cod integer primary key autoincrement,
             email text not null unique,
             senha text not null)
         ''')
        conexao.commit()
    except Error as e:
      print("Não foi possível conectar-se!")
      print(e)
      conexao.rollback()
      cur.close()
      conexao.close()
      exit(0)
    while True:
        op = int(input("\n|1 - Login|\n|2 - Cadastrar-se|\n|3 - Parte Adm|\n\nDigite a opção desejada: "))
        if op == 2:
            cadastrar()
        elif op == 1:
            login()
            break
        elif op == 3:
            parteAdm()
            break