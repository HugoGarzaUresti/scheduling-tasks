import time
import schedule
from datetime import datetime

def scheduled_task():
    print(f"Task executed at {datetime.now()}")

def main():
    schedule.every(10).seconds.do(scheduled_task)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
