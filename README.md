# BankAccount Unit Test Suite

The project goal is to write unit tests using "pytest" for a simple "BankAccount" class to verify deposit, withdraw and initial balance behavior.

## Setup Instructions

Make sure Python is installed.

Go to the project folder
Open VS code for that folder.
Open terminal.

Install pytest using below command:
pip install pytest

run the tests using below command:

"pytest" : it shows test result.
"pytest -v" : it shows each tests status coverage and shows the result.

## The Logic (How I thought)

Pytest is simple to use and commonly taught for unit testing in Python. Each test function checks one requirement from the problem statement so that the tests are clear and easy to understand.

The issue I faced was that pytest was showing only dots "(...)" instead of showing which test passed. I fixed this by running "pytest-v" option, which displays each test name and its status.

## Output Screenshots

screenshots of the terminal showing all test cases with their status.
screenshots can be found ("unit-test-bank-account\screenshots") folder

## Future Improvements

If I had 2 more days, I would:
- Add a requirements.txt file
- Improve folder structure for larger projects
