from MongoScheme import MongoScheme
from PostgresScheme import PostgresScheme

#mongo = MongoScheme('lab1_mongodb')
#mongo.drop_db()
#mongo.create_gen_db()

postgres = PostgresScheme('postgresql://postgres:postgres@localhost:5432/postgresdb')
postgres.clear()
print("azaza")
postgres.generate_data()