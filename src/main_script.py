from src.MongoScheme import MongoScheme
from src.PostgresScheme import PostgresScheme
from src.MySqlScheme import MySqlScheme
from src.OracleScheme import OracleScheme

mongo = MongoScheme('lab1_mongodb')
mongo.drop_db()
mongo.create_gen_db()

postgres = PostgresScheme('postgresql://postgres:postgres@localhost:5432/postgresdb')
postgres.clear()
postgres.generate_data()

mysql = MySqlScheme('mysql://root:root@localhost/sys')
mysql.clear()
mysql.generate_data(100, 100)

oracle = OracleScheme("oracle+cx_oracle://myschema:1234@localhost/orcl")
oracle.clear()
oracle.generate_data(100, 100)