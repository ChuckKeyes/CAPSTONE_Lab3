# Lab 3 — Troubleshooting & Debugging

## Overview

For Lab 3, I worked on fixing a broken project. I started by running the program first so I could see what errors came up before changing stuff.

The main files I worked on were:

* `audit_menu.sh`
* `account_audit.py`
* `department_summary.py`
* `add_employee.py`

# Problems found

When I first ran the Python files, I got syntax errors. The first problems were mostly missing colons `:`.

Examples:

* `account_audit.py` was missing a `:` after `elif days >= 30`
* `department_summary.py` was missing a `:` after the `for` loop
* `add_employee.py` was missing a `:` after `elif not days.isdigit()`

![alt text](<Schermafbeelding 2026-07-03 004704.png>)

# What solved issues

 `audit_menu.sh`

The menu was able to open, but I had to adjust it so the options ran the correct scripts.

The menu options now do this:

* Option 1 makes the account report
* Option 2 makes the department report
* Option 3 adds an employee
* Option 4 archives the reports
* Option 5 exits the menu

I also used `python` instead of `python3` because I am on Windows and that is what worked on machine.

`account_audit.py`

This file checks if employee accounts are:

* `ACTIVE`
* `REVIEW`
* `DISABLE`

After fixing the missing colons, I found another problem. The code was mixing up the department and the days since last login.

The data should be read like this:

```text
username,department,days
```

I fixed the order so the account report showed the right department and the right status.

`department_summary.py`

This file counts how many employees are in each department.

One issue was this line:

```python
department_counts[department] == 1
```

That was wrong because `==` checks something. It does not set the value.

I changed it to:

```python
department_counts[department] = 1
```

After that, the department count worked.

`add_employee.py`

This file adds a new employee to `employees.txt`.

At first, it had a syntax error. After that, it had a writing error because it was trying to write a tuple instead of normal text.

I fixed it so the new employee gets written like this:

```text
username,department,days
```

I also fixed the blank username check and made sure the new employee starts on its own line.

# Testing

I tested each Python file by itself:

```bash
python scripts/account_audit.py
python scripts/department_summary.py
python scripts/add_employee.py
```

Then I tested the full menu:

```bash
bash audit_menu.sh
```

I tested options:

```text
1
2
3
4
5
```

I also checked the reports and archive files with:

```bash
cat reports/account_report.txt
cat reports/department_report.txt
cat archive/account_report.txt
cat archive/department_report.txt
```

# Screenshots

I included screenshots showing:

* the first syntax errors
* the code lines where I added the missing colons
* the evaluator failing with 5 passed and 10 failed
* the evaluator improving to 14 passed and 1 failed
* the final evaluator passing with 15 passed and 0 failed
* the reports and archive files working

# Final Result

After the last fix, I ran:

```bash
bash evaluate_lab.sh
```

Final result:

```text
Results: 15 passed, 0 failed.
Lab evaluation passed.
```
![alt text](<Schermafbeelding 2026-07-04 020323.png>)

# What I Learned

This lab helped me practice fixing errors one at a time. Some errors were typos, like missing colons. Other errors were logic problems.

Optional Instructor Review Prompts
After solving the lab, explain:

Which errors prevented execution before runtime?

Which errors allowed execution but produced wrong behavior?
- Syntax errors stopped the scripts from running.
Why is validating external data important in operational automation?
- 
Why can tuples be useful for fixed employee records but not be written directly to a file?
- because tuples are immutable, and in a dynamic input, does cannot be adjusted 
Why should an orchestration script validate that expected files exist before archiving?