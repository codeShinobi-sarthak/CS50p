import time, sched
import schedule


"""
 # 🥇 Method 1: Using time.sleep()
 # This will run infinitely after every 5 seconds so stop it
def task():
    print("Task run after 5 seconds")

while True:
    task()
    time.sleep(5)  # wait 5 seconds before running again
    
"""


"""
# 🥈 Method 2: Using sched module (built-in scheduler)

scheduler = sched.scheduler(time.time, time.sleep)

def my_task():
    print("Task executed at", time.ctime())

# Schedule task after 5 seconds
scheduler.enter(5, 1, my_task)

print("Starting scheduler...")
scheduler.run()

"""



# 🥉 Method 3: Using schedule library (very popular)
def my_task():
    print("Task executed!")

# Schedule tasks
schedule.every(5).seconds.do(my_task)
# schedule.every().day.at("14:30").do(my_task)  # at 2:30 PM

while True:
    schedule.run_pending()
    time.sleep(1)




"""
🏆 Method 4: Using APScheduler (Advanced)

If you need something more professional (like cron jobs, persistent jobs, etc.), use APScheduler.

"""