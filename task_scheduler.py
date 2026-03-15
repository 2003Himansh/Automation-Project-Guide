import schedule
import time
class TaskScheduler:

    def run_task(self, job, interval):

        schedule.every(interval).seconds.do(job)

        while True:
            schedule.run_pending()
            time.sleep(1)