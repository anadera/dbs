from Configuration import Configuration
from Util import generate_name_string
from Util import generate_person_name_string
from Util import random_date
from random import randrange
from datetime import datetime


class PostgresScheme:
    def __init__(self, url):
        self.postgres_config = Configuration(url, "_postgres")
        self.University_postgres = self.postgres_config.Base.classes.university
        self.Faculty_postgres = self.postgres_config.Base.classes.faculty
        self.Department_postgres = self.postgres_config.Base.classes.department
        self.Major_postgres = self.postgres_config.Base.classes.major
        self.Student_postgres = self.postgres_config.Base.classes.student
        self.Semester_postgres = self.postgres_config.Base.classes.semester
        self.Subject_postgres = self.postgres_config.Base.classes.subject
        self.Subject_in_semester = self.postgres_config.Base.classes.subject_in_semester
        self.Teacher_postgres = self.postgres_config.Base.classes.teacher
        self.Teacher_subject_postgres = self.postgres_config.Base.classes.teacher_subject
        self.Subject_major_postgres = self.postgres_config.Base.classes.subject_major
        self.Scores_postgres = self.postgres_config.Base.classes.scores
        self.id = 1

    def clear(self):
        self.postgres_config.session.query(self.University_postgres).delete()
        self.postgres_config.session.query(self.Faculty_postgres).delete()
        self.postgres_config.session.query(self.Department_postgres).delete()
        self.postgres_config.session.query(self.Student_postgres).delete()
        self.postgres_config.session.query(self.Major_postgres).delete()
        self.postgres_config.session.query(self.Subject_postgres).delete()
        self.postgres_config.session.query(self.Semester_postgres).delete()
        self.postgres_config.session.query(self.Subject_in_semester_postgres).delete()
        self.postgres_config.session.query(self.Subject_major_postgres).delete()
        self.postgres_config.session.query(self.Teacher_postgres).delete()
        self.postgres_config.session.query(self.Teacher_subject_postgres).delete()
        self.postgres_config.session.query(self.Scores_postgres).delete()

    def gen_university(self):
        university = [self.University_postgres(university_id=self.id,
                                               university_name="ITMO",
                                               university_standart_type="standart")]
        self.id = self.id + 1
        return university

    def gen_faculty(self, f_university_id):
        faculty = [self.Faculty_postgres(faculty_id=self.id,
                                         faculty_name=generate_name_string("Faculty ", 12),
                                         f_university_id=f_university_id)]
        self.id = self.id + 1
        return faculty

    def gen_department(self, d_faculty_id):
        department = [self.Department_postgres(department_id=self.id,
                                               department_name=generate_name_string("Department ", 12),
                                               d_faculty_id=d_faculty_id)]
        self.id = self.id + 1
        return department

    def gen_major(self, m_department_id):
        major = [self.Major_postgres(major_id=self.id,
                                     major_type=generate_name_string("type ", 5),
                                     m_department_id=m_department_id)]
        self.id = self.id + 1
        return major

    def gen_student(self, stu_major_id):
        student = [self.Student_postgres(student_id=self.id,
                                         student_name=generate_person_name_string(),
                                         stu_major_id=stu_major_id)]
        self.id = self.id + 1
        return student

    def gen_semester(self,sem_major_id):
        semester = [self.Semester_postgres(semester_id=self.id,
                                           semester_num=randrange(1, 8),
                                           sem_major_id=sem_major_id)]
        self.id = self.id + 1
        return semester

    def gen_subject(self):
        subject = [self.Subject_postgres(subject_id=self.id,
                                         subject_name=generate_name_string("Foundations of ", 10))]
        self.id = self.id + 1
        return subject

    def gen_subject_in_semester(self, sis_subject_id, sis_semester_id):
        ctype = ["exam", "credit"]
        subject_in_semester = [self.Subject_in_semester(sis_id=self.id,
                                                        lectures=randrange(0, 20),
                                                        practices=randrange(0, 40),
                                                        labs=randrange(0, 20),
                                                        control_type=ctype[randrange(len(ctype))],
                                                        sis_subject_id=sis_subject_id,
                                                        sis_semester_id=sis_semester_id)]
        self.id = self.id + 1
        return subject_in_semester

    def gen_teacher(self, t_department_id):
        teacher = [self.Teacher_postgres(teacher_id=self.id,
                                         teacher_name=generate_person_name_string(),
                                         t_department_id=t_department_id)]
        self.id = self.id + 1
        return teacher

    def gen_scores(self, sc_teacher_id, sc_subject_id, sc_student_id, sc_semester_id):
        score = [self.Scores_postgres(score_id=self.id,
                                      score=randrange(100),
                                      scoreDate=random_date(datetime.strptime('01/01/2014 01:00 AM', '%m/%d/%Y %I:%M %p'),
                                                              datetime.strptime('01/01/2019 01:00 AM', '%m/%d/%Y %I:%M %p')),
                                      sc_teacher_id=sc_teacher_id,
                                      sc_subject_id=sc_subject_id,
                                      sc_student_id=sc_student_id,
                                      sc_semester_id=sc_semester_id)]
        self.id = self.id + 1
        return score

    def gen_teacher_subject(self, t_sub_teacher_id, t_sub_subject_id):
        teacher_subject = [self.Teacher_subject_postgres(t_sub_id=self.id,
                                                         t_sub_teacher_id=t_sub_teacher_id,
                                                         t_sub_subject_id=t_sub_subject_id)]
        self.id = self + 1
        return teacher_subject

    def gen_subject_major(self, sub_m_subject_id, sub_m_major_id):
        subject_major = [self.Subject_major_postgres(sub_m_id=self.id,
                                                     sub_m_subject_id=sub_m_subject_id,
                                                     sub_m_major_id=sub_m_major_id)]
        self.id = self.id + 1
        return subject_major
