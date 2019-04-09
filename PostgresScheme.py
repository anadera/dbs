from Configuration import Configuration
from Util import generate_name_string
from Util import generate_person_name_string
from Util import random_date
from Util import postgres_date
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
        self.Subject_in_semester_postgres = self.postgres_config.Base.classes.subject_in_semester
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
        st = ["standart", "original"]
        university = self.University_postgres(university_id=self.id,
                                               university_name=generate_name_string("ITMO",2),
                                               university_standart_type=st[randrange(len(st))])
        self.id = self.id + 1
        return university

    def gen_faculty(self, f_university_id):
        faculty = self.Faculty_postgres(faculty_id=self.id,
                                         faculty_name=generate_name_string("Faculty ", 12),
                                         f_university_id=f_university_id)
        self.id = self.id + 1
        return faculty

    def gen_department(self, d_faculty_id):
        department = self.Department_postgres(department_id=self.id,
                                               department_name=generate_name_string("Department ", 12),
                                               d_faculty_id=d_faculty_id)
        self.id = self.id + 1
        return department

    def gen_major(self, m_department_id):
        major = self.Major_postgres(major_id=self.id,
                                     major_type=generate_name_string("type ", 5),
                                     m_department_id=m_department_id)
        self.id = self.id + 1
        return major

    def gen_student(self, stu_major_id):
        student = self.Student_postgres(student_id=self.id,
                                         student_name=generate_person_name_string(),
                                         stu_major_id=stu_major_id)
        self.id = self.id + 1
        return student

    def gen_semester(self, sem_major_id):
        semester = self.Semester_postgres(semester_id=self.id,
                                           semester_num=randrange(1, 8),
                                           sem_major_id=sem_major_id)
        self.id = self.id + 1
        return semester

    def gen_subject(self):
        subject = self.Subject_postgres(subject_id=self.id,
                                         subject_name=generate_name_string("Foundations of ", 10))
        self.id = self.id + 1
        return subject

    def gen_subject_in_semester(self, sis_subject_id, sis_semester_id):
        ctype = ["exam", "credit"]
        subject_in_semester = self.Subject_in_semester_postgres(sis_id=self.id,
                                                                 lectures=randrange(0, 20),
                                                                 practises=randrange(0, 40),
                                                                 labs=randrange(0, 20),
                                                                 control_type=ctype[randrange(len(ctype))],
                                                                 sis_subject_id=sis_subject_id,
                                                                 sis_semester_id=sis_semester_id)
        self.id = self.id + 1
        return subject_in_semester

    def gen_teacher(self, t_department_id):
        teacher = self.Teacher_postgres(teacher_id=self.id,
                                         teacher_name=generate_person_name_string(),
                                         t_department_id=t_department_id)
        self.id = self.id + 1
        return teacher

    def gen_scores(self, sc_teacher_id, sc_subject_id, sc_student_id, sc_semester_id):
        score = self.Scores_postgres(score_id=self.id,
                                      score=randrange(100),
                                      scoredate=postgres_date(random_date(
                                          datetime.strptime('01/01/2014 01:00 AM', '%m/%d/%Y %I:%M %p'),
                                          datetime.strptime('01/01/2019 01:00 AM', '%m/%d/%Y %I:%M %p'))),
                                      sc_teacher_id=sc_teacher_id,
                                      sc_subject_id=sc_subject_id,
                                      sc_student_id=sc_student_id,
                                      sc_semester_id=sc_semester_id)
        self.id = self.id + 1
        return score

    def gen_teacher_subject(self, t_sub_teacher_id, t_sub_subject_id):
        teacher_subject = self.Teacher_subject_postgres(t_sub_id=self.id,
                                                         t_sub_teacher_id=t_sub_teacher_id,
                                                         t_sub_subject_id=t_sub_subject_id)
        self.id = self.id + 1
        return teacher_subject

    def gen_subject_major(self, sub_m_subject_id, sub_m_major_id):
        subject_major = self.Subject_major_postgres(sub_m_id=self.id,
                                                     sub_m_subject_id=sub_m_subject_id,
                                                     sub_m_major_id=sub_m_major_id)
        self.id = self.id + 1
        return subject_major

    def generate_data(self):
        universities = []
        faculties = []
        departments = []
        majors = []
        students = []
        semesters = []
        subjects = []
        subjects_in_semester = []
        teachers = []
        scores = []
        teachers_subject = []
        subjects_major = []
        for u_r in range(2):
            tmp_university_id = self.id
            universities.append(self.gen_university())
            for f_r in range(10):
                tmp_faculty_id = self.id
                faculties.append(self.gen_faculty(tmp_university_id))
                for d_r in range(4):
                    tmp_deprtment_id = self.id
                    departments.append(self.gen_department(tmp_faculty_id))
                    for m_r in range(5):
                        tmp_major_id = self.id
                        majors.append(self.gen_major(tmp_deprtment_id))
                        for stu_r in range(5):
                            tmp_student_id = self.id
                            students.append(self.gen_student(tmp_major_id))
                        for sem_r in range(8):
                            tmp_semester_id = self.id
                            semesters.append(self.gen_semester(tmp_major_id))
                        for sub_r in range(5):
                            tmp_subject_id = self.id
                            subjects.append(self.gen_subject())
                            subjects_major.append(self.gen_subject_major(tmp_subject_id, tmp_major_id))
                        for sis_r in range(8):
                            tmp_sis_id = self.id
                            subjects_in_semester.append(self.gen_subject_in_semester(tmp_subject_id, tmp_semester_id))
                    for t_r in range(10):
                        tmp_teacher_id = self.id
                        teachers.append(self.gen_teacher(tmp_deprtment_id))
                        for sc_r in range(2):
                            scores.append(
                                self.gen_scores(tmp_teacher_id, tmp_subject_id, tmp_student_id, tmp_semester_id))
                        teachers_subject.append(self.gen_teacher_subject(tmp_teacher_id, tmp_subject_id))

        self.postgres_config.session.add_all(universities)
        self.postgres_config.session.add_all(faculties)
        self.postgres_config.session.add_all(departments)
        self.postgres_config.session.add_all(majors)
        self.postgres_config.session.add_all(students)
        self.postgres_config.session.add_all(semesters)
        self.postgres_config.session.add_all(subjects)
        self.postgres_config.session.add_all(subjects_in_semester)
        self.postgres_config.session.add_all(teachers)
        self.postgres_config.session.add_all(scores)
        self.postgres_config.session.add_all(teachers_subject)
        self.postgres_config.session.add_all(subjects_major)
        self.postgres_config.session.commit()
