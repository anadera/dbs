from Configuration import Configuration


class PostgresScheme:
    def __init__(self, url, naming_symbol):
        self.postgres_config = Configuration(url, naming_symbol)
        self.University_postgres = self.postgres_config.Base.classes.university
        self.Faculty_postgres = self.postgres_config.Base.classes.faculty
        self.Department_postgres = self.postgres_config.Base.classes.department
        self.Student_postgres = self.postgres_config.Base.classes.student
        self.Major_postgres = self.postgres_config.Base.classes.major
        self.Subject_postgres = self.postgres_config.Base.classes.subject
        self.Semester_postgres = self.postgres_config.Base.classes.semester
        self.Subject_in_semester_postgres = self.postgres_config.Base.classes.subject_in_semester
        self.Subject_major_postgres = self.postgres_config.Base.classes.subject_major
        self.Teacher_postgres = self.postgres_config.Base.classes.teacher
        self.Teacher_subject_postgres = self.postgres_config.Base.classes.teacher_subject
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
