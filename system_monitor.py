import psutil


class SystemMonitor:

    def check_system(self):

        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent

        print("\nSystem Status\n")

        print("CPU Usage:", cpu, "%")
        print("Memory Usage:", memory, "%")
        print("Disk Usage:", disk, "%")