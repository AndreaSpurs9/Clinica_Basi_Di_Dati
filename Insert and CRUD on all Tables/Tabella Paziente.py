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

# Connessione al database MySQL
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

# Operazioni CRUD

# Aggiunta Pazienti:
nuovo_paziente = Paziente(nome="Mario Rossi", data_nascita="13/03/1970",
                              telefono="3145672890", indirizzo="via roma 1")
session.add(nuovo_paziente)
session.commit()
nuovo_paziente = Paziente(nome="Lucia Neri", data_nascita="20/12/1967",
                              telefono="3383872504", indirizzo="via milano 8")
session.add(nuovo_paziente)
session.commit()
nuovo_paziente = Paziente(nome="Massimo Verdi", data_nascita="04/07/1994",
                              telefono="3274092167", indirizzo="via padova 84")
session.add(nuovo_paziente)
session.commit()
nuovo_paziente = Paziente(nome="Lucio Giusti", data_nascita="24/01/1967",
                              telefono="3397654231", indirizzo="via milano 16")

session.add(nuovo_paziente)
session.commit()

# Modifica Paziente:
paziente = session.query(Paziente).filter_by(id_paziente='4').first()
if paziente:
    paziente.nome = "Simone"
    session.commit()
    
# Lettura Pazienti:       
session.query(Paziente).all()

# Delete Paziente:
paziente = session.query(Paziente).filter_by(id_paziente='4').first()
if paziente:
    session.delete(paziente)
    session.commit()

session.close()
