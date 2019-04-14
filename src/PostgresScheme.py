from src.Configuration import Configuration
from src.Util import generate_name_string
from src.Util import generate_person_name_string
from src.Util import random_date
from src.Util import postgres_date
from random import randrange
from datetime import datetime


class PostgresScheme:
    def __init__(self, url):
        self.postgres_config = Configuration(url, "_postgres")
        self.University_postgres = self.postgres_config.Base.classes.university
        self.Faculty_postgres = self.postgres_config.Base.classes.faculty
        self.Subdivision_postgres = self.postgres_config.Base.classes.subdivision
        self.Specialization_postgres = self.postgres_config.Base.classes.specialization
        self.Student_group_postgres = self.postgres_config.Base.classes.student_group
        self.Student_postgres = self.postgres_config.Base.classes.student
        self.Semester_postgres = self.postgres_config.Base.classes.semester
        self.Subject_postgres = self.postgres_config.Base.classes.subject
        self.Employee_postgres = self.postgres_config.Base.classes.employee
        self.Specialization_program_postgres = self.postgres_config.Base.classes.specialization_program
        self.Results_postgres = self.postgres_config.Base.classes.results
        self.id = 1

    def clear(self):
        self.postgres_config.session.query(self.Results_postgres).delete()
        self.postgres_config.session.query(self.Specialization_program_postgres).delete()
        self.postgres_config.session.query(self.Employee_postgres).delete()
        self.postgres_config.session.query(self.Subject_postgres).delete()
        self.postgres_config.session.query(self.Semester_postgres).delete()
        self.postgres_config.session.query(self.Student_postgres).delete()
        self.postgres_config.session.query(self.Student_group_postgres).delete()
        self.postgres_config.session.query(self.Specialization_postgres).delete()
        self.postgres_config.session.query(self.Subdivision_postgres).delete()
        self.postgres_config.session.query(self.Faculty_postgres).delete()
        self.postgres_config.session.query(self.University_postgres).delete()

    def gen_university(self):
        st = ["standart", "original"]
        university = self.University_postgres(university_id=self.id,
                                              university_name=generate_name_string("ITMO", 2),
                                              university_standart_type=st[randrange(len(st))])
        self.id = self.id + 1
        return university

    def gen_faculty(self, f_university_id):
        faculty = self.Faculty_postgres(faculty_id=self.id,
                                        faculty_name=generate_name_string("Faculty ", 12),
                                        f_university_id=f_university_id)
        self.id = self.id + 1
        return faculty

    def gen_subdivision(self, d_faculty_id):
        subdivision = self.Subdivision_postgres(subdivision_id=self.id,
                                                subdivision_name=generate_name_string("subdivision ", 12),
                                                d_faculty_id=d_faculty_id)
        self.id = self.id + 1
        return subdivision

    def gen_specialization(self):
        specialization = self.Specialization_postgres(specialization_id=self.id,
                                                      specialization_name=generate_name_string("spec ", 5),
                                                      )
        self.id = self.id + 1
        return specialization

    def gen_student_group(self, gr_subdivision, gr_specialization):
        group = self.Student_group_postgres(group_id=self.id,
                                            group_name=generate_name_string("14", 3),
                                            year=postgres_date(
                                                random_date(
                                                    datetime.strptime('01/01/1980 01:00 AM', '%m/%d/%Y %I:%M %p'),
                                                    datetime.strptime('01/01/2019 01:00 AM', '%m/%d/%Y %I:%M %p'))),
                                            group_subdivision=gr_subdivision,
                                            group_specialization=gr_specialization,
                                            course_number=randrange(4))
        self.id = self.id + 1
        return group

    def gen_student(self, stu_group_id):
        student = self.Student_postgres(student_id=self.id,
                                        student_name=generate_person_name_string(),
                                        group_id=stu_group_id)
        self.id = self.id + 1
        return student

    def gen_semester(self, sem_specialization_id):
        semester = self.Semester_postgres(semester_id=self.id,
                                          semester_num=randrange(1, 8),
                                          sem_specialization_id=sem_specialization_id)
        self.id = self.id + 1
        return semester

    def gen_subject(self):
        subject = self.Subject_postgres(subject_id=self.id,
                                        subject_name=generate_name_string("Foundations of ", 10))
        self.id = self.id +1
        return subject

    def gen_employee(self, t_subdivision_id):
        employee = self.Employee_postgres(employee_id=self.id,
                                          employee_name=generate_person_name_string(),
                                          t_subdivision_id=t_subdivision_id)
        self.id = self.id + 1
        return employee

    def gen_specialization_program(self, program_subject_id, program_semester_id, program_teacher):
        ctype = ["exam", "credit"]
        program = self.Specialization_program_postgres(sp_id=self.id,
                                                       year=postgres_date(
                                                           random_date(
                                                               datetime.strptime('01/01/1980 01:00 AM',
                                                                                 '%m/%d/%Y %I:%M %p'),
                                                               datetime.strptime('01/01/2019 01:00 AM',
                                                                                 '%m/%d/%Y %I:%M %p'))),
                                                       lectures=randrange(0, 20),
                                                       practises=randrange(0, 40),
                                                       labs=randrange(0, 20),
                                                       control_type=ctype[randrange(len(ctype))],
                                                       sp_subject_name=program_subject_id,
                                                       sp_semester_id=program_semester_id,
                                                       main_teacher=program_teacher)
        self.id = self.id + 1
        return program

    def gen_results(self, sc_teacher_id, sc_subject_id, sc_student_id, sc_semester_id):
        result = self.Results_postgres(result_id=self.id,
                                       sc_subject_name=sc_subject_id,
                                       mark=randrange(100),
                                       sc_student_id=sc_student_id,
                                       sc_teacher_id=sc_teacher_id,
                                       resultdate=postgres_date(random_date(
                                           datetime.strptime('01/01/2014 01:00 AM', '%m/%d/%Y %I:%M %p'),
                                           datetime.strptime('01/01/2019 01:00 AM', '%m/%d/%Y %I:%M %p'))))
        self.id = self.id + 1
        return result

    def generate_data(self):
        universities = []
        faculties = []
        subdivisions = []
        specializations = []
        student_groups = []
        students = []
        semesters = []
        subjects = []
        employees = []
        specialization_programs = []
        results = []
        tmp_university_id = self.id
        universities.append(self.gen_university())
        for f_r in range(10):
            tmp_faculty_id = self.id
            faculties.append(self.gen_faculty(tmp_university_id))
            for d_r in range(4):
                tmp_subdivision_id = self.id
                subdivisions.append(self.gen_subdivision(tmp_faculty_id))
                for emp_r in range(5):
                    tmp_employee_id = self.id
                    employees.append(self.gen_employee(tmp_subdivision_id))
        for spec_r in range(10):
            tmp_specialization_id = self.id
            specializations.append(self.gen_specialization())
            for gr_r in range(4):
                tmp_group_id = self.id
                student_groups.append(self.gen_student_group(tmp_subdivision_id,tmp_specialization_id))
                for stu_r in range(10):
                    tmp_student_id = self.id
                    students.append(self.gen_student(tmp_group_id))
            for sem_r in range(8):
                tmp_sem_id = self.id
                semesters.append(self.gen_semester(tmp_specialization_id))
                for sub_r in range(10):
                    subjects.append(self.gen_subject())
                    tmp_sub_id=subjects[-1].subject_name
                    for sp_r in range(5):
                        tmp_sp_id = self.id
                        specialization_programs.append(self.gen_specialization_program(tmp_sub_id,tmp_sem_id,tmp_employee_id))
                    for res_r in range(10):
                        results.append(self.gen_results(tmp_employee_id,tmp_sub_id,tmp_student_id,tmp_sem_id))
        self.postgres_config.session.add_all(universities)
        self.postgres_config.session.add_all(faculties)
        self.postgres_config.session.add_all(subdivisions)
        self.postgres_config.session.add_all(specializations)
        self.postgres_config.session.add_all(student_groups)
        self.postgres_config.session.add_all(students)
        self.postgres_config.session.add_all(semesters)
        #print(subjects)
        self.postgres_config.session.add_all(subjects)
        self.postgres_config.session.add_all(specialization_programs)
        self.postgres_config.session.add_all(employees)
        self.postgres_config.session.add_all(results)
        self.postgres_config.session.commit()
