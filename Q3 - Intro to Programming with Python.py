#Q3

class Patient:
    def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, phone_number, emergency_contact_name, emergency_contact_phone):
        self.full_name = f"{first_name} {middle_name} {last_name}"
        self.address = f"{address}, {city}, {state} {zip_code}"
        self.phone_number = phone_number
        self.emergency_contact = f"{emergency_contact_name}, {emergency_contact_phone}"


class Procedure:
    def __init__(self, name, date, practitioner, charges):
        self.name = name
        self.date = date
        self.practitioner = practitioner
        self.charges = charges


if __name__ == "__main__":
    # Create an instance of the Patient class with sample data
    patient = Patient("John", "Doe", "Smith", "123 Main St", "Anytown", "CA", "12345", "555-1234", "Jane Doe", "555-5678")

    # Create three instances of the Procedure class with sample data
    procedure1 = Procedure("Physical Exam", "Today's date", "Dr. Irvine", 250.00)
    procedure2 = Procedure("X-ray", "Today's date", "Dr. Jamison", 500.00)
    procedure3 = Procedure("Blood Test", "Today's date", "Dr. Smith", 200.00)

    # Display patient and procedures information
    print("Patient Information:")
    print("Full Name:", patient.full_name)
    print("Address:", patient.address)
    print("Phone Number:", patient.phone_number)
    print("Emergency Contact:", patient.emergency_contact)

    total_charges = procedure1.charges + procedure2.charges + procedure3.charges

    print("\nProcedure Information:")
    print(f"\nProcedure #1:\nProcedure name: {procedure1.name}\nDate: {procedure1.date}\nPractitioner: {procedure1.practitioner}\nCharge: {procedure1.charges}")
    print(f"\nProcedure #2:\nProcedure name: {procedure2.name}\nDate: {procedure2.date}\nPractitioner: {procedure2.practitioner}\nCharge: {procedure2.charges}")
    print(f"\nProcedure #3:\nProcedure name: {procedure3.name}\nDate: {procedure3.date}\nPractitioner: {procedure3.practitioner}\nCharge: {procedure3.charges}")

    print("\nTotal Charges for all Procedures:", total_charges)
