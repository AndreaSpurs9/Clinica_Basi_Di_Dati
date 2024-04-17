import mysql.connector
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.inspection import inspect


DATABASE = {
    'username': 'root',
    'password': '1234',
    'host': 'localhost',
    'port': '3306',
    'database': 'clinica',
}

# Connessione al database
engine = create_engine(f"mysql+mysqlconnector://{DATABASE['username']}:{DATABASE['password']}@{DATABASE['host']}:{DATABASE['port']}/{DATABASE['database']}", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Definizione della classe Infermiere
class Infermiere(Base):
    __tablename__ = 'infermiere'

    id_infermiere = Column(Integer, primary_key=True)
    nome = Column(String(255))
    
# Operazioni CRUD

# Aggiunta Infermiere:
nuovo_infermiere = Infermiere(nome="Francesco Risi")
session.add(nuovo_infermiere)
session.commit()
nuovo_infermiere = Infermiere(nome="Marco Franchi")
session.add(nuovo_infermiere)
session.commit()
nuovo_infermiere = Infermiere(nome="Martina Belli")
session.add(nuovo_infermiere)
nuovo_infermiere = Infermiere(nome="Lucia Sala")
session.add(nuovo_infermiere)
session.commit()

# Modifica Infermiere:
infermiere = session.query(Infermiere).filter_by(id_infermiere='4').first()
if infermiere:
    infermiere.nome = "Simona"
    session.commit()
    
# Lettura Infermieri:       
session.query(Infermiere).all()

# Delete Infermiere:
infermiere = session.query(Infermiere).filter_by(id_infermiere='4').first()
if infermiere:
    session.delete(infermiere)
    session.commit()

session.close()

