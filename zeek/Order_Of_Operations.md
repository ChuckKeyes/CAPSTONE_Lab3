# This is the Order of Operations:

## 1. Syntax (Checking files & permissions precedes this step)
### 1.1:
- "pwd"
- "cd /path/to/CAPSTONE_Lab3/zeek"
- "find . -maxdepth 2 -type f | sort"
- "chmod +x audit_menu.sh evaluate_lab.sh"
### 1.2:
- "bash -n audit_menu.sh"

- "python3 -m py_compile scripts/account_audit.py"
- "python3 -m py_compile scripts/account_audit.py"
- "python3 -m py_compile scripts/account_audit.py"

  (**Fix anything that stops the files from running at all!!**)
  
## 2. Fix up "Menu"
Confirm:
- "1" --> runs account_audit.py > reports/account_report.txt
- "2" --> runs department_summary.py > reports/department_report.txt
- "3" --> runs add_employee.py
- "4" --> copies reports/*.txt to archive/
- "5" --> exits cleanly

  (**Do NOT finalize the Python files yet...First make sure the menu dispatch works!!**)
  
## 3. Account Audit
Points of interest:
- reading data/employees.txt
- skipping blank lines
- skipping malformed lines
- skipping non-numeric days

Classify:
- 0-29 --> ACTIVE
- 30-89 --> REVIEW
- 90+ --> DISABLE

Test out this file:
- "python3 scripts/account_audit.py"
  
## 4. Department Summary

Points of interest:
- only counting valid records
- printing department counts
- skipping malformed lines
- skipping non-numeric days

Test out this file:
- "python3 scripts/department_summary.py"

## 5. Add Employee
Points of interest (validation):
- blank username = reject
- blank department = reject
- non-numeric days = reject
- valid record = append one line

  (**Test invalid input first, THEN valid input!!**)
  
## 6. Test flow & Archive 
- "./audit_menu.sh" (Run this script!)

Enter the following selections (in order):
- "1"
- "2"
- "4"
- "5"

Next, check these parameters:
- "ls -al reports"
- "ls -al archive"
- "cat reports/account_report.txt"
- "cat reports/department_report.txt"

## 7. Evaluation (Moment of Truth)
- "./evaluate_lab.sh" (Run this script!)

Expectation:

- "Results: 15 passed, 0 failed."
- "Lab evaluation passed."
