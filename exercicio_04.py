from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


# Conectar ao SQLite em memória
engine = create_engine('sqlite:///meubanco.db', echo=True)

print("Conexão com SQLite estabelecida.")

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=True)
    idade = Column(Integer, nullable=True)

Base.metadata.create_all(engine)

print("Tabela Criada com SQLite estabelecida.")

# assumindo que engine já foi criado

Session = sessionmaker(bind=engine)
session = Session()

with Session() as session:
    novo_usuario = Usuario(nome='Thiago', idade=36)
    session.add(novo_usuario)
    # O commit é feito automaticamente aqui, se não houver exceções
    # O rollback é automaticamente chamado se uma exceção ocorrer
    # A sessão é fechada automaticamente ao sair do bloco with
