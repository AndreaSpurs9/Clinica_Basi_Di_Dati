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

# Definizione della classe Medico
class Medico(Base):
    __tablename__ = 'medico'

    id_medico = Column(Integer, primary_key=True)
    nome = Column(String(255))
    specializzazione = Column(String(255))

# Definizione della classe Infermiere
class Infermiere(Base):
    __tablename__ = 'infermiere'

    id_infermiere = Column(Integer, primary_key=True)
    nome = Column(String(255))

# Definizione della classe Farmaco
class Farmaco(Base):
    __tablename__ = 'farmaco'

    id_farmaco = Column(Integer, primary_key=True)
    nome = Column(String(255))
    dosaggio = Column(String(255))
    scadenza = Column(String(255))
    utilizzo = Column(String(255))
    id_paziente = Column(Integer, ForeignKey('paziente.id_paziente'))

# Definizione della classe Risultato Esame
class RisultatoEsame(Base):
    __tablename__ = 'risultato_esame'

    id_risultato_esame = Column(Integer, primary_key=True)
    nome_esame = Column(String(255))
    esito = Column(String(255))
    data = Column(String(255))
    id_paziente = Column(Integer, ForeignKey('paziente.id_paziente'))

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

# Definizione della classe CartellaClinica
class CartellaClinica(Base):
    __tablename__ = 'cartella_clinica'

    id_cartella_clinica = Column(Integer, primary_key=True)
    motivazione = Column(String(255))
    id_paziente = Column(Integer, ForeignKey('paziente.id_paziente'))
    id_medico = Column(Integer, ForeignKey('paziente.id_medico'))
    id_diagnosi = Column(Integer, ForeignKey('paziente.id_diagnosi'))
    id_ricovero = Column(Integer, ForeignKey('paziente.id_ricovero'))
    id_operazione = Column(Integer, ForeignKey('paziente.id_operazione'))

# Selezione di tutti i pazienti
print("Utenti nel database:")
pazienti = session.query(Paziente).all()
for paziente in pazienti:
    print(f"ID: {paziente.id_paziente}, Nome: {paziente.nome}")

# Selezione di tutti i medici per una determinata specializzazione
risultati = session.query(Medico).filter(Medico.specializzazione == "ortopedia").all()

for medico in risultati:
    print(f"ID Medico: {medico.id_medico} - {medico.nome}")

# Selezione delle cartelle cliniche che presentano nella motivazione la parola ginocchio
risultati = session.query(CartellaClinica).filter(CartellaClinica.motivazione.like('%ginocchio%')).all()

for cartella_clinica in risultati:
    print(f"ID Cartella: {cartella_clinica.id_cartella_clinica}")

# Selezione dei pazienti con un farmaco assegnato e la motivazione presente nella cartella clinica
risultati = session.query(Paziente.nome.label('nome_paziente'), Farmaco.nome.label('nome_farmaco'), CartellaClinica.motivazione) \
  .join(Farmaco, Paziente.id_paziente == Farmaco.id_paziente) \
  .join(CartellaClinica, Paziente.id_paziente == CartellaClinica.id_paziente) \
  .all()

for risultato in risultati:
    print(f"Nome paziente: {risultato.nome_paziente}")
    print(f"Nome farmaco: {risultato.nome_farmaco}")
    print(f"Motivazione: {risultato.motivazione}")

# Selezione dei pazienti operati da un determinato medico
risultati = session.query(Paziente.nome, Operazione.data, Medico.id_medico) \
    .join(CartellaClinica, Paziente.id_paziente == CartellaClinica.id_paziente) \
    .join(Operazione, CartellaClinica.id_operazione == Operazione.id_operazione) \
    .join(Medico, CartellaClinica.id_medico == Medico.id_medico) \
    .filter(Medico.id_medico == 1) \
    .all()

for risultato in risultati:
    print(f"ID medico: {risultato.id_medico}")
    print(f"Nome paziente: {risultato.nome}")
    print(f"Data operazione: {risultato.data}")

session.close()
