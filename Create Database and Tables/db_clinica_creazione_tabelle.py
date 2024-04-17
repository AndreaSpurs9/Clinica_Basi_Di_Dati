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

# Connessione al server MySQL
conn = mysql.connector.connect(
    user=DATABASE['username'],
    password=DATABASE['password'],
    host=DATABASE['host'],
    port=DATABASE['port']
)

# Creazione del database se non esiste
def create_database(conn, database_name):
    try:
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        print(f"Database '{database_name}' creato con successo.")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Errore durante la creazione del database: {err}")

# Creazione delle tabelle se non esistono
def create_table(conn, database_name):
    try:
        cursor = conn.cursor()
        cursor.execute(f"USE {database_name}")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS paziente (
                id_paziente INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                data_nascita VARCHAR(255) NOT NULL,
                telefono VARCHAR(255) NOT NULL,
                indirizzo VARCHAR(255) NOT NULL
            )
        """)
        print("Tabella 'paziente' creata con successo.")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS medico (
                id_medico INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                specializzazione VARCHAR(255) NOT NULL
            )
        """)
        print("Tabella 'medico' creata con successo.")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS infermiere (
                id_infermiere INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL
            )
        """)
        print("Tabella 'infermiere' creata con successo.")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS farmaco (
                id_farmaco INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                dosaggio VARCHAR(255) NOT NULL,
                scadenza VARCHAR(255) NOT NULL,
                utilizzo VARCHAR(255) NOT NULL,
                id_paziente INT, FOREIGN KEY(id_paziente) REFERENCES Paziente(id_paziente)
            )
        """)
        print("Tabella 'farmaco' creata con successo.")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS risultato_esame (
                id_risultato_esame INT PRIMARY KEY AUTO_INCREMENT,
                nome_esame VARCHAR(255) NOT NULL,
                esito VARCHAR(255) NOT NULL,
                data VARCHAR(255) NOT NULL,
                id_paziente INT, FOREIGN KEY(id_paziente) REFERENCES Paziente(id_paziente)
            )
        """)
        print("Tabella 'risultato_esame' creata con successo.")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS operazione (
                id_operazione INT PRIMARY KEY AUTO_INCREMENT,
                tipologia VARCHAR(255) NOT NULL,
                esito VARCHAR(255) NOT NULL,
                data VARCHAR(255) NOT NULL,
                id_infermiere INT, FOREIGN KEY(id_infermiere) REFERENCES infermiere(id_infermiere)
            )
        """)
        print("Tabella 'operazione' creata con successo.")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS diagnosi (
                id_diagnosi INT PRIMARY KEY AUTO_INCREMENT,
                cura VARCHAR(255) NOT NULL,
                esito VARCHAR(255) NOT NULL,
                data VARCHAR(255) NOT NULL
            )
        """)
        print("Tabella 'ricovero' creata con successo.")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ricovero (
                id_ricovero INT PRIMARY KEY AUTO_INCREMENT,
                data_inizio VARCHAR(255) NOT NULL,
                data_fine VARCHAR(255) NOT NULL
            )
        """)
        print("Tabella 'ricovero' creata con successo.")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cartella_clinica (
                id_cartella_clinica INT PRIMARY KEY AUTO_INCREMENT,
                motivazione VARCHAR(255) NOT NULL,
                id_paziente INT,
                id_medico INT,
                id_diagnosi INT,
                id_ricovero INT,
                id_operazione INT,
                FOREIGN KEY(id_paziente) REFERENCES paziente(id_paziente),
                FOREIGN KEY(id_medico) REFERENCES medico(id_medico),
                FOREIGN KEY(id_diagnosi) REFERENCES diagnosi(id_diagnosi),
                FOREIGN KEY(id_ricovero) REFERENCES ricovero(id_ricovero),
                FOREIGN KEY(id_operazione) REFERENCES operazione(id_operazione)
            )
        """)
        print("Tabella 'cartella_clinica' creata con successo.")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Errore durante la creazione della tabella: {err}")

create_database(conn, DATABASE['database'])
create_table(conn, DATABASE['database'])

