# Purposefully broken: troubleshoot this file.
# Business requirement:
#   Count valid employee records by department.
#   Ignore malformed records and records with non-numeric inactivity values.

from pathlib import Path

department_counts = {}

employees_file = Path(__file__).resolve().parent.parent / "data" / "employees.txt"

with open(employees_file, "r") as file:
    for line in file:
        line = line.strip()

        if line == "":
            continue

        parts = line.split(",")

        if len(parts) != 3:
            continue

        username = parts[0]
        department = parts[1]
        days = parts[2]

        if not days.isdigit():
            continue

        if department in department_counts:
            department_counts[department] += 1
        else:
            department_counts[department] = 1

print("DEPARTMENT SUMMARY")
print("==================")

for department, count in department_counts.items():
    print(f"{department}: {count}")
