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
    
# Definizione della classe Risultato Esame
class RisultatoEsame(Base):
    __tablename__ = 'risultato_esame'

    id_risultato_esame = Column(Integer, primary_key=True)
    nome_esame = Column(String(255))
    esito = Column(String(255))
    data = Column(String(255))
    id_paziente = Column(Integer, ForeignKey('paziente.id_paziente'))
    
# Operazioni CRUD

# Aggiunta RisultatoEsame:
nuovo_risultato_esame = RisultatoEsame(nome_esame="Risonanza Magnetica", esito="rottura del legamento crociato anteriore sinistro",
                              data="14/04/2024", id_paziente='2')
session.add(nuovo_risultato_esame)
session.commit()
nuovo_risultato_esame = RisultatoEsame(nome_esame="ECG", esito="situazione normale",
                              data="14/04/2024", id_paziente='2')
session.add(nuovo_risultato_esame)
session.commit()

# Modifica RisultatoEsame:
risultato_esame = session.query(RisultatoEsame).filter_by(id_risultato_esame='2').first()
if risultato_esame:
    risultato_esame.data = "04/04/2024"
    session.commit()
    
# Lettura RisultatoEsame:       
session.query(RisultatoEsame).all()

# Delete RisultatoEsame:
risultato_esame = session.query(RisultatoEsame).filter_by(id_risultato_esame='2').first()
if risultato_esame:
    session.delete(risultato_esame)
    session.commit()

session.close()
