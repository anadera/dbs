from pymongo import MongoClient
from src.Util import random_date, generate_name_string
from random import randrange
from datetime import datetime
from bson.objectid import ObjectId


class MongoScheme:
    def __init__(self, dbname):
        self.client = MongoClient()
        self.db = self.client[dbname]

    # campuses
    def create_gen_campus(self):
        campuses = self.db.campuses
        campus_loc = "Vyazemskiy 5-7"
        campus_rtotal = 100
        #campus_roccup = 70
        campus = {
            "location": campus_loc,
            "rooms_total": campus_rtotal
        }
        result = campuses.insert_one(campus)
        # campus_ref_key = result.inserted_id
        return campuses

    # persons
    def create_gen_persons(self):
        persons = self.db.persons
        person_names = ["Anton", "Oleg", "Irina", "Alena", "Yulia", "Svetlana", "Dmitriy", "Amalia", "John", "Victor"]
        person_surnames = ["Shultz", "Ruban", "Karno", "Kovalenko", "Simonenko", "Kern", "Bubenko", "Davidenko",
                           "Krast",
                           "Topol"]
        person_privileges = ["yes", "no"]
        person_places = ["Omsk", "Tomsk", "Barnaul", "Ekaterinburg", "Volgograd", "Pskov", "Ussuriysk", "Bobruysk", "Astrahan", "Armavir"]
        person_education_from = ["2014", "2015", "2016", "2017", "2018"]
        for x in range(200):
            person = {
                "surname": person_surnames[randrange(len(person_surnames))],
                "name": person_names[randrange(len(person_names))],
                "dateOfBirth": random_date(datetime.strptime('01/01/1985 01:00 AM', '%m/%d/%Y %I:%M %p'),
                                           datetime.strptime('01/01/2002 01:00 AM', '%m/%d/%Y %I:%M %p')),
                "placeOfBirth": person_places[randrange(len(person_places))]
                #"education_from": person_education_from[randrange(len(person_education_from))]
            }
            result = persons.insert_one(person)
        return persons

    # rooms
    def create_gen_rooms(self):
        rooms = self.db.rooms
        cf = self.db.campuses.find({"location": "Vyazemskiy 5-7"})
        room_num = int(cf[0]["rooms_total"])
        room_ttotal = 3
        room_tcurrent = 2
        room_san_date = [datetime.strptime('01/01/2014 01:00 AM', '%m/%d/%Y %I:%M %p'),
                         datetime.strptime('01/01/2019 01:00 AM', '%m/%d/%Y %I:%M %p')]
        room_san_bugs = ["yes", "no"]
        for x in range(room_num):
            room = {
                "room_number": x + 1,
                "campus_id": ObjectId(cf[0]["_id"]),
                "number_of_beds": randrange(2, room_ttotal),
                #"tenants_current": randrange(1, room_tcurrent),
                "sanitazation": {
                    "date_of_procedure": random_date(room_san_date[0], room_san_date[1]),
                    "bed_bugs": room_san_bugs[randrange(len(room_san_bugs))]
                }
            }
            result = rooms.insert_one(room)
        return rooms

    # tenants
    def create_gen_tenants(self):
        tenants = self.db.tenants
        tenants_residence = [datetime.strptime('01/01/2014 01:00 AM', '%m/%d/%Y %I:%M %p'),
                             datetime.strptime('01/01/2019 01:00 AM', '%m/%d/%Y %I:%M %p')]
        tenants_payment_s = 5000
        tenants_warnings = 3
        rd = 1
        next = 0
        for p in self.db.persons.find({}, {"_id": 1}):
            rsd = random_date(tenants_residence[0], tenants_residence[1])
            red = random_date(rsd, tenants_residence[1])
            vsd = random_date(rsd, red)
            ved = random_date(vsd, red)
            pd = random_date(rsd, red)
            tenant = {
                "person_id": p["_id"],
                "room_num": rd,
                "startDate": rsd,
                "endDate": red,
                "visit": {
                    "startDate": vsd,
                    "endDate": ved,
                },
                "payment": {
                    "date_of_transaction": pd,
                    "sum": randrange(tenants_payment_s)
                }
                #"warnings": randrange(tenants_warnings)
            }
            result = tenants.insert_one(tenant)
            next = next + 1
            if next % 2 == 0:
                rd = rd + 1
        return tenants

    def create_gen_db(self):
        MongoScheme.create_gen_campus(self)
        MongoScheme.create_gen_persons(self)
        MongoScheme.create_gen_rooms(self)
        MongoScheme.create_gen_tenants(self)
        # for t in self.db.tenants.find():
        #     print(t)
        # print("\n")
        # for r in self.db.rooms.find():
        #     print(r)
        # print("\n")
        # for p in self.db.persons.find():
        #     print(p)
        # print("\n")
        # for c in self.db.campuses.find():
        #     print(c)
        return self.db

    def drop_db(self):
        for col in self.db.list_collection_names():
            self.db[col].drop()
