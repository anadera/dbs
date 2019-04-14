create table university
(
	university_id integer primary key,
	university_name          varchar(50) not null,
	university_standart_type varchar(50),
	unique (university_name, university_standart_type)
);

create table faculty
(
	faculty_id    integer primary key,
	faculty_name          varchar(50) not null,
	f_university_id integer,
	foreign key (f_university_id) references university (university_id),
	unique (faculty_name, f_university_id)
);

create table subdivision
(
	subdivision_id         integer primary key,
	subdivision_name       varchar(50) not null,
	d_faculty_id integer,
	foreign key (d_faculty_id) references faculty(faculty_id),
	unique (subdivision_name, d_faculty_id)
);

create table specialization
(
	specialization_id            integer primary key,
	specialization_name    varchar(10)	,
	unique (specialization_id)
);

create table student_group
(
  group_id integer primary key,
  group_name varchar(10),
  year date,
  group_subdivision integer,
  group_specialization integer,
  course_number integer,
  foreign key(group_subdivision) references subdivision(subdivision_id),
  foreign key (group_specialization) references specialization(specialization_id),
  unique (group_id, group_name, year)
);

create table student
(
	student_id       integer primary key,
	group_id integer,
	student_name     varchar(50) not null,
	foreign key (group_id) references student_group(group_id),
	unique (student_id, student_name)
);

create table semester
(
	semester_id       integer primary key,
	semester_num      integer not null,
	sem_specialization_id integer,
	foreign key (sem_specialization_id) references specialization(specialization_id),
	unique (semester_id, semester_num, sem_specialization_id)
);

create table subject
(
  subject_id integer primary key,
	subject_name     varchar(50)
);

create table employee
(
	employee_id            integer primary key,
	employee_name          varchar(50) not null,
	t_subdivision_id integer,
	foreign key (t_subdivision_id) references subdivision(subdivision_id),
	unique (employee_id, employee_name, t_subdivision_id)
);

create table specialization_program
(
	sp_id integer primary key,
	year date,
	lectures     integer,
	practises    integer,
	labs         integer,
	control_type varchar(10),
	sp_subject_id integer,
	sp_semester_id integer,
	main_teacher integer,
	foreign key (sp_subject_id) references subject(subject_id),
	foreign key (sp_semester_id) references semester(semester_id),
	foreign key (main_teacher) references employee(employee_id),
	unique (sp_id,year, control_type, sp_subject_id, sp_semester_id)
);

create table results
(
	result_id integer primary key,
	sc_subject_id integer,
	mark      integer,
	sc_student_id integer,
	sc_teacher_id  integer,
	resultDate   date,
	foreign key (sc_teacher_id) references employee (employee_id),
	foreign key (sc_subject_id) references subject (subject_id),
	foreign key (sc_student_id) references student (student_id),
	unique (result_id, sc_subject_id,mark,sc_student_id,sc_teacher_id,resultDate)
);