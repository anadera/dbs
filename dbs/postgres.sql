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
	f_university_id integer,
	faculty_name          varchar(50) not null,
	foreign key (f_university_id) references university (university_id),
	unique (faculty_name, f_university_id)
);

create table department
(
	department_id         integer primary key,
	department_name       varchar(50) not null,
	d_faculty_id integer,
	foreign key (d_faculty_id) references faculty(faculty_id),
	unique (department_name, d_faculty_id)
);

create table major
(
	major_id            integer primary key,
	major_type    varchar(10),
	m_department_id integer,
	foreign key (m_department_id) references department(department_id),
	unique (major_type, m_department_id)
);

create table student
(
	student_id       integer primary key,
	student_name     varchar(50) not null,
	stu_major_id integer,
	foreign key (stu_major_id) references major(major_id),
	unique (student_id, student_name)
);

create table semester
(
	semester_id       integer primary key,
	semester_num      integer not null,
	sem_major_id integer,
	foreign key (sem_major_id) references major(major_id),
	unique (semester_num, sem_major_id)
);

create table subject
(
	subject_id       integer primary key,
	subject_name     varchar(50) not null,
	unique (subject_name)
);

create table subject_in_semester
(
	sis_id integer primary key,
	lectures     integer,
	practises    integer,
	labs         integer,
	control_type varchar(10),
	sis_subject_id integer,
	sis_semester_id integer,
	foreign key (sis_subject_id) references subject(subject_id),
	foreign key (sis_semester_id) references semester(semester_id),
	unique (sis_subject_id, sis_semester_id)
);

create table teacher
(
	teacher_id            integer primary key,
	teacher_name          varchar(50) not null,
	t_department_id integer,
	foreign key (t_department_id) references department(department_id),
	unique (teacher_name, t_department_id)
);

create table scores
(
	score_id integer primary key,
	score       integer,
	scoreDate   date,
	sc_teacher_id  integer,
	sc_subject_id integer,
	sc_student_id integer,
	sc_semester_id integer,
	foreign key (sc_teacher_id) references teacher (teacher_id),
	foreign key (sc_subject_id) references subject (subject_id),
	foreign key (sc_student_id) references student (student_id),
	foreign key (sc_semester_id) references semester (semester_id)  
);

create table teacher_subject
(
	t_sub_id integer primary key,
	t_sub_teacher_id integer,
	t_sub_subject_id integer,
	foreign key (t_sub_teacher_id) references teacher(teacher_id),
	foreign key (t_sub_subject_id) references subject(subject_id),
	unique (t_sub_teacher_id, t_sub_subject_id)
);

create table subject_major
(
	sub_m_id integer primary key,
	sub_m_subject_id integer,
	sub_m_major_id integer,
	foreign key (sub_m_subject_id) references subject(subject_id),
	foreign key (sub_m_major_id) references major(major_id),
	unique (sub_m_subject_id, sub_m_major_id)
);