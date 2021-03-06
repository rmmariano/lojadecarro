# coding: utf8

# Se estiver em ambiente de teste, cria temporariamente
# as dependências em relação aos importes automáticos
if 'db' not in locals():
    from global_imports import *

######################################################################

e_m={
    'empty':'Este campo é obrigatório',
    'in_db':'Este registro já existe no banco de dados',
    'not_in_db':'Este registro não existe no banco de dados',
    'email':'Você precisa inserir um e-mail válido',
    'image':'O arquivo precisa ser uma imagem válida',
    'not_in_set':'Você precisa escolher um valor válido',
    'not_in_range':'Digite um número entre %(min)s e %(max)s',
    }

config=dict(nmsite='Loja de Carro', dscsite='Só os melhores carros')

estados=('Novo', 'Usado')

cores=('Azul', 'Amarelo', 'Verde', 'Vermelho',\
    'Prata', 'Branco', 'Preto', 'Vinho')


# criamos um validador pré definido
notempty=IS_NOT_EMPTY(error_message=e_m['empty'])

# definição da tabela de marcas
db.define_table('marca',
                Field('nome', unique=True, notnull=True)
                #format='%(nome)s'
                )

# validadores da tabela de marcas
db.marca.nome.requires=[notempty, IS_NOT_IN_DB(db, 'marca.nome',error_message=e_m['in_db'])]

# definição da tabela de carros
db.define_table('carro',
                Field('marca', db.marca, notnull=True),
                Field('modelo', notnull=True),
                Field('ano', 'integer', notnull=True),
                Field('cor', notnull=True),
                Field('valor', 'double'),
                Field('itens', 'list:string'),
                Field('estado', notnull=True),
                Field('descr', 'text')
                # Field('foto', 'upload'),
                # format='%(modelo)s - %(ano)s - %(estado)s'               
                )

# validação da tabela carro
db.carro.marca.requires=IS_IN_DB(db, 'marca.id','marca.nome', 
                                 error_message=e_m['not_in_db'])
db.carro.modelo.requires=notempty
db.carro.ano.requires=[notempty,IS_INT_IN_RANGE(request.now.year-20,request.now.year+2,
                                                 error_message=e_m['not_in_range'])]
db.carro.cor.requires=IS_IN_SET(cores)
db.carro.itens.requires=IS_IN_SET(('Alarme','Trava','Som', 'Ar'),multiple=True,
                                  error_message=e_m['not_in_set'])
db.carro.estado.requires=IS_IN_SET(estados,error_message=e_m['not_in_set'])
#db.carro.foto.requires=IS_EMPTY_OR(IS_IMAGE(extensions=('jpeg', 'png', '.gif'),error_message=e_m['image']))

# definição da tabela de compradores
db.define_table('comprador',
                Field('id_carro', db.carro),
                Field('nome'),
                Field('email'),
                Field('telefone'),
                Field('financiar','boolean'),
                Field('troca','boolean')
                #Field('data', 'datetime', default=request.now)
                )

# validação da tabela de compradores
db.comprador.nome.requires=notempty
db.comprador.email.requires=IS_EMAIL(error_message=e_m['email'])
db.comprador.telefone.requires=notempty

#formatacao da tabela de compradores
db.comprador.nome.label = 'Seu nome completo'
db.comprador.email.label = 'Seu endereço de e-mail'
db.comprador.telefone.label = 'Seu telefone'
db.comprador.financiar.label = 'Quero financiar'
db.comprador.troca.label = 'Quero dar outro carro em troca'
# db.comprador.data.writable=False
# db.comprador.data.readable=False


# id_marca1 = db.marca.insert(nome="marca1")
# id_marca2 = db.marca.insert(nome="marca2")

# db.carro.insert(marca=id_marca1,modelo="modelo1",ano=1950,estado="Novo",
#                     cor="Preto",valor=30.000,descr="um carro preto")

