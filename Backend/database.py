import configparser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

config = configparser.ConfigParser()
config.read('config.prop')

db_user = config.get('DB_CRED','DB_USER')
db_pass = config.get('DB_CRED','DB_PASSWORD')
db_host = config.get('DB_CRED','DB_HOST')
db_port = config.get('DB_CRED','DB_PORT')
db_name = config.get('DB_CRED','DB_NAME')

DATABASE_URL = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
 
engine = create_engine(DATABASE_URL)

# sessionmaker creates a factory (a class) that can generate database sessions.
# A session = a connection to the database used for CRUD operations.

# “Create a session factory for connecting to the PostgreSQL database.
# Do not auto-commit or auto-flush. Use the engine we defined.”

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

Base = declarative_base()

