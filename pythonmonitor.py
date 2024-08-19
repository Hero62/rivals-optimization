import psutil
import time

def get_cpu_usage(process_name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            return proc.cpu_percent(interval=1)
    return None

def get_fps():
    start_time = time.time()
    time.sleep(0.1)  # Simulate frame processing
    end_time = time.time()
    return round(1 / (end_time - start_time), 2)

def monitor_performance(process_name):
    while True:
        cpu_usage = get_cpu_usage(process_name)
        fps = get_fps()

        if cpu_usage is not None:
            print(f"CPU_USAGE={cpu_usage}%")
            print(f"FPS={fps}")
        else:
            print("CPU_USAGE=Process Not Found")
            print("FPS=0")

        time.sleep(1)  # Adjust as needed

if __name__ == "__main__":
    monitor_performance("RobloxPlayerBeta.exe")
