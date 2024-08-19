import psutil
import time

def get_cpu_usage(process_name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            try:
                return proc.cpu_percent(interval=1)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                return 0  # Process no longer exists or can't be accessed
    return 0

def get_fps():
    start_time = time.time()
    time.sleep(0.1)  # Simulate frame processing
    end_time = time.time()
    return round(1 / (end_time - start_time), 2)

def monitor_performance(process_name):
    while True:
        cpu_usage = get_cpu_usage(process_name)
        fps = get_fps()

        print(f"CPU_USAGE={cpu_usage}")
        print(f"FPS={fps}")

        time.sleep(1)  # Adjust as needed

if __name__ == "__main__":
    monitor_performance("RobloxPlayerBeta.exe")
