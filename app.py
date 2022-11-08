import os
import schedule
import time
    
def job():
    os.system("python Hortinha.py")

schedule.every(62).minutes.do(job)    

while True:
    schedule.run_pending()
    time.sleep(1)