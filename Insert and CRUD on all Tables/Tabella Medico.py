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

# Definizione della classe Medico
class Medico(Base):
    __tablename__ = 'medico'

    id_medico = Column(Integer, primary_key=True)
    nome = Column(String(255))
    specializzazione = Column(String(255))

# Operazioni CRUD

# Aggiunta Medici:
nuovo_medico = Medico(nome="Filippo Giallo", specializzazione="ortopedia")
session.add(nuovo_medico)
session.commit()
nuovo_medico = Medico(nome="Simona Viola", specializzazione="estetica")
session.add(nuovo_medico)
session.commit()
nuovo_medico = Medico(nome="Filippo Giallo", specializzazione="generale")
session.add(nuovo_medico)
session.commit()
nuovo_medico = Medico(nome="Luca Bianchi", specializzazione="generale")
session.add(nuovo_medico)
session.commit()
# Modifica Medico:
medico = session.query(Medico).filter_by(id_medico='4').first()
if medico:
    medico.nome = "Simone"
    session.commit()
# Lettura Medici:        
session.query(Medico).all()
session.commit()
# Delete Medico:
medico = session.query(Medico).filter_by(id_medico='4').first()
if medico:
    session.delete(medico)
    session.commit()

session.close()
