import random

from src.Configuration import Configuration
from src.Util import generate_string, generateRandomDate


class MySqlScheme:
    def __init__(self, url):
        self.my_sql_config = Configuration(url, "_my_sql")
        self.Person_mysql = self.my_sql_config.Base.classes.person
        self.Scientific_project_mysql = self.my_sql_config.Base.classes.scientific_project
        self.Conference_mysql = self.my_sql_config.Base.classes.conference
        self.Publisher_mysql = self.my_sql_config.Base.classes.publisher
        self.Conference_info_mysql = self.my_sql_config.Base.classes.conference_info
        self.Publication_mysql = self.my_sql_config.Base.classes.publication
        self.Job_mysql = self.my_sql_config.Base.classes.job_position
        self.Authors_mysql = self.my_sql_config.Base.classes.authors
        self.Conference_participants_mysql = self.my_sql_config.Base.classes.participant_of_conference
        self.Reading_list_mysql = self.my_sql_config.Base.classes.reading_list
        self.Project_member_mysql = self.my_sql_config.Base.classes.project_member
        self.id = 1

    def clear(self):
        self.my_sql_config.session.query(self.Reading_list_mysql).delete()
        self.my_sql_config.session.query(self.Authors_mysql).delete()
        self.my_sql_config.session.query(self.Publication_mysql).delete()
        self.my_sql_config.session.query(self.Conference_participants_mysql).delete()
        self.my_sql_config.session.query(self.Conference_info_mysql).delete()
        self.my_sql_config.session.query(self.Project_member_mysql).delete()
        self.my_sql_config.session.query(self.Scientific_project_mysql).delete()
        self.my_sql_config.session.query(self.Conference_mysql).delete()
        self.my_sql_config.session.query(self.Publisher_mysql).delete()
        self.my_sql_config.session.query(self.Person_mysql).delete()

    def generatePublicationInfo(self, publisher_id):
        publicationCollection = []
        for i in range(10):
            publicationCollection.append(
                self.Publication_mysql(id=self.id, name=generate_string(15), p_type="type",
                                       citation_index=random.randint(0, 10),
                                       publisher_id=publisher_id))
            self.id = self.id + 1
        return publicationCollection

    def generateConferenceInfo(self, conference_name, publishers):
        conferenceInfoCollection = []
        for i in range(3):
            conferenceInfoCollection.append(
                self.Conference_info_mysql(id=self.id, conference_name=conference_name, start_date=generateRandomDate(),
                                           end_date=generateRandomDate(),
                                           place=generate_string(10),
                                           publisher_id=random.choice(publishers).id))
            self.id = self.id + 1
        return conferenceInfoCollection

    def generateAuthors(self, person_id, publishers, size):
        authors = []
        for i in range(size):
            random_publisher_publications = random.choice(publishers).publication_collection
            authors.append(self.Authors_mysql(id=self.id,
                                              publication_id=random.choice(random_publisher_publications).id,
                                              person_id=person_id))
            self.id = self.id + 1
        return authors

    def generateConferenceParticipants(self, person_id, conferences, size):
        participants = []
        for i in range(size):
            random_conference = random.choice(conferences)
            participants.append(self.Conference_participants_mysql(id=self.id,
                                                                   conference_id=random_conference.id,
                                                                   person_id=person_id))
            self.id = self.id + 1
        return participants

    def generateReadingList(self, person_id, publishers, size):
        list = []
        for i in range(size):
            random_publisher = random.choice(publishers)
            list.append(self.Reading_list_mysql(id=self.id, publisher_id=random_publisher.id,
                                                person_id=person_id, start_date=generateRandomDate(),
                                                end_date=generateRandomDate()))
            self.id = self.id + 1
        return list

    def generateProjectMembers(self, person_id, projects):
        members = [self.Project_member_mysql(id=self.id, project_name=random.choice(projects).name,
                                             member_id=person_id, start_date=generateRandomDate(),
                                             end_date=generateRandomDate())]
        self.id = self.id + 1
        return members

    def generate_data(self, start_person_id, other_id):
        self.id = other_id
        publishers = []
        for i in range(5):
            publishers.append(self.Publisher_mysql(id=self.id,
                                                   name=generate_string(20),
                                                   p_type="type",
                                                   p_language="eng",
                                                   date_of_publication=generateRandomDate(),
                                                   location=generate_string(10),
                                                   size=20,
                                                   publication_collection=self.generatePublicationInfo(self.id)))
            self.id = self.id + 1

        projects = []
        for i in range(5):
            projects.append(self.Scientific_project_mysql(name=generate_string(15)))

        job_position = []
        for i in range(5):
            job_position.append(self.Job_mysql(name=generate_string(10)))

        conferences_names = []
        conferences = []
        for i in range(5):
            name = generate_string(20)
            conferences_names.append(self.Conference_mysql(name=name))
            conferences.extend(self.generateConferenceInfo(name, publishers))

        persons = []
        for i in range(100):
            persons.append(
                self.Person_mysql(id=start_person_id, full_name=generate_string(8) + " " + generate_string(7),
                                  birth_date=generateRandomDate(),
                                  authors_collection=self.generateAuthors(start_person_id, publishers, 1),
                                  position_name = random.choice(job_position).name,
                                  reading_list_collection=self.generateReadingList(start_person_id, publishers,
                                                                                   1),
                                  participant_of_conference_collection=self.generateConferenceParticipants(
                                      start_person_id,
                                      conferences,
                                      1),
                                  project_member_collection=self.generateProjectMembers(start_person_id, projects)))
            start_person_id = start_person_id + 1

        self.my_sql_config.session.add_all(publishers)
        self.my_sql_config.session.add_all(conferences_names)
        self.my_sql_config.session.add_all(conferences)
        self.my_sql_config.session.add_all(job_position)
        self.my_sql_config.session.add_all(projects)
        self.my_sql_config.session.add_all(persons)
        self.my_sql_config.session.commit()