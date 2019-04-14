CREATE TABLE Authors (
  id             number(10),
  publication_id number(10) NOT NULL,
  person_id      number(10) NOT NULL,
  PRIMARY KEY (id),
  unique(publication_id, person_id));

CREATE TABLE Campus (
  id       number(10),
  location varchar2(100) NOT NULL,
  rooms_total number(10),
  PRIMARY KEY (id),
  UNIQUE(location));

CREATE TABLE Conference_info (
  id              number(10),
  conference_name varchar2(100) NOT NULL,
  publisher_id    number(10),
  endDate         date NOT NULL,
  startDate       date NOT NULL,
  place           varchar2(100) NOT NULL,
  unique(conference_name, publisher_id, startDate, place),
  PRIMARY KEY (id));

CREATE TABLE Conference (
  name varchar2(100) NOT NULL,
  PRIMARY KEY (name));

CREATE TABLE Conference_participants (
  id            number(10),
  person_id     number(10) NOT NULL,
  conference_id number(10) NOT NULL,
  PRIMARY KEY (id),
  unique(person_id, conference_id));

CREATE TABLE Employee (
  id        number(10),
  person_id number(10) NOT NULL,
  subdivision_name varchar2(25) ,
  position  varchar2(20),
  startDate date,
  endDate   date,
  PRIMARY KEY (id),
  unique(person_id, subdivision_name));


CREATE TABLE Faculty (
  id            number(10),
  name          varchar2(50) NOT NULL,
  university_id number(10) NOT NULL,
  type          varchar2(10),
  PRIMARY KEY (id),
  unique(name, university_id));

CREATE TABLE Group_info (
  id                 number(10),
  name               varchar2(25) NOT NULL,
  year_name          number(10) NOT NULL,
  subdivision_name        varchar2(25) NOT NULL,
  specialization_id number(10) NOT NULL,
  courseNumber       number(10) NOT NULL,
  PRIMARY KEY (id),
  unique(name, year_name));

CREATE TABLE Group_Schedule (
  group_id      number(10) NOT NULL ,
  schedule_id number(10) NOT NULL ,
  unique(group_id, schedule_id));


CREATE TABLE Mark (
  mark_value   number(5),
  letter varchar2(1) NOT NULL,
  PRIMARY KEY (mark_value));

CREATE TABLE Payment (
  id                  number(10),
  teenant_id          number(10) NOT NULL ,
  date_of_transaction date NOT NULL ,
  sum                 float(10) NOT NULL ,
  PRIMARY KEY (id),
  unique(teenant_id, date_of_transaction, sum));

CREATE TABLE Person (
  id           number(10),
  surname      varchar2(25) NOT NULL ,
  name         varchar2(25) NOT NULL ,
  patronymic   varchar2(25) ,
  dateOfBirth  date NOT NULL ,
  placeOfBirth varchar2(25) NOT NULL ,
  PRIMARY KEY (id),
  unique(surname, name, patronymic, dateOfBirth, placeOfBirth));

CREATE TABLE Program (
  id   number(10),
  name varchar2(25) NOT NULL,
  code varchar2(25) NOT NULL UNIQUE,
  PRIMARY KEY (id));


CREATE TABLE Project_members (
  id           number(10),
  project_name varchar2(100) NOT NULL ,
  member_id    number(10) NOT NULL ,
  PRIMARY KEY (id),
  unique(project_name, member_id));


CREATE TABLE Publication (
  id                       number(10),
  name                     varchar2(100) NOT NULL ,
  type                     varchar2(5) NOT NULL ,
  citation_index			 number(10),
  publisher_id             number(10) NOT NULL ,
  PRIMARY KEY (id),
  unique(name, type, publisher_id));

CREATE TABLE Publisher (
  id                  number(10),
  name                varchar2(100) NOT NULL ,
  type                varchar2(5) NOT NULL ,
  language            varchar2(15) NOT NULL ,
  date_of_publication date NOT NULL ,
  place               varchar2(25) NOT NULL ,
  n_size      		  number(10) NOT NULL ,
  PRIMARY KEY (id));

CREATE TABLE Reading_list (
  id           number(10),
  publisher_id number(10) NOT NULL ,
  person_id    number(10) NOT NULL ,
  start_date   date NOT NULL ,
  end_date     date,
  PRIMARY KEY (id),
  unique(publisher_id, person_id, start_date));

CREATE TABLE Results (
  id           number(10),
  subject_name number(10) NOT NULL ,
  mark_value         number(5) NOT NULL ,
  student_id   number(10) NOT NULL ,
  teacher_id   number(10) NOT NULL ,
  mark_date    date NOT NULL ,
  PRIMARY KEY (id),
  unique(subject_name, mark_value, student_id, teacher_id, mark_date));

CREATE TABLE Room (
  id              number(10),
  room_number     number(10) NOT NULL ,
  campus_id       number(10) NOT NULL ,
  number_of_beds number(10) NOT NULL ,
  PRIMARY KEY (id),
  unique(room_number, campus_id, number_of_beds));

CREATE TABLE Sanitization (
  id                number(10),
  bed_bugs          varchar2(1) NOT NULL ,
  date_of_procedure date NOT NULL ,
  room_id           number(10) NOT NULL,
  PRIMARY KEY (id),
  unique(bed_bugs, date_of_procedure, room_id));

CREATE TABLE Schedule (
  id           number(10),
  subject_name varchar(25) NOT NULL ,
  teacher_id   number(10) NOT NULL ,
  dayOfWeek    number(7) NOT NULL ,
  startTime    timestamp(7) NOT NULL ,
  endTime      timestamp(7) NOT NULL,
  typeOfWeek   char(1),
  room         varchar2(5) NOT NULL,
  PRIMARY KEY (id),
  unique(subject_name, teacher_id, dayOfWeek, startTime));

CREATE TABLE Scientific_project (
  name varchar2(100) NOT NULL,
  PRIMARY KEY (name));

CREATE TABLE Semester (
  id                number(10),
  semester_name     varchar2(20) NOT NULL ,
  specialization_id number(10) NOT NULL ,
  PRIMARY KEY (id),
  unique(semester_name, specialization_id));

CREATE TABLE Specialization (
  id         number(10),
  name       varchar2(25) NOT NULL,
  code       varchar2(20) UNIQUE,
  program_id number(10),
  PRIMARY KEY (id));

CREATE TABLE Specialization_program (
  id           number(10) ,
  year_value         number(10) NOT NULL ,
  lectures     number(10) NOT NULL ,
  practices    number(10) NOT NULL ,
  labs         number(10) NOT NULL ,
  control_type varchar2(2) NOT NULL ,
  subject_name varchar2(255) NOT NULL ,
  semester_id  number(10) NOT NULL ,
  main_teacher number(10) NOT NULL,
  PRIMARY KEY (id),
  unique(year_value, lectures, practices, labs, control_type, subject_name, semester_id));

CREATE TABLE Student (
  id            number(10),
  person_id     number(10) NOT NULL ,
  group_id      number(10) NOT NULL ,
  type_of_study varchar2(10),
  form_of_study varchar2(10),
  qualification varchar2(2),
  PRIMARY KEY (id),
  unique(person_id, group_id));

CREATE TABLE Subdivision (
  name       varchar2(25) NOT NULL,
  faculty_id number(10),
  PRIMARY KEY (name));

CREATE TABLE Subject (
  name varchar2(255) NOT NULL,
  PRIMARY KEY (name));

CREATE TABLE Teenant (
  id         number(10),
  person_id  number(10) NOT NULL ,
  room_num    number(10) NOT NULL ,
  start_date date NOT NULL ,
  end_date   date,
  PRIMARY KEY (id),
  unique(person_id, room_num, start_date));

CREATE TABLE University (
  id                      number(10),
  name                    varchar2(100) NOT NULL ,
  standart_type 		  varchar(10) NOT NULL ,
  PRIMARY KEY (id),
  unique(name, standart_type));

CREATE TABLE Visit (
  id         number(10),
  teenant_id number(10) NOT NULL ,
  start_date date NOT NULL ,
  end_date   date,
  PRIMARY KEY (id),
  unique(teenant_id, start_date));

CREATE TABLE Year (
  year_name      number(10),
  startDate date,
  endDate   date,
  PRIMARY KEY (year_name));



ALTER TABLE Employee ADD CONSTRAINT FKEmployee455086 FOREIGN KEY (person_id) REFERENCES Person (id);
ALTER TABLE Employee ADD CONSTRAINT FKEmployee280037 FOREIGN KEY (subdivision_name) REFERENCES Subdivision (name);
ALTER TABLE Student ADD CONSTRAINT FKStudent152773 FOREIGN KEY (person_id) REFERENCES Person (id);
ALTER TABLE Student ADD CONSTRAINT FKStudent949208 FOREIGN KEY (group_id) REFERENCES Group_info (id);
ALTER TABLE Group_info ADD CONSTRAINT FKGroup531654 FOREIGN KEY (subdivision_name) REFERENCES Subdivision (name);
ALTER TABLE Group_info ADD CONSTRAINT FKGroup238021 FOREIGN KEY (year_name) REFERENCES Year (year_name);
ALTER TABLE Group_info ADD CONSTRAINT FKGroup413568 FOREIGN KEY (specialization_id) REFERENCES Specialization (id);
ALTER TABLE Schedule ADD CONSTRAINT FKSchedule537344 FOREIGN KEY (teacher_id) REFERENCES Employee (id);
ALTER TABLE Group_Schedule ADD CONSTRAINT FKGroup_Sche247036 FOREIGN KEY (group_id) REFERENCES Group_info (id);
ALTER TABLE Group_Schedule ADD CONSTRAINT FKGroup_Sche29284 FOREIGN KEY (schedule_info) REFERENCES Schedule (id);
ALTER TABLE Specialization ADD CONSTRAINT FKSpecializa702220 FOREIGN KEY (program_id) REFERENCES Program (id);
ALTER TABLE Project_members ADD CONSTRAINT FKProject_me705906 FOREIGN KEY (project_name) REFERENCES Scintific_project (name);
ALTER TABLE Project_members ADD CONSTRAINT FKProject_me550842 FOREIGN KEY (member_id) REFERENCES Employee (id);
ALTER TABLE Conference_info ADD CONSTRAINT FKConfefrenc99924 FOREIGN KEY (conference_name) REFERENCES Conference (name);
ALTER TABLE Conference_info ADD CONSTRAINT FKConfefrenc813049 FOREIGN KEY (publisher_id) REFERENCES Publisher (id);
ALTER TABLE Conference_participants ADD CONSTRAINT FKConference910230 FOREIGN KEY (conference_id) REFERENCES Conference_info (id);
ALTER TABLE Conference_participants ADD CONSTRAINT FKConference940320 FOREIGN KEY (person_id) REFERENCES Person (id);
ALTER TABLE Publication ADD CONSTRAINT FKPublicatio106751 FOREIGN KEY (publisher_id) REFERENCES Publisher (id);
ALTER TABLE Reading_list ADD CONSTRAINT FKReading_li351228 FOREIGN KEY (publisher_id) REFERENCES Publisher (id);
ALTER TABLE Reading_list ADD CONSTRAINT FKReading_li445003 FOREIGN KEY (person_id) REFERENCES Person (id);
ALTER TABLE Authors ADD CONSTRAINT FKAuthors974269 FOREIGN KEY (publication_id) REFERENCES Publication (id);
ALTER TABLE Authors ADD CONSTRAINT FKAuthors514087 FOREIGN KEY (person_id) REFERENCES Person (id);
ALTER TABLE Room ADD CONSTRAINT FKRoom887829 FOREIGN KEY (campus_id) REFERENCES Campus (id);
ALTER TABLE Teenant ADD CONSTRAINT FKTeenant542541 FOREIGN KEY (room_num) REFERENCES Room (room_number);
ALTER TABLE Teenant ADD CONSTRAINT FKTeenant568183 FOREIGN KEY (person_id) REFERENCES Person (id);
ALTER TABLE Sanitization ADD CONSTRAINT FKSanitzatio786620 FOREIGN KEY (room_id) REFERENCES Room (id);
ALTER TABLE Payment ADD CONSTRAINT FKPayment431193 FOREIGN KEY (teenant_id) REFERENCES Teenant (id);
ALTER TABLE Visit ADD CONSTRAINT FKVisit739183 FOREIGN KEY (teenant_id) REFERENCES Teenant (id);
ALTER TABLE Faculty ADD CONSTRAINT FKFaculty474039 FOREIGN KEY (university_id) REFERENCES University (id);
ALTER TABLE Subdivision ADD CONSTRAINT FKSubdivisio586637 FOREIGN KEY (faculty_id) REFERENCES Faculty (id);
ALTER TABLE Semester ADD CONSTRAINT FKSemester101142 FOREIGN KEY (specialization_id) REFERENCES Specialization (id);
ALTER TABLE Specialization_program ADD CONSTRAINT FKSpecializa221690 FOREIGN KEY (Semester_id) REFERENCES Semester (id);
ALTER TABLE Specialization_program ADD CONSTRAINT FKSpecializa914592 FOREIGN KEY (year_value) REFERENCES Year (year_name);
ALTER TABLE Specialization_program ADD CONSTRAINT FKSpecializa477402 FOREIGN KEY (subject_name) REFERENCES Subject (name);
ALTER TABLE Specialization_program ADD CONSTRAINT FKSpecializa636672 FOREIGN KEY (main_teacher) REFERENCES Employee (id);
ALTER TABLE Results ADD CONSTRAINT FKResults28773 FOREIGN KEY (teacher_id) REFERENCES Employee (id);
ALTER TABLE Results ADD CONSTRAINT FKResults587217 FOREIGN KEY (subject_name) REFERENCES Specialization_program (id);
ALTER TABLE Results ADD CONSTRAINT FKResults689878 FOREIGN KEY (mark_value) REFERENCES Mark (mark_value);
ALTER TABLE Results ADD CONSTRAINT FKResults291286 FOREIGN KEY (student_id) REFERENCES Student (id);
ALTER TABLE Schedule ADD CONSTRAINT FKSchedule78646 FOREIGN KEY (subject_name) REFERENCES Subject (name);
