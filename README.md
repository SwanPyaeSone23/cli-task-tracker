# CLI Task Tracker

A simple, lightweight Command Line Interface (CLI) task tracking tool built with Python.

## Features
- Default status set to `in-progress`
- Custom date formatting (`DD-MM-YYYY HH:MM:SS`)
- Automatically manages sequential IDs without missing number gaps

## Usage

# Mark a task as done
python task_tracker.py done 1

# Show all tasks with timestamps
python task_tracker.py show-all-list

# Delete a task
python task_tracker.py delete 1