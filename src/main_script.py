from src.MongoScheme import MongoScheme
from src.PostgresScheme import PostgresScheme
from src.MySqlScheme import MySqlScheme
from src.OracleScheme import OracleScheme
from src.ResultScheme import ResultScheme


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
                                  qualification=student.qualification))
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
#mongo.drop_db()
#mongo.create_gen_db()

postgres = PostgresScheme('postgresql://postgres:postgres@localhost:5432/postgresdb')
#postgres.clear()
#postgres.generate_data()

mysql = MySqlScheme('mysql://root:root@localhost/sys')
#mysql.clear()
#mysql.generate_data(100, 100)

oracle = OracleScheme("oracle+cx_oracle://myschema:1234@localhost/orcl")
#oracle.clear()
#oracle.generate_data(100, 100)

result = ResultScheme('oracle+cx_oracle://newschema:1234@localhost/orcl')
result.clear()

persons_oracle = oracle.oracle_config.session.query(oracle.Person_oracle).all()
years_oracle = oracle.oracle_config.session.query(oracle.Year_oracle).all()
subdivision_oracle = oracle.oracle_config.session.query(oracle.Subdivision_oracle).all()
subjects_oracle = oracle.oracle_config.session.query(oracle.Subject_oracle).all()
programs_oracle = oracle.oracle_config.session.query(oracle.Program_oracle).all()
group_oracle = oracle.oracle_config.session.query(oracle.Group_oracle).all()
specialization_oracle = oracle.oracle_config.session.query(oracle.Specialization_oracle).all()

persons_mysql = mysql.my_sql_config.session.query(mysql.Person_mysql).all()
conferences_mysql = mysql.my_sql_config.session.query(mysql.Conference_mysql).all()
conference_info_mysql = mysql.my_sql_config.session.query(mysql.Conference_info_mysql)
projects_mysql = mysql.my_sql_config.session.query(mysql.Scientific_project_mysql).all()
publishers_mysql = mysql.my_sql_config.session.query(mysql.Publisher_mysql).all()

result_people = {}

result.clear()

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

maxEmployeeId = max(oracle.oracle_config.session.query(oracle.Employee_oracle).all(), key=lambda x: x.id).id

for person in persons_oracle:
    result_people[person.id] = result.Person_result(id=person.id,
                                                    surname=person.surname,
                                                    name=person.name,
                                                    patronymic=person.patronymic,
                                                    dateofbirth=person.date_of_birth,
                                                    placeofbirth=person.place_of_birth,
                                                    employee_collection=generateEmployeesFromOracle(person),
                                                    student_collection=generateStudentCollectionFromOracle(person))

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
                                                        authors_collection=original_person.authors_collection,
                                                        reading_list_collection=original_person.reading_list_collection,
                                                        conference_participants_collection=original_person.conference_participants_collection)

for person in result_people.values():
    result.result_config.session.add(person)
    result.result_config.session.commit()
