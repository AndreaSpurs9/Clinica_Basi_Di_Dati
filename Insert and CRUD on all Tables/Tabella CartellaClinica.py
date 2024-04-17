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

# Connessione al database
engine = create_engine(f"mysql+mysqlconnector://{DATABASE['username']}:{DATABASE['password']}@{DATABASE['host']}:{DATABASE['port']}/{DATABASE['database']}", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Definizione della classe CartellaClinica
class CartellaClinica(Base):
    __tablename__ = 'cartella_clinica'

    id_cartella_clinica = Column(Integer, primary_key=True)
    motivazione = Column(String(255))
    id_paziente = Column(Integer, ForeignKey('paziente.id_paziente'))
    id_medico = Column(Integer, ForeignKey('medico.id_medico'))
    id_diagnosi = Column(Integer, ForeignKey('diagnosi.id_diagnosi'))
    id_ricovero = Column(Integer, ForeignKey('ricovero.id_ricovero'))
    id_operazione = Column(Integer, ForeignKey('operazione.id_operazione'))

# Definizione della classe Paziente
class Paziente(Base):
    __tablename__ = 'paziente'

    id_paziente = Column(Integer, primary_key=True)
    nome = Column(String(255))
    data_nascita = Column(String(255))
    telefono = Column(String(255))
    indirizzo = Column(String(255))

# Definizione della classe Medico
class Medico(Base):
    __tablename__ = 'medico'

    id_medico = Column(Integer, primary_key=True)
    nome = Column(String(255))
    specializzazione = Column(String(255))

# Definizione della classe Operazione
class Operazione(Base):
    __tablename__ = 'operazione'

    id_operazione = Column(Integer, primary_key=True)
    tipologia = Column(String(255))
    esito = Column(String(255))
    data = Column(String(255))
    id_infermiere = Column(Integer, ForeignKey('infermiere.id_infermiere'))

# Definizione della classe Diagnosi
class Diagnosi(Base):
    __tablename__ = 'diagnosi'

    id_diagnosi = Column(Integer, primary_key=True)
    cura = Column(String(255))
    esito = Column(String(255))
    data = Column(String(255))

# Definizione della classe Ricovero
class Ricovero(Base):
    __tablename__ = 'ricovero'

    id_ricovero = Column(Integer, primary_key=True)
    data_inizio = Column(String(255))
    data_fine = Column(String(255))

# Operazioni CRUD

# Aggiunta CartellaClinica:
nuova_cartella_clinica = CartellaClinica(motivazione="Paziente operato al ginocchio sinistro causa rottura legamento, esito operazione positivo",
                                         id_paziente="2", id_medico="1",
                                         id_diagnosi="1", id_ricovero="1",
                                         id_operazione="1")
session.add(nuova_cartella_clinica)
session.commit()
                       
nuova_cartella_clinica = CartellaClinica(motivazione="necessario intervento facciale per setto nasale deviato, esito operazione positivo",
                                         id_paziente="1", id_medico="2",
                                         id_diagnosi="2", id_ricovero="2",
                                         id_operazione="2")
session.add(nuova_cartella_clinica)
session.commit()

nuova_cartella_clinica = CartellaClinica(motivazione="Paziente operato",
                                         id_paziente="2", id_medico="1",
                                         id_diagnosi="1", id_ricovero="1",
                                         id_operazione="1")
session.add(nuova_cartella_clinica)
session.commit()


# Modifica CartellaClinica:
cartella_clinica = session.query(CartellaClinica).filter_by(id_cartella_clinica='3').first()
if cartella_clinica:
    session.motivazione = "Dimesso"
    session.commit()
    
# Lettura CartelleCliniche:       
session.query(CartellaClinica).all()

# Delete CartellaClinica:
cartella_clinica = session.query(CartellaClinica).filter_by(id_cartella_clinica='3').first()
if cartella_clinica:
    session.delete(cartella_clinica)
    session.commit()

session.close()
