from sqlalchemy.orm import Session
from models.employee import Employee

class EmployeeCrud:
    @staticmethod
    def create_employee(db:Session, name: str, department: str, salary: int):
        try:
            employee = Employee(name=name, department=department, salary=salary)
            db.add(employee)
            db.commit()
            db.refresh(employee)
            return employee
        except Exception as e:
            db.rollback()
            raise e
    
    
    @staticmethod
    def get_employee(db:Session, id: int):
        return db.query(Employee).filter(Employee.id == id).first()
    
    @staticmethod
    def get_all_employee(db:Session):
        return db.query(Employee).all()
    
    @staticmethod
    def update_employee(db:Session, id: int, **kwargs):
        try:
            employee = db.query(Employee).filter(Employee.id == id).first()
            if employee:
                for key, value in kwargs.items():
                    setattr(employee, key, value)
                db.commit()
                db.refresh(employee)
            return employee
        except Exception as e:
            db.rollback()
            raise e
        
    @staticmethod
    def delete_employee(db:Session, id: int):
        try:
            employee = db.query(Employee).filter(Employee.id == id).first()
            if employee:
                db.delete(employee)
                db.commit()
                return True
            return False
        except Exception as e:
            db.rollback()
            raise e
            
            
                
            
    