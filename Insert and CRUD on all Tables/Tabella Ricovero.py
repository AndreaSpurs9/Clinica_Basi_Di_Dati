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

# Definizione della classe Ricovero
class Ricovero(Base):
    __tablename__ = 'ricovero'

    id_ricovero = Column(Integer, primary_key=True)
    data_inizio = Column(String(255))
    data_fine = Column(String(255))

# Operazioni CRUD

# Aggiunta Ricovero:
nuovo_ricovero = Ricovero(data_inizio="13/04/2024", data_fine="19/04/2024")
session.add(nuovo_ricovero)
session.commit()

nuovo_ricovero = Ricovero(data_inizio="28/12/2020", data_fine="05/01/2021")
session.add(nuovo_ricovero)
session.commit()

nuovo_ricovero = Ricovero(data_inizio="28/02/2020", data_fine="28/02/2020")
session.add(nuovo_ricovero)
session.commit()


# Modifica Ricovero:
ricovero = session.query(Ricovero).filter_by(id_ricovero='3').first()
if ricovero:
    session.data_inizio = "03/03/2020"
    session.commit()
    
# Lettura Ricoveri:       
session.query(Ricovero).all()

# Delete Ricovero:
ricovero = session.query(Ricovero).filter_by(id_ricovero='3').first()
if ricovero:
    session.delete(ricovero)
    session.commit()

session.close()
