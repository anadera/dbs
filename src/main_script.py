from src.MongoScheme import MongoScheme
from src.PostgresScheme import PostgresScheme
from src.MySqlScheme import MySqlScheme
from src.OracleScheme import OracleScheme
from src.ResultScheme import ResultScheme
from src.Util import toyear, postgres_date
from datetime import datetime


def generateConferecneParticipants(person):
    participantsCollection = []
    for participant in person.participant_of_conference_collection:
        participantsCollection.append(result.Conference_participants(id=participant.id, person_id=person.id,
                                                                     conference_id=participant.conference_id))
    return participantsCollection


def generateNewPersonWithEmployeeFromMySql(person, maxEmployeeId):
    names = person.full_name.split(' ')
    employeeCollection = generateEmployeesFromMysql(person, maxEmployeeId)
    return result.Person_result(id=person.id, surname=names[0],
                                name=names[1] if len(names) > 1 else None,
                                patronymic=names[2] if len(names) > 2 else None,
                                dateofbirth=person.birth_date,
                                placeofbirth="Unknown",
                                employee_collection=employeeCollection,
                                authors_collection=generateAuthors(person),
                                reading_list_collection=generateReadingList(person),
                                conference_participants_collection=generateConferecneParticipants(person))


def generateAuthors(person):
    authorsCollection = []
    for author in person.authors_collection:
        authorsCollection.append(result.Authors_result(id=author.id, publication_id=author.publication_id,
                                                       person_id=person.id))
    return authorsCollection


def generateReadingList(person):
    readingListCollection = []
    for readingList in person.reading_list_collection:
        readingListCollection.append(
            result.Reading_list_result(id=readingList.id, publisher_id=readingList.publisher_id,
                                       person_id=person.id, start_date=readingList.start_date,
                                       end_date=readingList.end_date))
    return readingListCollection


def generateEmployeesFromMysql(person, maxEmployeeId):
    employeeCollection = []
    for project in person.project_member_collection:
        employeeCollection.append(result.Employee_result(id=maxEmployeeId, position=person.position_name,
                                                         startdate=project.start_date, enddate=project.end_date,
                                                         project_members_collection=[
                                                             result.Project_member_result(id=project.id,
                                                                                          project_name=project.project_name,
                                                                                          member_id=maxEmployeeId)]))
    return employeeCollection


def generateScheduleFromOracle(employee):
    scheduleCollection = []
    for schedule in employee.schedule_info_collection:
        scheduleCollection.append(result.Schedule_result(id=schedule.id, subject_name=schedule.subject_name,
                                                         teacher_id=employee.id, dayofweek=schedule.day_of_week,
                                                         starttime=schedule.start_time, endtime=schedule.end_time,
                                                         typeofweek=schedule.type_of_week, room=schedule.room))
    return scheduleCollection


def generateEmployeesFromOracle(person):
    employeeCollection = []
    for employee in person.employee_collection:
        employeeCollection.append(result.Employee_result(id=employee.id,
                                                         subdivision_name=employee.subdivision_name,
                                                         position=employee.position,
                                                         startdate=employee.startdate,
                                                         enddate=employee.enddate,
                                                         schedule_collection=generateScheduleFromOracle(employee)))
    return employeeCollection


def generateStudentCollectionFromOracle(person):
    studentCollection = []
    for student in person.student_collection:
        studentCollection.append(
            result.Student_result(id=student.id, person_id=student.person_id, group_id=student.group_id,
                                  type_of_study=student.type_of_study, form_of_study=student.form_of_study,
                                  qualification=student.qualification[:2]))
    return studentCollection


def generatePulicationInfo(publisher):
    publicationCollection = []
    for publication in publisher.publication_collection:
        publicationCollection.append(
            result.Publication_result(id=publication.id, name=publication.name, type=publication.p_type,
                                      citation_index=publication.citation_index,
                                      publisher_id=publisher.id))
    return publicationCollection


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

result = ResultScheme('oracle+cx_oracle://newschema:1234@localhost/orcl')
result.clear()

persons_oracle = oracle.oracle_config.session.query(oracle.Person_oracle).all()
years_oracle = oracle.oracle_config.session.query(oracle.Year_oracle).all()
subdivision_oracle = oracle.oracle_config.session.query(oracle.Subdivision_oracle).all()
subjects_oracle = oracle.oracle_config.session.query(oracle.Subject_oracle).all()
programs_oracle = oracle.oracle_config.session.query(oracle.Program_oracle).all()
group_oracle = oracle.oracle_config.session.query(oracle.Group_oracle).all()
mark_oracle = oracle.oracle_config.session.query(oracle.Mark_oracle).all()
specialization_oracle = oracle.oracle_config.session.query(oracle.Specialization_oracle).all()

persons_mysql = mysql.my_sql_config.session.query(mysql.Person_mysql).all()
conferences_mysql = mysql.my_sql_config.session.query(mysql.Conference_mysql).all()
conference_info_mysql = mysql.my_sql_config.session.query(mysql.Conference_info_mysql)
projects_mysql = mysql.my_sql_config.session.query(mysql.Scientific_project_mysql).all()
publishers_mysql = mysql.my_sql_config.session.query(mysql.Publisher_mysql).all()

universities_postgres = postgres.postgres_config.session.query(postgres.University_postgres).all()
faculties_postgres = postgres.postgres_config.session.query(postgres.Faculty_postgres).all()
subdivisions_postgress = postgres.postgres_config.session.query(postgres.Subdivision_postgres).all()
specialization_postgress = postgres.postgres_config.session.query(postgres.Specialization_postgres).all()
student_group_postgress = postgres.postgres_config.session.query(postgres.Student_group_postgres).all()
student_postgress = postgres.postgres_config.session.query(postgres.Student_postgres).all()

semester_postgress = postgres.postgres_config.session.query(postgres.Semester_postgres).all()
subject_postgress = postgres.postgres_config.session.query(postgres.Subject_postgres).all()
employee_postgress = postgres.postgres_config.session.query(postgres.Employee_postgres).all()
specialization_program_postgress = postgres.postgres_config.session.query(
    postgres.Specialization_program_postgres).all()
results_postgress = postgres.postgres_config.session.query(postgres.Results_postgres).all()

result_people = {}

result.clear()

for c in mongo.campuses.find():
    result.result_config.session.add(
        result.Campus_result(id=c["id"],
                             location=c["location"],
                             rooms_total=c["rooms_total"]))
    result.result_config.session.commit()

for r in mongo.rooms.find():
    result.result_config.session.add(
        result.Room_result(id=r["id"],
                           room_number=r["room_number"],
                           campus_id=r["campus_id"],
                           number_of_beds=r["number_of_beds"]))
    result.result_config.session.add(
        result.Sanitization_result(id=r["id"],
                                   bed_bugs=r["sanitazation"]["bed_bugs"],
                                   date_of_procedure=r["sanitazation"]["date_of_procedure"],
                                   room_id=r["id"]))
    result.result_config.session.commit()

for mark in mark_oracle:
    result.result_config.session.add(
        result.Mark_result(mark_value = mark.name, letter = mark.letter))
    result.result_config.session.commit()

for year in years_oracle:
    result.result_config.session.add(
        result.Year_result(year_name=year.name, startdate=year.startdate, enddate=year.enddate))
    result.result_config.session.commit()

for subdivision in subdivision_oracle:
    result.result_config.session.add(
        result.Subdivision_result(name=subdivision.name))
    result.result_config.session.commit()

for project in projects_mysql:
    result.result_config.session.add(
        result.Scientific_project_result(name=project.name))
    result.result_config.session.commit()

for subject in subjects_oracle:
    result.result_config.session.add(
        result.Subject_result(name=subject.name))
    result.result_config.session.commit()

for program in programs_oracle:
    result.result_config.session.add(
        result.Program_result(id=program.id, name=program.name, code=program.code))
    result.result_config.session.commit()

for specialization in specialization_oracle:
    result.result_config.session.add(
        result.Specialization_result(id=specialization.id, name=specialization.name, code=specialization.code,
                                     program_id=specialization.program_id))
    result.result_config.session.commit()

for group in group_oracle:
    result.result_config.session.add(
        result.Group_result(id=group.id, name=group.name, year_name=group.year_name,
                            specialization_id=group.specialization_id,
                            subdivision_name=group.subdivision_name, coursenumber=group.coursenumber))
    result.result_config.session.commit()

for publisher in publishers_mysql:
    result.result_config.session.add(
        result.Publisher_result(id=publisher.id,
                                name=publisher.name,
                                type=publisher.p_type,
                                language=publisher.p_language,
                                date_of_publication=publisher.date_of_publication,
                                place=publisher.location,
                                n_size=publisher.size,
                                publication_collection=generatePulicationInfo(publisher)))
    result.result_config.session.commit()

for conference in conferences_mysql:
    result.result_config.session.add(
        result.Conference_result(name=conference.name))
    result.result_config.session.commit()

for conference in conference_info_mysql:
    result.result_config.session.add(result.Conference_info_result(id=conference.id,
                                                                   conference_name=conference.conference_name,
                                                                   publisher_id=conference.publisher_id,
                                                                   startdate=conference.start_date,
                                                                   enddate=conference.end_date,
                                                                   place=conference.place))
    result.result_config.session.commit()

students_collection = []
maxEmployeeId = max(oracle.oracle_config.session.query(oracle.Employee_oracle).all(), key=lambda x: x.id).id

for person in persons_oracle:
    students_collection = students_collection + generateStudentCollectionFromOracle(person)
    result_people[person.id] = result.Person_result(id=person.id,
                                                    surname=person.surname,
                                                    name=person.name,
                                                    patronymic=person.patronymic,
                                                    dateofbirth=person.date_of_birth,
                                                    placeofbirth=person.place_of_birth,
                                                    employee_collection=generateEmployeesFromOracle(person)
                                                    )

for person in persons_mysql:
    maxEmployeeId = maxEmployeeId + 1
    if person.id not in result_people.keys():
        result_people[person.id] = generateNewPersonWithEmployeeFromMySql(person, maxEmployeeId)
    else:
        original_person = result_people[person.id]
        result_people[person.id] = result.Person_result(id=original_person.id, surname=original_person.surname,
                                                        name=original_person.name,
                                                        patronymic=original_person.patronymic,
                                                        dateofbirth=original_person.dateofbirth,
                                                        placeofbirth=original_person.placeofbirth,
                                                        employee_collection=generateEmployeesFromMysql(
                                                            person,
                                                            maxEmployeeId) + original_person.employee_collection,
                                                        authors_collection=generateAuthors(person),
                                                        reading_list_collection=generateReadingList(person),
                                                        conference_participants_collection=generateConferecneParticipants(
                                                            person))

for person in mongo.persons.find():
    if person["id"] not in result_people.keys():
        result_people[person["id"]] = result.Person_result(
            id=person["id"],
            surname=person["surname"],
            name=person["name"],
            patronymic=None,
            dateofbirth=person["dateOfBirth"],
            placeofbirth=person["placeOfBirth"]
        )

for person in result_people.values():
    result.result_config.session.add(person)
    result.result_config.session.commit()

for t in mongo.tenants.find():
    if t["person_id"] not in result_people.keys():
        result_people[t["id"]] = result.Person_result(
            id=t["id"],
            surname="Unknown",
            name="Unknown",
            patronymic=None,
            dateofbirth=t["startDate"],
            placeofbirth="Unknown"
        )
        result.result_config.session.add(result_people[t["id"]])
        result.result_config.session.commit()
    result.result_config.session.add(
        result.Teenant_result(id=t["id"],
                              person_id=t["person_id"],
                              room_num=t["room_num"],
                              start_date=t["startDate"],
                              end_date=t["endDate"]))
    result.result_config.session.add(
        result.Visit_result(id=t["id"],
                            teenant_id=t["id"],
                            start_date=t["visit"]["startDate"],
                            end_date=t["visit"]["endDate"]))
    result.result_config.session.add(
        result.Payment_result(id=t["id"],
                              teenant_id=t["id"],
                              date_of_transaction=t["payment"]["date_of_transaction"],
                              sum=t["payment"]["sum"]))
    result.result_config.session.commit()

for university in universities_postgres:
    result.result_config.session.add(
        result.University_result(id=university.university_id,
                                 name=university.university_name,
                                 standart_type=university.university_standart_type))
    result.result_config.session.commit()

for faculty in faculties_postgres:
    result.result_config.session.add(
        result.Faculty_result(id=faculty.faculty_id,
                              name=faculty.faculty_name,
                              university_id=faculty.f_university_id,
                              type=None))
    result.result_config.session.commit()

for subdivision in subdivisions_postgress:
    result.result_config.session.add(
        result.Subdivision_result(
            name=subdivision.subdivision_name,
            faculty_id=subdivision.d_faculty_id))
    result.result_config.session.commit()

for specialization in specialization_postgress:
    result.result_config.session.add(
        result.Specialization_result(
            id=specialization.specialization_id,
            name=specialization.specialization_name,
            code=None,
            program_id=None))
    result.result_config.session.commit()

for student_group in student_group_postgress:
    if toyear(student_group.year) not in years_oracle:
        result.result_config.session.add(
            result.Year_result(year_name=toyear(student_group.year), startdate=datetime(2018, 9, 1),
                               enddate=datetime(2019, 9, 1)))
    if (student_group.group_subdivision not in subdivision_oracle) or (
            student_group.group_subdivision not in subdivisions_postgress):
        break
    else:
        result.result_config.session.add(
            result.Group_result(
                id=student_group.group_id,
                name=student_group.group_name,
                year_name=toyear(student_group.year),
                subdivision_name=student_group.group_subdivision,
                specialization_id=student_group.group_specialization,
                coursenumber=student_group.course_number
            )
        )
    result.result_config.session.commit()

maxPersonId = max(result.result_config.session.query(result.Person_result).all(), key=lambda x: x.id).id

for student in student_postgress:
    if student.group_id in result.result_config.session.query(result.Group_result).all():
        maxPersonId = maxPersonId + 1
        result_people[maxPersonId] = result.Person_result(
            id=maxPersonId,
            surname="Unknown",
            name=student.student_name,
            patronymic=None,
            dateofbirth=datetime(1900, 1, 1),
            placeofbirth="Unknown"
        )
        result.result_config.session.add(result_people[maxPersonId])
        result.result_config.session.commit()
        result.result_config.session.add(
            result.Student_result(
                id=student.student_id,
                person_id=maxPersonId,
                group_id=student.group_id,
                type_of_study=student.type_of_study,
                form_of_study=student.form_of_study,
                qualification=student.qualification
            )
        )

for semester in semester_postgress:
    if semester.sem_specialization_id in result.result_config.session.query(result.Specialization_result).all():
        result.result_config.session.add(
            result.Semester_result(
                id=semester.semester_id,
                semester_name=str(semester.semester_num),
                specialization_id=semester.sem_specialization_id))
        result.result_config.session.commit()

for subject in subject_postgress:
    result.result_config.session.add(
        result.Subject_result(
            name=subject.subject_name,
            ))
    result.result_config.session.commit()

for employee in employee_postgress:
    if employee.t_subdivision_id in result.result_config.session.query(result.Subdivision_result).all():
        maxPersonId = maxPersonId + 1
        result_people[maxPersonId] = result.Person_result(
            id=maxPersonId,
            surname="Unknown",
            name=employee.employee_name,
            patronymic=None,
            dateofbirth=datetime(1900, 1, 1),
            placeofbirth="Unknown"
        )
        result.result_config.session.add(result_people[maxPersonId])
        result.result_config.session.commit()
        result.result_config.session.add(
            result.Employee_result(
                id=employee.employee_id,
                person_id=maxPersonId,
                subdivision_name=str(employee.t_subdivision_id),
                position="Unknown",
                startdate=datetime(1900, 1, 1),
                enddate=datetime(1900, 1, 1)
            )
        )
        result.result_config.session.commit()

for sp in specialization_program_postgress:
    if sp.sp_subject_name in result.result_config.session.query(result.Subject_result).all() and sp.sp_semester_id in result.result_config.session.query(result.Semester_result).all() and sp.main_teacher in result.result_config.session.query(result.Employee_result).all():
        result.result_config.session.add(
            result.Specialization_program_result(
                id=sp.sp_id,
                year_value=sp.year,
                lectures=sp.lectures,
                practices=sp.practises,
                labs=sp.labs,
                control_type=sp.control_type,
                subject_name=sp.sp_subject_id,
                semester_id=sp.sp_semester_id,
                main_teacher=sp.main_teacher
            )
        )
        result.result_config.session.commit()

for student in students_collection:
    try:
        result.result_config.session.add(student)
        result.result_config.session.commit()
    except Exception:
        continue
