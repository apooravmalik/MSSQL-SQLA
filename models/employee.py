from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    department = Column(String(50))
    salary = Column(Integer)
    
    def __repr__(self):
        return f"Employee(id={self.id}, name={self.name}, department={self.department}, salary={self.salary})"
    