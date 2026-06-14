# -todo-api-report
-

## Description
This program connects to the JSONPlaceholder Todos API and fetches the
to-do list for a specific user (userId=1). It then analyzes the list and
prints a short report showing how many tasks are completed, how many are
still pending, the completion rate, and an overall project status.

## Features
- Sends a GET request to a public API using the `requests` library
- Checks the response status code before reading any data
- Safely reads each todo using `.get()`
- Counts completed and pending tasks
- Calculates the completion rate as a percentage
- Prints a final project status: EXCELLENT, GOOD, or NEEDS_FOCUS
- Prints a clear error message if the API request fails, instead of crashing

## How to Run
1. Make sure Python 3 is installed.
2. Install the requests library if needed:
   ```
   pip install requests
   ```
3. Run the program:
   ```
   python main.py
   ```

## Technologies
- Python 3
- requests library
- JSONPlaceholder public API
