# CAPSTONE Lab 3 – Corporate_Auditor_Report (Troubleshooting Guide)

## Auditor

*Christopher Alonzo*

---

# Overview

During this lab, the supplied employee file intentionally contained malformed records, invalid numeric values, and incorrectly formatted CSV entries. The repaired programs skipped invalid records while continuing to process valid employee information.

This auditor project contains syntax errors, logic errors, runtime errors, and data validation problems and syncing problems

## Objective: 
- Troubleshoot and run this application with the original conditions & requirements 
- DO NOT completely rewrite the project! 

## Components: 
 - Python programs (3)
 - Bash orchestration script (1)
 - Functional evaluator (1)

---

# Errors That Prevented Execution Before Runtime

My pathway to run the files was not executing properly. I needed a command .pv. 


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

In every work environment all data must be double checked before further processed. Errors are rampant in every industry. Same applies to external data, external data such as HR systems, payroll, daily logs, all need to be audited for further processing. 

Input validation prevents:

*   application malfunction,
*   inaccurate reports,
*   corrupted data files,
*   incorrect audit results,
*   security issues caused by malformed input.
---

# Why Tuples Are Useful but Cannot Be Written Directly to a File

Tuples provide a convenient way to store a fixed collection of related values.

In the project we used;
* username
* department
* days since last login

A tuple keeps these values grouped together before prepping.

However, the `file.write()` function only understands text string. Attempting to write a tuple directly produces a `TypeError`.

In order for the Tuple to work, they must be formatted in the proper CSV string before converting into a data file.


---

# Why the Orchestration Script Should Verify Files Before Archiving

The purpose of orchestrating scripts is to coordinate and run scripts and programs in the proper order so it does not have to be done manually. 

Automation scripts can also verify necessary files to exist before attempting operations such as copying or archiving. If you do not validate;

* copy commands may fail,
* error messages may confuse users,
* incomplete archives may be created,
* automated workflows may terminate unexpectedly.

By confirming that report files exist before archiving them, the script becomes more executable and can be pushed to eventually used for projects.

---

# Lessons Learned

The troubleshooting exercise helped us distinguish and fix syntax errors, logic errors and runtime errors. We had to use what we learned in class and class readings on how to fix the errors and run different type sof files properly. This included; python and shell script.

