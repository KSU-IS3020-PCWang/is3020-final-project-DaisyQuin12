import csv
def add_appointment(appointments, name, number,date, time, reason):
    appointment = {
        "id": max([a["id"] for a in appointments], default=0) + 1,
        "name": name,
        "number": number,
        "date": date,
        "time": time,
        "reason": reason
    }
    appointments.append(appointment)
    return appointment
def view_appointments(appointments):
    if not appointments:
        print("No appointments scheduled.")
        return
    for appointment in appointments:
        print("Appointment:", appointment["id"])
        print("Name:", appointment["name"])
        print("Number:", appointment["number"])
        print("Date:", appointment["date"])
        print("Time:", appointment["time"])
        print("Reason:", appointment["reason"])


def save_appointments(appointments):
    def load_appointments():
        appointments = []

        try:
            with open("data/appointments.csv", "r") as csvfile:
                reader = csv.DictReader(csvfile)

                for appointment in reader:
                    appointment["id"] = int(appointment["id"])
                    appointments.append(appointment)

        except FileNotFoundError:
            print("No saved appointments found.")

        return appointments

    with open("data/appointments.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["id", "name", "number", "date", "time", "reason"])
        writer.writeheader()
        writer.writerows(appointments)
    print("Appointments saved.")


def load_appointments():
    appointments = []

    try:
        with open("data/appointments.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile)

            for appointment in reader:
                appointment["id"] = int(appointment["id"])
                appointments.append(appointment)

    except FileNotFoundError:
        print("No saved appointments found.")

    return appointments

def search_appointments(appointments):
    name = input("Enter customer name: ")
    found = False

    for appointment in appointments:
        if name.lower() == appointment["name"].lower():
            view_appointments([appointment])
            found = True

    if not found:
        print("No matching appointments found.")


def delete_appointment(appointments):
    appointment_id = input("Enter appointment number: ")

    for appointment in appointments:
        if str(appointment["id"]) == appointment_id:
            appointments.remove(appointment)
            save_appointments(appointments)
            print("Appointment deleted.")
            return

    print("Appointment not found.")


def main():
    appointments = load_appointments()

    while True:
        print("\nAppointment Scheduler")
        print("1. Add appointment")
        print("2. View appointments")
        print("3. Search appointments")
        print("4. Delete appointment")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter customer name: ")
            number = input("Enter phone number: ")
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            reason = input("Enter reason for appointment: ")

            add_appointment(appointments, name, number, date, time, reason)
            save_appointments(appointments)

        elif choice == "2":
            view_appointments(appointments)

        elif choice == "3":
            search_appointments(appointments)

        elif choice == "4":
            delete_appointment(appointments)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

main()
