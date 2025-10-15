from datetime import datetime
from config import db


class Department(db.Model):
    __tablename__ = "departments"

    id = db.Column(db.Integer, primary_key=True )
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text)
    num_doctors = db.Column(db.Integer, default=0)
    contact_email = db.Column(db.String(120))

    # Relationships
    doctors = db.relationship("Doctor", back_populates="department")

    def __repr__(self):
        return f"<Department {self.name}>"


class Doctor(db.Model):
    __tablename__ = "doctors"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    years_of_experience = db.Column(db.Integer)
    specialization = db.Column(db.String(100))
    qualification = db.Column(db.String(100))

    department_id = db.Column(db.Integer, db.ForeignKey("departments.id"))
    department = db.relationship("Department", back_populates="doctors")

    # Relationships
    appointments = db.relationship("Appointment", back_populates="doctor")
    visits = db.relationship("PatientVisit", back_populates="doctor")

    def __repr__(self):
        return f"<Doctor {self.first_name} {self.last_name}>"

class Patient(db.Model):
    __tablename__ = "patients"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10))

    # Relationships
    appointments = db.relationship("Appointment", back_populates="patient")
    visits = db.relationship("PatientVisit", back_populates="patient")

    def __repr__(self):
        return f"<Patient {self.first_name} {self.last_name}>"


class Medicine(db.Model):
    __tablename__ = "medicines"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    

    # Relationships
    prescriptions = db.relationship("Prescription", back_populates="medicine")

    def __repr__(self):
        return f"<Medicine {self.name}>"

class Prescription(db.Model):
    __tablename__ = "prescriptions"

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patients.id"))
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctors.id"))
    medicine_id = db.Column(db.Integer, db.ForeignKey("medicines.id"))
    # dosage = db.column( db.String(50) , nullable =False  )
    date_issued = db.Column(db.DateTime)

    # Relationships
    medicine = db.relationship("Medicine", back_populates="prescriptions")
    patient = db.relationship("Patient")
    doctor = db.relationship("Doctor")

    def __repr__(self):
        return f"<Prescription {self.id}>"

class PatientVisit(db.Model):
    __tablename__ = "patient_visits"

    id = db.Column(db.Integer, primary_key=True)
    visit_no = db.Column(db.String(20), unique=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patients.id"))
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctors.id"))
    diagnosis = db.Column(db.Text)
    prescription_id = db.Column(db.Integer, db.ForeignKey("prescriptions.id"))
    date_time = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    patient = db.relationship("Patient", back_populates="visits")
    doctor = db.relationship("Doctor", back_populates="visits")
    prescription = db.relationship("Prescription")

    def __repr__(self):
        return f"<PatientVisit {self.visit_no}>"


class Appointment(db.Model):
    __tablename__ = "appointments"

    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctors.id"))
    patient_id = db.Column(db.Integer, db.ForeignKey("patients.id"))
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id"))

    date_time = db.Column(db.DateTime, default=datetime.utcnow)
    reason = db.Column(db.Text)
    is_cancelled = db.Column(db.Boolean, default=False)
    is_completed = db.Column(db.Boolean, default=False)

    # Relationships
    doctor = db.relationship("Doctor", back_populates="appointments")
    patient = db.relationship("Patient", back_populates="appointments")
    department = db.relationship("Department")

    def __repr__(self):
        return f"<Appointment {self.id}>"
