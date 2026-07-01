# Purposefully broken: troubleshoot this file.
# Business requirement:
#   Prompt for username, department, and days since last login.
#   Reject blank username or department and non-numeric days.
#   Append one correctly formatted CSV line for valid input.

username = input("Username: ")
department = input("Department: ")
days = input("Days since last login: ")

if username == "" and department == "":
    print("Username and department must not be blank.")

elif not days.isdigit()
    print("Days since last login must be a whole number.")

else:
    new_employee = (username, department, days)

    with open("data/employees.txt", "a") as file:
        file.write(new_employee)

    print(f"Employee {username} added successfully.")