from MongoScheme import MongoScheme
from PostgresScheme import PostgresScheme
from MySqlScheme import MySqlScheme

#mongo = MongoScheme('lab1_mongodb')
#mongo.drop_db()
#mongo.create_gen_db()

#postgres = PostgresScheme('postgresql://postgres:postgres@localhost:5432/postgresdb')
#postgres.clear()
#postgres.generate_data()

mysql = MySqlScheme('mysql://root:root@localhost/sys')
mysql.clear()
mysql.generate_data(100, 100)