Troubleshooting Order
1. Confirm files and permissions
pwd
find . -maxdepth 2 -type f | sort
chmod +x audit_menu.sh evaluate_lab.sh
2. Check syntax first
bash -n audit_menu.sh

python3 -m py_compile scripts/account_audit.py
python3 -m py_compile scripts/department_summary.py
python3 -m py_compile scripts/add_employee.py

Fix anything that stops the files from even running.

3. Fix audit_menu.sh enough to run options

Make sure:

1 runs account_audit.py > reports/account_report.txt
2 runs department_summary.py > reports/department_report.txt
3 runs add_employee.py
4 copies reports/*.txt to archive/
5 exits cleanly

Do not perfect the Python yet. First make the menu dispatch work.

4. Fix account_audit.py

Focus on:

read data/employees.txt
skip blank lines
skip malformed lines
skip non-numeric days
classify:
0-29 ACTIVE
30-89 REVIEW
90+ DISABLE

Test:

python3 scripts/account_audit.py
5. Fix department_summary.py

Focus on:

only count valid records
skip malformed lines
skip non-numeric days
print department counts

Test:

python3 scripts/department_summary.py
6. Fix add_employee.py

Focus on validation:

blank username = reject
blank department = reject
non-numeric days = reject
valid record = append one line

Test invalid input first, then valid input.

7. Test full menu flow
./audit_menu.sh

Enter:

1
2
4
5

Then check:

ls -al reports
ls -al archive
cat reports/account_report.txt
cat reports/department_report.txt
8. Run evaluator last
./evaluate_lab.sh

Goal:

Results: 15 passed, 0 failed.
Lab evaluation passed.
Big rule

Fix in this order:

Syntax → Menu → Account Audit → Department Summary → Add Employee → Archive → Evaluator