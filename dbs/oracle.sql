create table person (
    id integer primary key,
    surname varchar(50) not null,
    name varchar(50) not null,
    patronymic varchar(50),
    date_of_birth date not null,
    place_of_birth varchar(50),
    unique(surname, name, patronymic, date_of_birth, place_of_birth)
);


create table year (
    name varchar(4) primary key,
    startDate date,
    endDate date
);

create table program (
    id integer primary key,
    name varchar(50),
    code varchar(25)
);

create table specialization (
    id integer primary key,
    name varchar(50),
    code varchar(50),
    program_id references program(id)
);

create table subdivision (
    name varchar(50) primary key,
    type varchar(1)
);

create table group_info (
    id integer primary key,
    name varchar(50),
    year_name references year(name),
    subdivision_name varchar(50) references subdivision(name),
    specialization_id integer references specialization(id),
    courseNumber integer
);

create table student (
    id integer primary key,
    person_id integer references person(id),
    group_id integer references group_info(id),
    type_of_study varchar(2),
    form_of_study varchar(1),
    qualification varchar(10)
);

create table employee (
    id integer primary key,
    person_id integer references person(id),
    subdivision_name varchar(50) references subdivision(name),
    position varchar(20),
    startDate date,
    endDate date,
    unique(person_id, subdivision_name, position, startDate)
);

create table subject (
    name varchar(100) primary key
);

create table schedule_info (
    id integer primary key,
    subject_name varchar(100) references subject(name),
    teacher_id integer references employee(id),
    day_of_week integer not null,
    start_time date,
    end_time date,
    type_of_week varchar(2),
    room varchar(5)
);

create table group_schedule (
    id integer primary key,
    group_id integer references group_info(id),
    schedule_id integer references schedule_info(id)
);

create table mark (
    name integer primary key,
    letter varchar(1)
);

create table result (
    id integer primary key,
    subject_name  varchar(100) references subject(name),
    mark_value integer references mark(name),
    student_id references student(id)
);

commit;