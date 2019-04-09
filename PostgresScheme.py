from Configuration import Configuration
from Util import generate_string


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

    def generateUniversity(self, university_id):
        universityCollection = []
        universityCollection.append(self.University_postgres(id=self.id, name="ITMO", standart_type="standart"))
        self.id = self.id + 1
        return universityCollection

    def generate_data(self, start_person_id, other_id):
        self.id = other_id
        self.postgres_config.session.add(self.University_postgres(university_id=start_person_id, university_name="ITMO", university_standart_type="st"))
        self.postgres_config.session.commit()
        #start_person_id = start_person_id + 1
        #self.postgres_config.session.add_all(universities)

