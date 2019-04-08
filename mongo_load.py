from pymongo import MongoClient
from random import randrange
from datetime import timedelta
from datetime import datetime
from bson.objectid import ObjectId


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


# campuses
def create_gen_campus(db):
    campuses = db.campuses
    campus_loc = "Vyazemskiy 5-7"
    campus_rtotal = 100
    campus_roccup = 70
    campus = {"location": campus_loc,
              "rooms_total": campus_rtotal,
              "rooms_occupied": campus_roccup
              }
    result = campuses.insert_one(campus)
    # campus_ref_key = result.inserted_id
    return campuses


# persons
def create_gen_persons(db):
    persons = db.persons
    person_names = ["Anton", "Oleg", "Irina", "Alena", "Yulia", "Svetlana", "Dmitriy", "Amalia", "John", "Victor"]
    person_surnames = ["Shultz", "Ruban", "Karno", "Kovalenko", "Simonenko", "Kern", "Bubenko", "Davidenko", "Krast",
                       "Topol"]
    person_privileges = ["yes", "no"]
    person_education_from = ["2014", "2015", "2016", "2017", "2018"]
    for x in range(200):
        person = {
            "name": person_names[randrange(len(person_names))],
            "surname": person_surnames[randrange(len(person_surnames))],
            "privileges": person_privileges[randrange(len(person_privileges))],
            "education_from": person_education_from[randrange(len(person_education_from))]
        }
        result = persons.insert_one(person)
    return persons


# rooms
def create_gen_rooms(db, campuses):
    rooms = db.rooms
    cf = campuses.find({"location":"Vyazemskiy 5-7"})
    room_num = int(cf[0]["rooms_total"])
    room_ttotal = 3
    room_tcurrent = 2
    room_san_date = [datetime.strptime('01/01/2014 01:00 AM', '%m/%d/%Y %I:%M %p'),
                     datetime.strptime('01/01/2019 01:00 AM', '%m/%d/%Y %I:%M %p')]
    room_san_bugs = ["yes", "no"]
    for x in range(room_num):
        room = {
            "campus_id": ObjectId(cf[0]["_id"]),
            "room_number": x+1,
            "tenants_total": randrange(2, room_ttotal),
            "tenants_current": randrange(1, room_tcurrent),
            "sanitazation": {
                "date": random_date(room_san_date[0], room_san_date[1]),
                "bedbugs": room_san_bugs[randrange(len(room_san_bugs))]
            }
        }
        result = rooms.insert_one(room)
    return rooms


# tenants
def create_gen_tenants(db, persons, rooms):
    tenants = db.tenants
    tenants_residence = [datetime.strptime('01/01/2014 01:00 AM', '%m/%d/%Y %I:%M %p'),
                         datetime.strptime('01/01/2019 01:00 AM', '%m/%d/%Y %I:%M %p')]
    tenants_payment_s = 5000
    tenants_warnings = 3
    rd = 1
    next = 0
    for p in persons.find({}, {"_id": 1}):
        rsd = random_date(tenants_residence[0], tenants_residence[1])
        red = random_date(rsd, tenants_residence[1])
        vsd = random_date(rsd, red)
        ved = random_date(vsd, red)
        pd = random_date(rsd, red)
        tenant = {
            "person_id": p["_id"],
            "room_num": rd,
            "residence": {
                "startDate": rsd,
                "endDate": red
            },
            "visit": {
                "startDate": vsd,
                "endDate": ved,
            },
            "payment": {
                "date": pd,
                "sum": randrange(tenants_payment_s)
            },
            "warnings": randrange(tenants_warnings)
        }
        result = tenants.insert_one(tenant)
        next = next + 1
        if next%2==0:
            rd = rd +1
    return tenants

def create_gen_db(db):
    campuses = create_gen_campus(db)
    persons = create_gen_persons(db)
    rooms = create_gen_rooms(db, campuses)
    tenants = create_gen_tenants(db, persons, rooms)
    for t in tenants.find():
        print(t)
    print("\n")
    for r in rooms.find():
        print(r)
    print("\n")
    for p in persons.find():
        print(p)
    print("\n")
    for c in campuses.find():
        print(c)
    return db


def drop_db(db):
    for col in db.list_collection_names():
        db[col].drop()


def main():
    client = MongoClient()
    db = client['lab1_mongodb']
    drop_db(db)
    create_gen_db(db)

if __name__ == "__main__":
    main()