Real-Time Network Ping Monitor

A Python script that continuously pings a list of IP addresses and plots their RTT (Round-Trip Time) live on a graph. This helps visualize network latency and identify delays or unreachable nodes in real time.
🧩 Features

    ✅ Hardcoded list of IP addresses (customizable)

    📈 Live plotting of ping RTTs over time using matplotlib

    🚦 Handles packet loss and unreachable hosts gracefully

    🔄 Auto-updating graph with time on X-axis and RTT on Y-axis

    🧵 Multi-threaded pinging for simultaneous IP monitoring

    💻 Works on Linux, macOS, and Windows

🛠️ Requirements

    Python 3.x

    matplotlib (Install with pip install matplotlib)

🚀 How to Run

    Clone the repository:

git clone https://github.com/anspectrum/Real-Time-Network-Ping-Monitor.git

cd Real-Time-Network-Ping-Monitor

Install dependencies:

pip install matplotlib

Run the script:

    python3 pings.py

✏️ Configuration

You can modify the list of IP addresses at the top of pings.py:

IP_ADDRESSES = [
    "192.168.100.1",
    "192.168.0.1",
    "192.168.2.2",
    "192.168.2.1",
    "1.1.1.1"
]

Add or remove IPs as needed.
📊 Behavior

    Each IP is pinged once per second.

    RTTs are displayed on a live graph.

    Only the last 100 RTT values are shown for each IP (rolling window).

    If an IP does not respond, it will appear as a gap in the line for that IP.

🧠 Example Use Cases

    Diagnose intermittent network issues

    Monitor latency to routers, gateways, DNS servers, or public IPs

    Visualize spikes and drops in network performance

<img width="1366" height="526" alt="Screenshot" src="https://github.com/user-attachments/assets/ace61217-cd2b-4882-b6cc-8ba969b680ad" />
