import subprocess
import platform
import threading
import time
import matplotlib.pyplot as plt
import re
from collections import deque

# Hardcoded IP addresses
IP_ADDRESSES = [
    "192.168.100.1",
    "192.168.0.1",
    "192.168.2.2",
    "192.168.2.1",
    "1.1.1.1"
]

# Max number of data points to retain
MAX_HISTORY = 100
ping_history = {ip: deque(maxlen=MAX_HISTORY) for ip in IP_ADDRESSES}
time_history = deque(maxlen=MAX_HISTORY)
lock = threading.Lock()

def parse_rtt(output):
    # Extract RTT based on OS
    if platform.system().lower() == "windows":
        match = re.search(r'Average = (\d+)ms', output)
    else:
        match = re.search(r'time[=<]([\d.]+) ?ms', output)
    return float(match.group(1)) if match else None

def ping_host(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    wait_flag = '-w' if platform.system().lower() == 'windows' else '-W'
    while True:
        try:
            output = subprocess.check_output(
                ['ping', param, '1', wait_flag, '1', str(ip)],
                stderr=subprocess.DEVNULL,
                universal_newlines=True
            )
            rtt = parse_rtt(output)
        except subprocess.CalledProcessError:
            rtt = None

        with lock:
            ping_history[ip].append(rtt)

        time.sleep(1)

def plot_rtt():
    plt.ion()
    fig, ax = plt.subplots()
    lines = {ip: ax.plot([], [], label=ip)[0] for ip in IP_ADDRESSES}
    ax.set_ylabel("RTT (ms)")
    ax.set_xlabel("Time (s)")
    ax.set_title("Live RTT to IPs")
    ax.legend()

    start_time = time.time()

    while True:
        with lock:
            current_time = time.time() - start_time
            time_history.append(current_time)

            for ip in IP_ADDRESSES:
                y_data = list(ping_history[ip])
                x_data = list(time_history)[-len(y_data):]  # Ensure lengths match
                lines[ip].set_data(x_data, y_data)

            ax.relim()
            ax.autoscale_view()

        plt.pause(1)


def main():
    for ip in IP_ADDRESSES:
        threading.Thread(target=ping_host, args=(ip,), daemon=True).start()
    plot_rtt()

if __name__ == "__main__":
    main()
