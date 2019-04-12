CREATE TABLE `job_position` (
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`name`)
);

CREATE TABLE `person` (
  `id` int(11) NOT NULL,
  `full_name` varchar(100) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  `position_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `full_name` (`full_name`,`birth_date`),
  CONSTRAINT `person_ibfk_1` FOREIGN KEY (`position_name`) REFERENCES `job_position` (`name`)
);

CREATE TABLE `scientific_project` (
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`name`)
);

CREATE TABLE `project_member` (
  `id` int(11) NOT NULL,
  `project_name` varchar(100) DEFAULT NULL,
  `member_id` int(11) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `project_name` (`project_name`,`member_id`,`start_date`),
  CONSTRAINT `project_member_ibfk_1` FOREIGN KEY (`project_name`) REFERENCES `scientific_project` (`name`),
  CONSTRAINT `project_member_ibfk_2` FOREIGN KEY (`member_id`) REFERENCES `person` (`id`)
);

CREATE TABLE `publisher` (
  `id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `p_type` varchar(10) DEFAULT NULL,
  `p_language` varchar(20) DEFAULT NULL,
  `date_of_publication` date DEFAULT NULL,
  `location` varchar(20) DEFAULT NULL,
  `size` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`,`p_type`,`date_of_publication`)
);

CREATE TABLE `publication` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `p_type` varchar(10) DEFAULT NULL,
  `citation_index` int(11) DEFAULT NULL,
  `publisher_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`,`p_type`),
  CONSTRAINT `publication_ibfk_1` FOREIGN KEY (`publisher_id`) REFERENCES `publisher` (`id`)
);

CREATE TABLE `authors` (
  `id` int(11) NOT NULL,
  `publication_id` int(11) DEFAULT NULL,
  `person_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `publication_id` (`publication_id`,`person_id`),
  CONSTRAINT `authors_ibfk_1` FOREIGN KEY (`publication_id`) REFERENCES `publication` (`id`),
  CONSTRAINT `authors_ibfk_2` FOREIGN KEY (`person_id`) REFERENCES `person` (`id`)
);

CREATE TABLE `conference` (
  `name` varchar(200) NOT NULL,
  PRIMARY KEY (`name`)
);

CREATE TABLE `conference_info` (
  `id` int(11) NOT NULL,
  `conference_name` varchar(200) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `place` varchar(200) DEFAULT NULL,
  `publisher_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `start_date` (`start_date`,`conference_name`),
  CONSTRAINT `conference_info_ibfk_1` FOREIGN KEY (`publisher_id`) REFERENCES `publisher` (`id`)
);

CREATE TABLE `participant_of_conference` (
  `id` int(11) NOT NULL,
  `person_id` int(11) DEFAULT NULL,
  `conference_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `person_id` (`person_id`,`conference_id`),
  CONSTRAINT `participant_of_conference_ibfk_1` FOREIGN KEY (`person_id`) REFERENCES `person` (`id`),
  CONSTRAINT `participant_of_conference_ibfk_2` FOREIGN KEY (`conference_id`) REFERENCES `conference_info` (`id`)
);

CREATE TABLE `reading_list` (
  `id` int(11) NOT NULL,
  `publisher_id` int(11) DEFAULT NULL,
  `person_id` int(11) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `publisher_id` (`publisher_id`,`person_id`,`start_date`),
  KEY `person_id` (`person_id`),
  CONSTRAINT `reading_list_ibfk_1` FOREIGN KEY (`publisher_id`) REFERENCES `publisher` (`id`),
  CONSTRAINT `reading_list_ibfk_2` FOREIGN KEY (`person_id`) REFERENCES `person` (`id`)
);
