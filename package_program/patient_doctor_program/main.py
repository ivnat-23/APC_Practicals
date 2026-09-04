from patient_management.patient import add_patient, display_patient
from doctor_management.doctor import add_doctor, display_doctor
from billing.bill import calculate_bill, display_bill
from medical_records.record import add_record, display_record

patient=add_patient(101,"Amit",21)
doctor=add_doctor(1,"Dr. Sharma","Cardiology")
bill=calculate_bill(5000,1000)
record=add_record(101,"Fever","Paracetamol")

display_patient(patient)
display_doctor(doctor)
display_bill(bill)
display_record(record)
