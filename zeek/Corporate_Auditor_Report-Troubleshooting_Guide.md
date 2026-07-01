# CAPSTONE Lab 3 – Corporate_Auditor_Report (Troubleshooting Guide)

## Student

**Omari Miller**

---

# Overview

The Corporate Account Auditor project was intentionally supplied with syntax errors, logic errors, runtime errors, and data validation problems. The objective was to troubleshoot the application while preserving the original business requirements. The project consisted of three Python programs, one Bash orchestration script, and a functional evaluator.

---

# Errors That Prevented Execution Before Runtime

These errors prevented the programs from running until they were corrected.

## account_audit.py

* Missing colon after the `elif days >= 30` statement, causing a Python `SyntaxError`.
* The interpreter stopped before executing the remainder of the program.

## add_employee.py

* Missing colon after the `elif not days.isdigit()` statement, producing a Python `SyntaxError`.

These syntax errors had to be repaired before any functional testing could begin.

---

# Errors That Allowed Execution but Produced Wrong Behavior

Several scripts executed but produced incorrect results due to logic or runtime errors.

## account_audit.py

* `line.strip()` was called without assigning the result back to `line`, preventing proper removal of newline characters.
* Blank-line detection failed because newline characters remained.
* Employee tuple indexes were reversed:

  * Department was retrieved from index 2 instead of index 1.
  * Days were retrieved from index 1 instead of index 2.
* Comparing a department string to an integer caused a runtime `TypeError`.
* Malformed records and invalid inactivity values required validation before processing.

## department_summary.py

* Dictionary initialization used the comparison operator (`==`) instead of the assignment operator (`=`).
* New departments were never added correctly to the dictionary.
* The corrected version properly initialized each department count before incrementing it.

## add_employee.py

* Username and department validation incorrectly used the `and` operator instead of validating each field independently.
* Employee data was stored as a tuple and passed directly to `file.write()`.
* `file.write()` accepts only strings, resulting in a `TypeError`.
* The employee record needed to be written as a properly formatted CSV string.

## audit_menu.sh

* User input was stored in the variable `choice`, but the `case` statement examined `selection`.
* Option 2 incorrectly executed `account_audit.py` instead of `department_summary.py`.
* Report archiving did not verify that report files existed before copying them.

---

# Why Validating External Data Is Important

Operational automation frequently processes information supplied by users, HR systems, databases, or external applications. These data sources cannot always be trusted to contain valid information.

Input validation prevents:

* application crashes,
* invalid reports,
* corrupted data files,
* incorrect audit results,
* security issues caused by malformed input.

During this lab, the supplied employee file intentionally contained malformed records, invalid numeric values, and incorrectly formatted CSV entries. The repaired programs skipped invalid records while continuing to process valid employee information.

---

# Why Tuples Are Useful but Cannot Be Written Directly to a File

Tuples provide a convenient way to store a fixed collection of related values.

Example:

* username
* department
* days since last login

A tuple keeps these values grouped together during processing.

However, the `file.write()` function only accepts a string. Attempting to write a tuple directly produces a `TypeError`.

Therefore, employee information must first be converted into a properly formatted CSV string before being written to the data file.

---

# Why the Orchestration Script Should Verify Files Before Archiving

Automation scripts should always verify that required files exist before attempting operations such as copying or archiving.

Without validation:

* copy commands may fail,
* error messages may confuse users,
* incomplete archives may be created,
* automated workflows may terminate unexpectedly.

By confirming that report files exist before archiving them, the script becomes more reliable and better suited for production environments.

---

# Lessons Learned

This troubleshooting exercise demonstrated the importance of distinguishing between syntax errors, logic errors, and runtime errors. It also reinforced proper input validation, CSV processing, Bash menu design, Python data structures, and defensive programming techniques commonly used in Linux automation and cloud engineering.

