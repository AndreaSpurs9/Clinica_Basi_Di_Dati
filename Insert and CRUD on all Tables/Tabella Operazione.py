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
    'database': 'clinica'
}

# Connessione al database MySQL
engine = create_engine(f"mysql+mysqlconnector://{DATABASE['username']}:{DATABASE['password']}@{DATABASE['host']}:{DATABASE['port']}/{DATABASE['database']}", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Definizione della classe Infermiere
class Infermiere(Base):
    __tablename__ = 'infermiere'

    id_infermiere = Column(Integer, primary_key=True)
    nome = Column(String(255))

# Definizione della classe Operazione
class Operazione(Base):
    __tablename__ = 'operazione'

    id_operazione = Column(Integer, primary_key=True)
    tipologia = Column(String(255))
    esito = Column(String(255))
    data = Column(String(255))
    id_infermiere = Column(Integer, ForeignKey('infermiere.id_infermiere'))

# Operazioni CRUD

# Aggiunta Operazioni:
nuova_operazione = Operazione(tipologia="ortopedia", esito="positivo",
                              data="16/04/2024", id_infermiere="3")
session.add(nuova_operazione)
session.commit()

nuova_operazione = Operazione(tipologia="estetica", esito="positivo",
                              data="02/01/2021", id_infermiere="1")
session.add(nuova_operazione)
session.commit()

nuova_operazione = Operazione(tipologia="ortopedia", esito="positivo",
                              data="02/01/2023", id_infermiere="2")
session.add(nuova_operazione)
session.commit()


# Modifica Operazione:
operazione = session.query(Operazione).filter_by(id_operazione='3').first()
if operazione:
    operazione.tipologia = "generale"
    session.commit()
    
# Lettura Operazioni:       
session.query(Operazione).all()

# Delete Operazione:
operazione = session.query(Operazione).filter_by(id_operazione='3').first()
if operazione:
    session.delete(operazione)
    session.commit()

session.close()
