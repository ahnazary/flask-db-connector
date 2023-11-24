import sqlalchemy
from sqlalchemy import text
from dotenv import load_dotenv
import os

load_dotenv()

class PostgresInterface:
    def __init__(self):
        self.user = os.getenv('NEON_POSTGRES_USER')
        self.password = os.getenv('NEON_POSTGRES_PASSWORD')
        self.host = os.getenv('NEON_POSTGRES_HOST')
        self.port = os.getenv('NEON_POSTGRES_PORT')
        self.database = os.getenv('NEON_POSTGRES_DB')
        self.engine = sqlalchemy.create_engine(
            f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}?sslmode=require'
        )
        self.connection = self.engine.connect()

    def execute(self, query):
        return self.connection.execute(query).fetchall()

    def close(self):
        self.connection.close()
        self.engine.dispose()


# pg_interface = PostgresInterface()
# query = text('select count(*) from stocks.balance_sheet')
# result = pg_interface.execute(query)
# print(result)