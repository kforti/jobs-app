from pathlib import Path
import os

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
import mysql.connector
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.joinpath(".env"))

host = os.environ.get("DATABASE_HOST")
user = os.environ.get("DATABASE_USER"),
password = os.environ.get("DATABASE_PASSWORD")
database = os.environ.get("DATABASE_NAME", "")

mydb = mysql.connector.connect(
  host=os.environ.get("DATABASE_HOST"),
  user=os.environ.get("DATABASE_USER"),
  password=os.environ.get("DATABASE_PASSWORD")
)

mycursor = mydb.cursor()
mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
resp = mycursor.execute(f"SHOW databases")

meta = MetaData()

students = Table(
   'jobs', meta,
   Column('id', Integer, primary_key=True),
   Column('status', String(50))
)

url = f"mysql://root:{password}@{host}:3306/{database}"
engine = create_engine(url, echo=True)
meta.create_all(engine)