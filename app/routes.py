from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Student
from datetime import datetime

# Home page route to display students
@app.route("/")
def index():
    students = Student.query.all()  # Get all students
    return render_template("index.html", students=students)

# Add student route
@app.route("/add", methods=["POST"])
def add_student():
    roll_no = request.form['roll_no']
    name = request.form['name']
    class_name = request.form['class_name']
    dob = datetime.strptime(request.form['dob'], '%Y-%m-%d')

    # Create new student record
    new_student = Student(roll_no=roll_no, name=name, class_name=class_name, date_of_birth=dob)

    # Add to database and commit
    db.session.add(new_student)
    db.session.commit()

    return redirect(url_for("index"))

# Route to delete a student
@app.route("/delete/<int:id>")
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for("index"))
