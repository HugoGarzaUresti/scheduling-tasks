# Scheduling Tasks

This guide demonstrates how to schedule tasks in Python using the `schedule` library. We will create a simple task that prints a message to the console every 10 seconds.

## Requirements

- Python 3.x
- `schedule` library

## Setup

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Run the application:
    ```sh
    python run.py
    ```

## Code Explanation

### `app/scheduler.py`

This module contains functions to schedule tasks.

- **`scheduled_task`**: A function that prints the current datetime to the console.
- **`main`**: Schedules `scheduled_task` to run every 10 seconds and starts the scheduler.

### `run.py`

This script serves as the entry point for the application. It calls the `main` function to start the task scheduler.

## Additional Information

- The `schedule` library provides a simple way to schedule tasks at specific intervals.
- You can adjust the interval and task as needed for your application.
