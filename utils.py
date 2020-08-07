from models import Pessoas, db_session, Usuarios


# Insere dados na tabela
def insere_pessoas():
    pessoa = Pessoas(nome='Capelotti', idade=25)
    print(pessoa)
    pessoa.save()


# Realiza consulta na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    #pessoa = Pessoas.query.filter_by(nome='Capelotti').first()
    #print(pessoa.idade)


# Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Capelotti').first()
    pessoa.nome = 'Cesar'
    pessoa.save()


# Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Capelotti').first()
    pessoa.delete()


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)



if __name__ == '__main__':
    insere_usuario('pedro', '1234')
    insere_usuario('capelotti', '4321')
    consulta_todos_usuarios()
    #insere_pessoas()
    #consulta_pessoas()
    #exclui_pessoa()
    #altera_pessoa()

