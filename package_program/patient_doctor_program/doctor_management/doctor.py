def add_doctor(doctor_id,name,specialization):
    return doctor_id,name,specialization

def display_doctor(doctor):
    print("Doctor ID:",doctor[0])
    print("Doctor Name:",doctor[1])
    print("Specialization:",doctor[2])
