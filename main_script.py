from MongoScheme import MongoScheme
from PostgresScheme import PostgresScheme

mongo = MongoScheme('lab1_mongodb')
postgres = PostgresScheme('postgresql://postgres:postgres@localhost:5432/postgresdb', "_postgres_scheme")