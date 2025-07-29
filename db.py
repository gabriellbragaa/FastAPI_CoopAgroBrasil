from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2

# Configurações do banco de dados

def get_connection():
    return psycopg2.connect(
        dbname="CoopAgroBrasil",
        user="postgres",
        password="12345678",
        host="localhost",
        port="5432"
    )