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

# Definizione della classe Paziente
class Paziente(Base):
    __tablename__ = 'paziente'

    id_paziente = Column(Integer, primary_key=True)
    nome = Column(String(255))
    data_nascita = Column(String(255))
    telefono = Column(String(255))
    indirizzo = Column(String(255))
    
# Definizione della classe Farmaco
class Farmaco(Base):
    __tablename__ = 'farmaco'

    id_farmaco = Column(Integer, primary_key=True)
    nome = Column(String(255))
    dosaggio = Column(String(255))
    scadenza = Column(String(255))
    utilizzo = Column(String(255))
    id_paziente = Column(Integer, ForeignKey('paziente.id_paziente'))
    
# Operazioni CRUD

# Aggiunta Farmaco:
nuovo_farmaco = Farmaco(nome="tachipirina", dosaggio="1000",
                              scadenza="04/2025", utilizzo="1 volta al giorno dopo cena",
                         id_paziente='1')
session.add(nuovo_farmaco)
session.commit()
nuovo_farmaco = Farmaco(nome="aulin", dosaggio="1000",
                              scadenza="04/2025", utilizzo="1 volta al giorno dopo cena",
                         id_paziente='1')
session.add(nuovo_farmaco)
session.commit()

# Modifica Farmaco:
farmaco = session.query(Farmaco).filter_by(id_farmaco='2').first()
if farmaco:
    farmaco.nome = "Aspirina"
    session.commit()
    
# Lettura Farmaci:       
session.query(Paziente).all()

# Delete Farmaco:
farmaco = session.query(Farmaco).filter_by(id_farmaco='2').first()
if farmaco:
    session.delete(farmaco)
    session.commit()


session.close()
