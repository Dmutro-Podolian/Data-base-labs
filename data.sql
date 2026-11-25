-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Projects` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `project_name` VARCHAR(45) NOT NULL,
  `description` VARCHAR(100) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `mydb`.`ProjectContacts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `full_name` VARCHAR(100) NOT NULL,
  `email` VARCHAR(45) NULL,
  `phone` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `mydb`.`ReqruitmentLevel` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `level_name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `mydb`.`Vacancies` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NOT NULL,
  `description` LONGTEXT NOT NULL,
  `Projects_id` INT NOT NULL,
  `status` VARCHAR(20) NULL,
  `ProjectContacts_id` INT NOT NULL,
  `ReqruitmentLevel_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Vacancies_Projects_idx` (`Projects_id` ASC) VISIBLE,
  INDEX `fk_Vacancies_ProjectContacts1_idx` (`ProjectContacts_id` ASC) VISIBLE,
  INDEX `fk_Vacancies_ReqruitmentLevel1_idx` (`ReqruitmentLevel_id` ASC) VISIBLE,
  INDEX `idx_vacancies_status` (`status` ASC) VISIBLE,
  CONSTRAINT `fk_Vacancies_Projects`
    FOREIGN KEY (`Projects_id`)
    REFERENCES `mydb`.`Projects` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Vacancies_ProjectContacts1`
    FOREIGN KEY (`ProjectContacts_id`)
    REFERENCES `mydb`.`ProjectContacts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Vacancies_ReqruitmentLevel1`
    FOREIGN KEY (`ReqruitmentLevel_id`)
    REFERENCES `mydb`.`ReqruitmentLevel` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `mydb`.`TechnicalLevel` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `level_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `mydb`.`EnglishLevel` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `level_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `mydb`.`Candidates` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `ReqruitmentLevel_id` INT NOT NULL,
  `TechnicalLevel_id` INT NOT NULL,
  `EnglishLevel_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Candidates_ReqruitmentLevel1_idx` (`ReqruitmentLevel_id` ASC) VISIBLE,
  INDEX `fk_Candidates_TechnicalLevel1_idx` (`TechnicalLevel_id` ASC) VISIBLE,
  INDEX `fk_Candidates_EnglishLevel1_idx` (`EnglishLevel_id` ASC) VISIBLE,
  INDEX `idx_candidates_email` (`email` ASC) VISIBLE,
  CONSTRAINT `fk_Candidates_ReqruitmentLevel1`
    FOREIGN KEY (`ReqruitmentLevel_id`)
    REFERENCES `mydb`.`ReqruitmentLevel` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Candidates_TechnicalLevel1`
    FOREIGN KEY (`TechnicalLevel_id`)
    REFERENCES `mydb`.`TechnicalLevel` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Candidates_EnglishLevel1`
    FOREIGN KEY (`EnglishLevel_id`)
    REFERENCES `mydb`.`EnglishLevel` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `mydb`.`CandidateVacansies` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Vacancies_id` INT NOT NULL,
  `Candidates_id` INT NOT NULL,
  `application_date` DATE NOT NULL,
  `status` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_CandidateVacansies_Vacancies1_idx` (`Vacancies_id` ASC) VISIBLE,
  INDEX `fk_CandidateVacansies_Candidates1_idx` (`Candidates_id` ASC) VISIBLE,
  CONSTRAINT `fk_CandidateVacansies_Vacancies1`
    FOREIGN KEY (`Vacancies_id`)
    REFERENCES `mydb`.`Vacancies` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_CandidateVacansies_Candidates1`
    FOREIGN KEY (`Candidates_id`)
    REFERENCES `mydb`.`Candidates` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `mydb`.`Interviews` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `interview_date` DATETIME(6) NOT NULL,
  `interviwer_name` VARCHAR(45) NULL,
  `CandidateVacansies_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Interviews_CandidateVacansies1_idx` (`CandidateVacansies_id` ASC) VISIBLE,
  CONSTRAINT `fk_Interviews_CandidateVacansies1`
    FOREIGN KEY (`CandidateVacansies_id`)
    REFERENCES `mydb`.`CandidateVacansies` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `mydb`.`InterviewResult` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `area_name` VARCHAR(45) NOT NULL,
  `comment` VARCHAR(100) NULL,
  `score_level` VARCHAR(45) NOT NULL,
  `Interviews_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_InterviewResult_Interviews1_idx` (`Interviews_id` ASC) VISIBLE,
  CONSTRAINT `fk_InterviewResult_Interviews1`
    FOREIGN KEY (`Interviews_id`)
    REFERENCES `mydb`.`Interviews` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `mydb`.`Projects_has_ProjectContacts` (
  `Projects_id` INT NOT NULL,
  `ProjectContacts_id` INT NOT NULL,
  PRIMARY KEY (`Projects_id`, `ProjectContacts_id`),
  INDEX `fk_Projects_has_ProjectContacts_ProjectContacts1_idx` (`ProjectContacts_id` ASC) VISIBLE,
  INDEX `fk_Projects_has_ProjectContacts_Projects1_idx` (`Projects_id` ASC) VISIBLE,
  CONSTRAINT `fk_Projects_has_ProjectContacts_Projects1`
    FOREIGN KEY (`Projects_id`)
    REFERENCES `mydb`.`Projects` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Projects_has_ProjectContacts_ProjectContacts1`
    FOREIGN KEY (`ProjectContacts_id`)
    REFERENCES `mydb`.`ProjectContacts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE TABLE `InterviewResult`;
TRUNCATE TABLE `Interviews`;
TRUNCATE TABLE `CandidateVacansies`;
TRUNCATE TABLE `Candidates`;
TRUNCATE TABLE `EnglishLevel`;
TRUNCATE TABLE `TechnicalLevel`;
TRUNCATE TABLE `Vacancies`;
TRUNCATE TABLE `ReqruitmentLevel`;
TRUNCATE TABLE `Projects_has_ProjectContacts`;
TRUNCATE TABLE `ProjectContacts`;
TRUNCATE TABLE `Projects`;

SET FOREIGN_KEY_CHECKS = 1;

INSERT INTO `ReqruitmentLevel` (`id`, `level_name`) VALUES
(1, 'Low Priority'), (2, 'Medium Priority'), (3, 'High Priority'), (4, 'Critical'), (5, 'Standard'),
(6, 'Urgent'), (7, 'Pool'), (8, 'VIP'), (9, 'Internal'), (10, 'External'),
(11, 'Executive'), (12, 'Contract'), (13, 'Temporary'), (14, 'Internship'), (15, 'Reserved');

INSERT INTO `TechnicalLevel` (`id`, `level_name`) VALUES
(1, 'Trainee'), (2, 'Junior'), (3, 'Junior+'), (4, 'Middle-'), (5, 'Middle'),
(6, 'Middle+'), (7, 'Senior-'), (8, 'Senior'), (9, 'Lead'), (10, 'Architect'),
(11, 'Principal'), (12, 'Specialist'), (13, 'Expert'), (14, 'Consultant'), (15, 'Master');

INSERT INTO `EnglishLevel` (`id`, `level_name`) VALUES
(1, 'A1 Beginner'), (2, 'A2 Elementary'), (3, 'B1 Intermediate'), (4, 'B2 Upper-Intermediate'), (5, 'C1 Advanced'),
(6, 'C2 Mastery'), (7, 'None'), (8, 'Basic'), (9, 'Fluent'), (10, 'Native'),
(11, 'Pre-Intermediate'), (12, 'Upper-Elementary'), (13, 'Professional'), (14, 'Bilingual'), (15, 'Elementary Plus');

INSERT INTO `Projects` (`id`, `project_name`, `description`) VALUES
(1, 'Alpha CRM', 'Customer relationship system development'),
(2, 'Beta ERP', 'Enterprise resource planning software'),
(3, 'Gamma Shop', 'Online retail marketplace platform'),
(4, 'Delta Health', 'Medical data tracking application'),
(5, 'Omega Pay', 'Secure financial transaction gateway'),
(6, 'Sigma Fleet', 'Logistics and warehouse management'),
(7, 'Zeta Game', 'Multiplayer backend services'),
(8, 'Theta Edu', 'E-learning management system'),
(9, 'Lambda AI', 'Machine learning data pipeline'),
(10, 'Kappa Cloud', 'Cloud storage administration tool'),
(11, 'Atlas GIS', 'Geospatial mapping and analysis'),
(12, 'Nexus IoT', 'Smart home sensor data collector'),
(13, 'Vortex HR', 'Human resources automation system'),
(14, 'Phoenix Sec', 'Cybersecurity auditing dashboard'),
(15, 'Titan Log', 'Supply chain optimization engine');

INSERT INTO `ProjectContacts` (`id`, `full_name`, `email`, `phone`) VALUES
(1, 'Ivan Franko', 'franko@alpha.com', '+380501112233'),
(2, 'Lesya Ukrayinka', 'ukrayinka@beta.com', '+380502223344'),
(3, 'Taras Shevchenko', 'shevchenko@gamma.com', '+380503334455'),
(4, 'Stepan Bandera', 'bandera@delta.com', '+380504445566'),
(5, 'Bohdan Khmel', 'khmel@omega.com', '+380505556677'),
(6, 'Mykhailo Hrushevsky', 'hrushevsky@sigma.com', '+380506667788'),
(7, 'Hryhoriy Skovoroda', 'skovoroda@zeta.com', '+380507778899'),
(8, 'Volodymyr Vynnychenko', 'vynnychenko@theta.com', '+380508889900'),
(9, 'Symon Petliura', 'petliura@lambda.com', '+380509990011'),
(10, 'Vyacheslav Chornovil', 'chornovil@kappa.com', '+380500001122'),
(11, 'Pavlo Chubynsky', 'chubynsky@atlas.com', '+380501234455'),
(12, 'Mykola Lysenko', 'lysenko@nexus.com', '+380502345566'),
(13, 'Ivan Mazepa', 'mazepa@vortex.com', '+380503456677'),
(14, 'Pylyp Orlyk', 'orlyk@phoenix.com', '+380504567788'),
(15, 'Dmytro Vyshnevetsky', 'vyshnevetsky@titan.com', '+380505678899');

INSERT INTO `Candidates` (`id`, `first_name`, `last_name`, `email`, `ReqruitmentLevel_id`, `TechnicalLevel_id`, `EnglishLevel_id`) VALUES
(1, 'Vitalii', 'Shurhot', 'vitalii.shurhot@gmail.com', 3, 5, 4),
(2, 'Nazarii', 'Vislak', 'vislak825@gmail.com', 3, 8, 5),
(3, 'Valentyna', 'Melnychuk', 'valia@ukr.net', 2, 2, 3),
(4, 'Andrii', 'Pavelchak', 'apavelchak@gmail.com', 4, 6, 4),
(5, 'Olena', 'Koval', 'koval.olena@gmail.com', 1, 3, 2),
(6, 'Dmytro', 'Bondarenko', 'd.bond@ukr.net', 5, 8, 6),
(7, 'Yuliia', 'Shevchuk', 'yuliia.sh@gmail.com', 2, 4, 3),
(8, 'Maksym', 'Kryvenko', 'maks.kryv@gmail.com', 4, 7, 5),
(9, 'Sofiia', 'Tkachenko', 'sofiia.t@gmail.com', 1, 2, 3),
(10, 'Pavlo', 'Rudenko', 'pavlo.rud@gmail.com', 5, 9, 6),
(11, 'Kateryna', 'Boyko', 'katya.boyko@gmail.com', 3, 5, 4),
(12, 'Oleh', 'Savchenko', 'oleh.sav@ukr.net', 2, 3, 3),
(13, 'Iryna', 'Hontar', 'iryna.hontar@gmail.com', 4, 8, 5),
(14, 'Yevhen', 'Kravchuk', 'yevhen.krav@gmail.com', 1, 4, 2),
(15, 'Svitlana', 'Moroz', 'svitlana.moroz@gmail.com', 5, 10, 9);

INSERT INTO `Vacancies` (`id`, `title`, `description`, `Projects_id`, `status`, `ProjectContacts_id`, `ReqruitmentLevel_id`) VALUES
(1, 'Python Dev', 'Backend Django development', 1, 'Open', 1, 3),
(2, 'Java Engineer', 'Enterprise backend services', 2, 'Open', 2, 4),
(3, 'React Frontend', 'UI marketplace development', 3, 'Closed', 3, 2),
(4, 'Data Analyst', 'Healthcare metrics processing', 4, 'Open', 4, 3),
(5, 'Security Spec', 'Fintech encryption testing', 5, 'Open', 5, 5),
(6, 'Logistics Lead', 'Fleet tracking software', 6, 'Open', 6, 2),
(7, 'Unity GameDev', 'Gameplay scripting mechanics', 7, 'Open', 7, 4),
(8, 'UI/UX Designer', 'Portal redesign research', 8, 'Closed', 8, 2),
(9, 'AI Researcher', 'Machine learning model tuning', 9, 'Open', 9, 5),
(10, 'Cloud Architect', 'AWS infrastructure management', 10, 'Open', 10, 5),
(11, 'GIS Specialist', 'Mapping software features', 11, 'Open', 11, 3),
(12, 'IoT Developer', 'Sensor communication protocol', 12, 'Open', 12, 4),
(13, 'HR Automation Engineer', 'Internal tools development', 13, 'Closed', 13, 2),
(14, 'Cyber Security Auditor', 'Vulnerability assessment', 14, 'Open', 14, 5),
(15, 'Supply Chain Dev', 'Optimization algorithm integration', 15, 'Open', 15, 3);

INSERT INTO `CandidateVacansies` (`id`, `Vacancies_id`, `Candidates_id`, `application_date`, `status`) VALUES
(1, 1, 1, '2026-03-01', 'Applied'),
(2, 2, 2, '2026-03-02', 'Interviewing'),
(3, 3, 3, '2026-03-03', 'Rejected'),
(4, 4, 4, '2026-03-04', 'Offered'),
(5, 5, 5, '2026-03-05', 'Applied'),
(6, 6, 6, '2026-03-06', 'Hired'),
(7, 7, 7, '2026-03-07', 'Interviewing'),
(8, 8, 8, '2026-03-08', 'Applied'),
(9, 9, 9, '2026-03-09', 'Rejected'),
(10, 10, 10, '2026-03-10', 'Hired'),
(11, 11, 11, '2026-03-11', 'Applied'),
(12, 12, 12, '2026-03-12', 'Interviewing'),
(13, 13, 13, '2026-03-13', 'Rejected'),
(14, 14, 14, '2026-03-14', 'Offered'),
(15, 15, 15, '2026-03-15', 'Hired');

INSERT INTO `Interviews` (`id`, `interview_date`, `interviwer_name`, `CandidateVacansies_id`) VALUES
(1, '2026-03-05 10:00:00', 'Ivan Franko', 1),
(2, '2026-03-06 12:00:00', 'Lesya Ukrayinka', 2),
(3, '2026-03-07 14:00:00', 'Taras Shevchenko', 3),
(4, '2026-03-08 11:00:00', 'Stepan Bandera', 4),
(5, '2026-03-09 15:00:00', 'Bohdan Khmel', 5),
(6, '2026-03-10 16:00:00', 'Mykhailo Hrushevsky', 6),
(7, '2026-03-11 09:30:00', 'Hryhoriy Skovoroda', 7),
(8, '2026-03-12 13:00:00', 'Volodymyr Vynnychenko', 8),
(9, '2026-03-13 14:30:00', 'Symon Petliura', 9),
(10, '2026-03-14 10:30:00', 'Vyacheslav Chornovil', 10),
(11, '2026-03-15 11:30:00', 'Pavlo Chubynsky', 11),
(12, '2026-03-16 12:30:00', 'Mykola Lysenko', 12),
(13, '2026-03-17 14:00:00', 'Ivan Mazepa', 13),
(14, '2026-03-18 15:30:00', 'Pylyp Orlyk', 14),
(15, '2026-03-19 16:30:00', 'Dmytro Vyshnevetsky', 15);

INSERT INTO `InterviewResult` (`id`, `area_name`, `comment`, `score_level`, `Interviews_id`) VALUES
(1, 'Python Core', 'Good understanding of OOP principles', 'High', 1),
(2, 'Spring Framework', 'Deep knowledge of enterprise patterns', 'Expert', 2),
(3, 'JavaScript/React', 'Needs improvement in state management', 'Medium', 3),
(4, 'SQL & Data', 'Excellent performance on aggregation queries', 'High', 4),
(5, 'Cybersecurity', 'Solid grasp of security protocols', 'Good', 5),
(6, 'Architecture', 'Great system design skills', 'Expert', 6),
(7, 'C# / Unity', 'Strong math background and physics logic', 'High', 7),
(8, 'UI/UX Principles', 'Good portfolio, minor workflow flaws', 'Medium', 8),
(9, 'Machine Learning', 'Strong theoretical foundation', 'High', 9),
(10, 'DevOps / AWS', 'Extensive production experience', 'Expert', 10),
(11, 'GIS Mapping', 'Familiar with spatial databases', 'High', 11),
(12, 'Embedded C', 'Good low-level understanding', 'Good', 12),
(13, 'HR Analytics', 'Strong communication skills', 'Medium', 13),
(14, 'Penetration Testing', 'Found critical vulnerabilities', 'Expert', 14),
(15, 'Algorithms', 'Clean and optimized code structure', 'Expert', 15);

INSERT INTO `Projects_has_ProjectContacts` (`Projects_id`, `ProjectContacts_id`) VALUES
(1, 1), (2, 2), (3, 3), (4, 4), (5, 5),
(6, 6), (7, 7), (8, 8), (9, 9), (10, 10),
(11, 11), (12, 12), (13, 13), (14, 14), (15, 15);