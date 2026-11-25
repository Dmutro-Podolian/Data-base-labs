from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String, Table, Text, func
from sqlalchemy.orm import foreign, relationship

from app.utils.db import Base

projects_contacts = Table(
    "Projects_has_ProjectContacts",
    Base.metadata,
    Column("Projects_id", Integer, ForeignKey("Projects.id"), primary_key=True),
    Column("ProjectContacts_id", Integer, ForeignKey("ProjectContacts.id"), primary_key=True),
)


class Project(Base):
    __tablename__ = "Projects"

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_name = Column(String(45), nullable=False)
    description = Column(Text, nullable=True)

    vacancies = relationship("Vacancy", backref="project_ref", cascade="all, delete-orphan")
    contacts = relationship("ProjectContact", secondary=projects_contacts, backref="projects")
    notes = relationship(
        "ProjectNote",
        backref="project_ref",
        primaryjoin="Project.id == foreign(ProjectNote.project_id)",
    )

    def put_into_dto(self):
        return {
            "id": self.id,
            "project_name": self.project_name,
            "description": self.description,
        }


class ProjectContact(Base):
    __tablename__ = "ProjectContacts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(45), nullable=True)
    phone = Column(String(45), nullable=True)

    def put_into_dto(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "email": self.email,
            "phone": self.phone,
        }


class ReqruitmentLevel(Base):
    __tablename__ = "ReqruitmentLevel"

    id = Column(Integer, primary_key=True, autoincrement=True)
    level_name = Column(String(45), nullable=True)

    def put_into_dto(self):
        return {
            "id": self.id,
            "level_name": self.level_name,
        }


class TechnicalLevel(Base):
    __tablename__ = "TechnicalLevel"

    id = Column(Integer, primary_key=True, autoincrement=True)
    level_name = Column(String(45), nullable=False)

    def put_into_dto(self):
        return {
            "id": self.id,
            "level_name": self.level_name,
        }


class EnglishLevel(Base):
    __tablename__ = "EnglishLevel"

    id = Column(Integer, primary_key=True, autoincrement=True)
    level_name = Column(String(45), nullable=False)

    def put_into_dto(self):
        return {
            "id": self.id,
            "level_name": self.level_name,
        }


class Vacancy(Base):
    __tablename__ = "Vacancies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(45), nullable=False)
    description = Column(Text, nullable=False)
    Projects_id = Column(Integer, ForeignKey("Projects.id"), nullable=False)
    status = Column(String(20), nullable=True)
    ProjectContacts_id = Column(Integer, ForeignKey("ProjectContacts.id"), nullable=False)
    ReqruitmentLevel_id = Column(Integer, ForeignKey("ReqruitmentLevel.id"), nullable=False)

    def put_into_dto(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "Projects_id": self.Projects_id,
            "ProjectContacts_id": self.ProjectContacts_id,
            "ReqruitmentLevel_id": self.ReqruitmentLevel_id,
        }


class Candidate(Base):
    __tablename__ = "Candidates"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False)
    ReqruitmentLevel_id = Column(Integer, ForeignKey("ReqruitmentLevel.id"), nullable=False)
    TechnicalLevel_id = Column(Integer, ForeignKey("TechnicalLevel.id"), nullable=False)
    EnglishLevel_id = Column(Integer, ForeignKey("EnglishLevel.id"), nullable=False)

    def put_into_dto(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "ReqruitmentLevel_id": self.ReqruitmentLevel_id,
            "TechnicalLevel_id": self.TechnicalLevel_id,
            "EnglishLevel_id": self.EnglishLevel_id,
        }


class CandidateVacancy(Base):
    __tablename__ = "CandidateVacansies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    Vacancies_id = Column(Integer, ForeignKey("Vacancies.id"), nullable=False)
    Candidates_id = Column(Integer, ForeignKey("Candidates.id"), nullable=False)
    application_date = Column(Date, nullable=False)
    status = Column(String(45), nullable=True)

    def put_into_dto(self):
        return {
            "id": self.id,
            "Vacancies_id": self.Vacancies_id,
            "Candidates_id": self.Candidates_id,
            "application_date": self.application_date.isoformat() if self.application_date else None,
            "status": self.status,
        }


class Interview(Base):
    __tablename__ = "Interviews"

    id = Column(Integer, primary_key=True, autoincrement=True)
    interview_date = Column(DateTime(6), nullable=False)
    interviwer_name = Column(String(45), nullable=True)
    CandidateVacansies_id = Column(Integer, ForeignKey("CandidateVacansies.id"), nullable=False)

    def put_into_dto(self):
        return {
            "id": self.id,
            "interview_date": self.interview_date.isoformat() if self.interview_date else None,
            "interviwer_name": self.interviwer_name,
            "CandidateVacansies_id": self.CandidateVacansies_id,
        }


class InterviewResult(Base):
    __tablename__ = "InterviewResult"

    id = Column(Integer, primary_key=True, autoincrement=True)
    area_name = Column(String(45), nullable=False)
    comment = Column(Text, nullable=True)
    score_level = Column(String(45), nullable=False)
    Interviews_id = Column(Integer, ForeignKey("Interviews.id"), nullable=False)

    def put_into_dto(self):
        return {
            "id": self.id,
            "area_name": self.area_name,
            "comment": self.comment,
            "score_level": self.score_level,
            "Interviews_id": self.Interviews_id,
        }


class ProjectNote(Base):
    __tablename__ = "ProjectNotes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, nullable=False)
    note_text = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    def put_into_dto(self):
        return {
            "id": self.id,
            "project_id": self.project_id,
            "note_text": self.note_text,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }


class ProjectAuditLog(Base):
    __tablename__ = "ProjectAuditLog"

    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, nullable=False)
    action_type = Column(String(20), nullable=False)
    old_name = Column(String(45), nullable=True)
    new_name = Column(String(45), nullable=True)
    changed_at = Column(DateTime, server_default=func.now())

    def put_into_dto(self):
        return {
            "id": self.id,
            "project_id": self.project_id,
            "action_type": self.action_type,
            "old_name": self.old_name,
            "new_name": self.new_name,
            "changed_at": self.changed_at.isoformat() if self.changed_at else None,
        }