from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.utils.db import Base

projects_contacts = Table(
    'Projects_has_ProjectContacts', 
    Base.metadata,
    Column('Projects_id', Integer, ForeignKey('Projects.id'), primary_key=True),
    Column('ProjectContacts_id', Integer, ForeignKey('ProjectContacts.id'), primary_key=True)
)

class Project(Base):
    __tablename__ = 'Projects'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_name = Column(String(45), nullable=False)
    description = Column(Text, nullable=True)
    
    vacancies = relationship('Vacancy', backref='project_ref', cascade='all, delete-orphan')
    
    contacts = relationship('ProjectContact', secondary=projects_contacts, backref='projects')

    def put_into_dto(self):
        return {
            'id': self.id,
            'project_name': self.project_name,
            'description': self.description
        }


class ProjectContact(Base):
    __tablename__ = 'ProjectContacts'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(45), nullable=True)
    phone = Column(String(45), nullable=True)

    def put_into_dto(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'email': self.email,
            'phone': self.phone
        }


class Vacancy(Base):
    __tablename__ = 'Vacancies'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(45), nullable=False)
    description = Column(Text, nullable=False)
    Projects_id = Column(Integer, ForeignKey('Projects.id'), nullable=False)
    status = Column(String(20), nullable=True)
    ProjectContacts_id = Column(Integer, ForeignKey('ProjectContacts.id'), nullable=False)
    ReqruitmentLevel_id = Column(Integer, nullable=False)

    def put_into_dto(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'Projects_id': self.Projects_id
        }