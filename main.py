from flask import Flask, request, jsonify
from config.database import getdb, engine
from models.employee import Employee, Base
from crud.employee_crud import EmployeeCrud

app = Flask(__name__)

# Create database tables
Base.metadata.create_all(bind=engine)

@app.route('/employees/create', methods=['POST'])
def create_employee():
    try:
        data = request.json
        db = next(getdb())
        employee = EmployeeCrud.create_employee(
            db=db,
            name=data['name'],
            department=data['department'],
            salary=data['salary']
        )
        
        return jsonify({
            'id': employee.id,
            'name': employee.name,
            'department': employee.department,
            'salary': employee.salary,
        }), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    try: 
        db = next(getdb())
        employee = EmployeeCrud.get_employee(db=db, id=id)
        
        if employee:
            return jsonify({
                'id': employee.id,
                'name': employee.name,
                'department': employee.department,
                'salary': employee.salary,
            })
        return jsonify({'message': 'Employee not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/employees', methods=['GET'])
def get_all_employees():
    try:
        db = next(getdb())
        employees = EmployeeCrud.get_all_employee(db=db)
        
        return jsonify([{
            'id': emp.id,
            'name': emp.name,
            'department': emp.department,
            'salary': emp.salary,
        } for emp in employees])
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/employees/update/<int:id>', methods=['PUT'])  # Fixed this line
def update_employee(id):
    try:
        data = request.json
        db = next(getdb())
        
        employee = EmployeeCrud.update_employee(db=db, id=id, **data)
        if employee:
            return jsonify({
                'id': employee.id,
                'name': employee.name,
                'department': employee.department,
                'salary': employee.salary
            })
        return jsonify({'message': 'Employee not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/employees/delete/<int:id>', methods=['DELETE'])
def delete_employee(id):
    try:
        db = next(getdb())  # Fixed getdb() function name
        success = EmployeeCrud.delete_employee(db=db, id=id)  # Fixed class name
        
        if success:
            return jsonify({'message': 'Employee deleted successfully'})
        return jsonify({'message': 'Employee not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)