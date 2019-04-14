from src.Configuration import Configuration


class ResultScheme:
    def __init__(self, url):
        self.result_config = Configuration(url, "_result")
        self.Subdivision_result = self.result_config.Base.classes.subdivision
        self.Person_result = self.result_config.Base.classes.person
        self.Employee_result = self.result_config.Base.classes.employee
        self.Student_result = self.result_config.Base.classes.student
        self.Year_result = self.result_config.Base.classes.year
        self.Group_result = self.result_config.Base.classes.group_info
        self.Program_result = self.result_config.Base.classes.program
        self.Specialization_result = self.result_config.Base.classes.specialization
        self.Schedule_result = self.result_config.Base.classes.schedule
        self.Mark_result = self.result_config.Base.classes.mark
        self.Scientific_project_result = self.result_config.Base.classes.scientific_project
        self.Conference_result = self.result_config.Base.classes.conference
        self.Conference_info_result = self.result_config.Base.classes.conference_info
        self.Publisher_result = self.result_config.Base.classes.publisher
        self.Publication_result = self.result_config.Base.classes.publication
        self.Reading_list_result = self.result_config.Base.classes.reading_list
        self.Subject_result = self.result_config.Base.classes.subject
        self.Project_member_result = self.result_config.Base.classes.project_members
        self.Authors_result = self.result_config.Base.classes.authors
        self.Conference_participants = self.result_config.Base.classes.conference_participants
        #self.Group_schedule_result = self.result_config.Base.classes.group_schedule
        self.Campus_result = self.result_config.Base.classes.campus
        self.Faculty_result = self.result_config.Base.classes.faculty
        self.Payment_result = self.result_config.Base.classes.payment
        self.Results_result = self.result_config.Base.classes.results
        self.Room_result = self.result_config.Base.classes.room
        self.Sanitization_result = self.result_config.Base.classes.sanitization
        self.Semester_result = self.result_config.Base.classes.semester
        self.Specialization_program_result = self.result_config.Base.classes.specialization_program
        self.Teenant_result = self.result_config.Base.classes.teenant
        self.University_result = self.result_config.Base.classes.university
        self.Visit_result = self.result_config.Base.classes.visit



    # It would be better to find new info in 4 database and update only new ones in the result db,
    # but this needs quite more code and we don't have enougth time and people in the team, so I suggest to simply clear  result db
    # and upload data again (we don't have to upload a lot of data to the database in the lab, so it won't need much time)
    def clear(self):
        self.result_config.session.query(self.Reading_list_result).delete()
        self.result_config.session.query(self.Authors_result).delete()
        self.result_config.session.query(self.Publication_result).delete()
        self.result_config.session.query(self.Conference_participants).delete()
        self.result_config.session.query(self.Conference_info_result).delete()
        self.result_config.session.query(self.Project_member_result).delete()
        self.result_config.session.query(self.Scientific_project_result).delete()
        #self.result_config.session.query(self.Group_Schedule_result).delete()
        self.result_config.session.query(self.Schedule_result).delete()
        self.result_config.session.query(self.Conference_result).delete()
        self.result_config.session.query(self.Publisher_result).delete()
        self.result_config.session.query(self.Student_result).delete()
        self.result_config.session.query(self.Employee_result).delete()
        self.result_config.session.query(self.Group_result).delete()
        self.result_config.session.query(self.Person_result).delete()
        self.result_config.session.query(self.Year_result).delete()
        self.result_config.session.query(self.Subject_result).delete()
        self.result_config.session.query(self.Specialization_result).delete()
        self.result_config.session.query(self.Program_result).delete()
        self.result_config.session.query(self.Mark_result).delete()
        self.result_config.session.query(self.Subdivision_result).delete()
        self.result_config.session.query(self.Payment_result).delete()
        self.result_config.session.query(self.Visit_result).delete()
        self.result_config.session.query(self.Teenant_result).delete()
        self.result_config.session.query(self.Sanitization_result).delete()
        self.result_config.session.query(self.Room_result).delete()
        self.result_config.session.query(self.Campus_result).delete()
        self.result_config.session.query(self.Results_result).delete()
        self.result_config.session.query(self.Specialization_program_result).delete()
        self.result_config.session.query(self.Semester_result).delete()
        self.result_config.session.query(self.Faculty_result).delete()
        self.result_config.session.query(self.University_result).delete()


