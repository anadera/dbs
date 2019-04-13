import datetime
import random

from src.Configuration import Configuration
from src.Util import generate_string, generateRandomDate


class OracleScheme:
    def __init__(self, url):
        self.oracle_config = Configuration(url, "_oracle")
        self.Person_oracle = self.oracle_config.Base.classes.person
        self.Year_oracle = self.oracle_config.Base.classes.year
        self.Program_oracle = self.oracle_config.Base.classes.program
        self.Mark_oracle = self.oracle_config.Base.classes.mark
        self.Subject_oracle = self.oracle_config.Base.classes.subject
        self.Subdivision_oracle = self.oracle_config.Base.classes.subdivision
        self.Employee_oracle = self.oracle_config.Base.classes.employee
        self.Group_oracle = self.oracle_config.Base.classes.group_info
        self.Specialization_oracle = self.oracle_config.Base.classes.specialization
        self.Group_Schedule_oracle = self.oracle_config.Base.classes.group_schedule
        self.Schedule_oracle = self.oracle_config.Base.classes.schedule_info
        self.Student_oracle = self.oracle_config.Base.classes.student
        self.Result_oracle = self.oracle_config.Base.classes.result
        self.id = 1

    def clear(self):
        self.oracle_config.session.query(self.Result_oracle).delete()
        self.oracle_config.session.query(self.Group_Schedule_oracle).delete()
        self.oracle_config.session.query(self.Schedule_oracle).delete()
        self.oracle_config.session.query(self.Student_oracle).delete()
        self.oracle_config.session.query(self.Employee_oracle).delete()
        self.oracle_config.session.query(self.Group_oracle).delete()
        self.oracle_config.session.query(self.Person_oracle).delete()
        self.oracle_config.session.query(self.Year_oracle).delete()
        self.oracle_config.session.query(self.Subject_oracle).delete()
        self.oracle_config.session.query(self.Specialization_oracle).delete()
        self.oracle_config.session.query(self.Program_oracle).delete()
        self.oracle_config.session.query(self.Mark_oracle).delete()
        self.oracle_config.session.query(self.Subdivision_oracle).delete()

    def generate_data(self, start_person_id, other_id):
        self.id = other_id
        subdivisions = []
        for i in range(5):
            subdivisions.append(self.Subdivision_oracle(name=generate_string(20),
                                                        type="f"))

        marks = [self.Mark_oracle(name=5, letter="A"), self.Mark_oracle(name=4, letter="B"),
                 self.Mark_oracle(name=3, letter="C")]

        subjects = []
        for i in range(5):
            subjects.append(self.Subject_oracle(name=generate_string(10)))

        program = []
        for i in range(5):
            program.append(self.Program_oracle(id=self.id, name=generate_string(10), code=generate_string(6)))
            self.id = self.id + 1

        specializations = []
        for i in range(10):
            specializations.append(
                self.Specialization_oracle(id=self.id, name=generate_string(10), code=generate_string(6),
                                           program_id=random.choice(program).id))
            self.id = self.id + 1

        years = [self.Year_oracle(name="2018", startdate=datetime.datetime(2018, 9, 1),
                                  enddate=datetime.datetime(2019, 5, 31)),
                 self.Year_oracle(name="2017", startdate=datetime.datetime(2017, 9, 1),
                                  enddate=datetime.datetime(2018, 5, 31)),
                 self.Year_oracle(name="2016", startdate=datetime.datetime(2016, 9, 1),
                                  enddate=datetime.datetime(2017, 5, 31))]

        groups = []
        for i in range(20):
            groups.append(
                self.Group_oracle(id=self.id, name=generate_string(4), year_name=random.choice(years).name,
                                  subdivision_name=random.choice(subdivisions).name,
                                  specialization_id=random.choice(specializations).id,
                                  coursenumber=random.randint(1, 6)))
            self.id = self.id + 1

        persons = []
        for i in range(100):
            persons.append(
                self.Person_oracle(id=start_person_id, surname=generate_string(10), name=generate_string(10),
                                   patronymic=generate_string(10),
                                   date_of_birth=generateRandomDate(),
                                   place_of_birth=generate_string(20)))
            start_person_id = start_person_id + 1

        employees = []
        for i in range(20):
            employees.append(
                self.Employee_oracle(id=self.id, person_id=random.choice(persons).id,
                                     subdivision_name=random.choice(subdivisions).name,
                                     position=generate_string(8),
                                     startdate=generateRandomDate(),
                                     enddate=generateRandomDate()))
            self.id = self.id + 1

        students = []
        for i in range(100):
            students.append(
                self.Student_oracle(id=self.id, person_id=random.choice(persons).id,
                                    group_id=random.choice(groups).id,
                                    type_of_study="t" + random.randint(1, 2).__str__(),
                                    form_of_study="i",
                                    qualification="bachelor"))
            self.id = self.id + 1

        schedule = []
        group_schedule = []
        for i in range(20):
            date = generateRandomDate()
            schedule.append(self.Schedule_oracle(id=self.id, subject_name=random.choice(subjects).name,
                                                 teacher_id=random.choice(employees).id,
                                                 day_of_week=random.randint(1, 7),
                                                 start_time=date, end_time=date + datetime.timedelta(hours=2),
                                                 type_of_week=random.choice(["e", "o"]),
                                                 room=random.randint(1000, 5000)))
            group_schedule.append(self.Group_Schedule_oracle(id=self.id, group_id=random.choice(groups).id,
                                                             schedule_id=self.id))
            self.id = self.id + 1

        result = []
        for i in range(200):
            result.append(self.Result_oracle(id=self.id, subject_name=random.choice(subjects).name,
                                             mark_value=random.choice(marks).name,
                                             student_id=random.choice(students).id))
            self.id = self.id + 1

            self.oracle_config.session.add_all(years)
            self.oracle_config.session.add_all(subdivisions)
            self.oracle_config.session.add_all(subjects)
            self.oracle_config.session.add_all(program)
            self.oracle_config.session.add_all(specializations)
            self.oracle_config.session.add_all(marks)
            self.oracle_config.session.add_all(persons)
            self.oracle_config.session.add_all(students)
            self.oracle_config.session.add_all(groups)
            self.oracle_config.session.add_all(employees)
            self.oracle_config.session.add_all(result)
            self.oracle_config.session.add_all(schedule)
            self.oracle_config.session.add_all(group_schedule)
            self.oracle_config.session.commit()
