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
    'database': 'clinica',}

# Connessione al database
engine = create_engine(f"mysql+mysqlconnector://{DATABASE['username']}:{DATABASE['password']}@{DATABASE['host']}:{DATABASE['port']}/{DATABASE['database']}", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Definizione della classe Diagnosi
class Diagnosi(Base):
    __tablename__ = 'diagnosi'

    id_diagnosi = Column(Integer, primary_key=True)
    cura = Column(String(255))
    esito = Column(String(255))
    data = Column(String(255))

# Operazioni CRUD

# Aggiunta Diagnosi:
nuova_diagnosi = Diagnosi(cura="necessaria operazione", esito="rottura del legamento crociato anteriore sinistro",
                              data="14/04/2024")
session.add(nuova_diagnosi)
session.commit()
nuova_diagnosi = Diagnosi(cura="necessaria operazione", esito="setto nasale deviato",
                              data="29/12/2020")
session.add(nuova_diagnosi)
session.commit()
nuova_diagnosi = Diagnosi(cura="necessaria operazione", esito="braccio dx rotto",
                              data="29/12/2021")
session.add(nuova_diagnosi)
session.commit()


# Modifica Diagnosi:
diagnosi = session.query(Diagnosi).filter_by(id_diagnosi='3').first()
if diagnosi:
    session.data = "03/4/2024"
    session.commit()
    
# Lettura Diagnosi:       
session.query(Diagnosi).all()

# Delete Diagnosi:
diagnosi = session.query(Diagnosi).filter_by(id_diagnosi='3').first()
if diagnosi:
    session.delete(diagnosi)
    session.commit()


session.close()
