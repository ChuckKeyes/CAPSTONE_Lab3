#!/usr/bin/env bash

# Purposefully broken: troubleshoot this file.
# Business requirement:
#   Option 1: run account audit and save reports/account_report.txt
#   Option 2: run department summary and save reports/department_report.txt
#   Option 3: add an employee
#   Option 4: archive current reports into archive/
#   Option 5: exit cleanly

PROJECT_ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$PROJECT_ROOT" || exit 1

while true
do
    echo
    echo "============================"
    echo " CORPORATE ACCOUNT AUDITOR"
    echo "============================"
    echo "1 - Run account audit"
    echo "2 - Run department summary"
    echo "3 - Add employee"
    echo "4 - Archive reports"
    echo "5 - Exit"
    echo

    if ! read -r -p "Select an option (1-5): " choice
    then
        echo "Input closed. Exiting."
        exit 1
    fi

    case "$selection" in
        1)
            python3 scripts/account_audit.py > reports/account_report.txt
            echo "Account report generated."
            ;;
        2)
            python3 scripts/account_audit.py > reports/department_report.txt
            echo "Department report generated."
            ;;
        3)
            python3 scripts/add_employee.py
            ;;
        4)
            cp reports/*.txt archive/
            echo "Reports archived."
            ;;
        5)
            echo "Goodbye."
            exit 0
            ;;
        *)
            echo "Invalid selection."
            ;;
    esac
done