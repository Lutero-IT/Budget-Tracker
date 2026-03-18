# Budget Tracker

## Description
This program is written in Python and takes input from a user
in a form of numbers and saves it as an account balance.
User can next add incomes or subtract expenses from the provided account balance.
Program tracks user's account balance from the moment it is definied.
It saves all the performed operations, starting and final account balance in form
of JSON file, which is next imported to JSON file where all the actions are saved.
When users starts program again, necessary information are downloaded from the
JSON file. In case when there is no such a file, it is created.

## What problem it solves?
It allows user to easliy track and update his story of incomes and expenses.

## Technologies used
Used Python to write the structure and logic of the program.
Used JSON to save and load user's account balance and actions.
From the python libraries and modules I used:
* json module - to convert and save actions performed by a user in Python to a format that allows to store data in JSON file
* datetime module - to give each entry exact time containing day, hour, minutes and seconds.
* Path module from pathlib - to connect Python program with a JSON file

## What have I learned in this project?
1. How to import and make use of python libraries and modules like json, datetime, pathlib.
2. How to create functions ( addIncome(), convert(), exitProgram())
3. if/else statements and how to use them to catch incorrect input and prevent program from
error
4. How to work with dictionaries ( options dictionary with functions assigned )
5. How to create, edit, save and load JSON files

## How to launch program?
Downlad the files ( either both .py and .json or just .py - .json will be created automatically if
missing) and type 'python budget_tracker.py' in terminal:
```
python budget_tracker.py
```
Next follow the instructions shown on the screen.

## Future plans
I'm planning to develop program much more than what it is today.
One of the things is sending and downloading data not from a local folder or machine, but
from a remote server. This way I'll learn how to use web structure in my programs.
I'm also planning to try different ways of saving data, like in a CSV file.

18.03.26