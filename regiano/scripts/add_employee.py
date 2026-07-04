# Purposefully broken: troubleshoot this file.
# Business requirement:
#   Prompt for username, department, and days since last login.
#   Reject blank username or department and non-numeric days.
#   Append one correctly formatted CSV line for valid input.

username = input("Username: ")
department = input("Department: ")
days = input("Days since last login: ")

if username == "" or department == "":
    print("Username and department must not be blank.")

# added a colon
elif not days.isdigit():
    print("Days since last login must be a whole number.")

# changed the variable to a string
else:
    new_employee = "\n" + username +","+ department +","+ days

    with open("data/employees.txt", "a") as file:
        file.write(new_employee)

    print(f"Employee {username} added successfully.")
