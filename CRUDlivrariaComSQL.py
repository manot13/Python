import sqlite3
from sqlite3 import Error

def select_all():
    sql="SELECT * from tb_livro"
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

def insert_one():
    sql="insert into tb_livro(titulo, autor, preco, ano) values(?, ?, ?, ?)"
    p_titulo = input("Título: ")
    p_autor = input("Autor: ")
    p_preco = input("Preço: ")
    p_ano = input("Ano [aaaa/mm/dd]: ")
    try:
        cur.execute(sql, (p_titulo, p_autor, p_preco, p_ano))
        conexao.commit()
        print("One record added successfully")
    except Error as e:
        print('Mensagem de erro no insert_one:')
        print(e)
        conexao.rollback()

def update_one():
    sql="update tb_livro set autor=? where titulo=?"
    autor = input("Novo autor: ")
    p_titulo = input("Título: ")
    try:
        cur.execute(sql, (autor, p_titulo))
        conexao.commit()
    except Error as e:
        print('Mensagem de erro no update_one: ')
        print(e)
        conexao.rollback()

def delete_one():
    sql="delete from tb_livro where titulo=?"
    try:
        n=input("Título da exclusão: ")
        cur.execute(sql,(n,))
        conexao.commit()
    except Error as e:
        print("Mensagem de erro no delete_one")
        print(e)
        conexao.rollback()

if __name__ == '__main__':
    database = 'livros.db'
    conexao=sqlite3.connect(database)
    try:
        cur = conexao.cursor()
        cur.execute('''create table if not exists tb_livro(
            pk_idt integer primary key autoincrement,
            titulo text not null unique,
            autor text not null,
            preco float,
            ano text)
        ''')
        conexao.commit()
    except Error as e:
        print('Mensagem de erro no main: ')
        print(e)
        conexao.rollback()
        cur.close()
        conexao.close()
        exit(0)
    while True:
        opcao = int(
            input("[1] insert one\n[2] select all\n[3] update one\n[4] delete one\n[5] select one\n[6] drop table \n[0] sair\nopção: "))
        if opcao == 1:
            insert_one()
        elif opcao == 2:
            select_all()
        elif opcao == 3:
            update_one()
        elif opcao == 4:
            delete_one()
        elif opcao == 6:
            cur.execute('drop table tb_livro')
            print("Drop table....")
            break