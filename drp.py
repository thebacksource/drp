import tkinter as tk
from tkinter import scrolledtext
import requests
import time
import threading

# Roblox services
roblox_services = {
    "Website": "https://www.roblox.com",
    "API": "https://api.roblox.com",
    "Auth": "https://auth.roblox.com",
    "Catalog": "https://catalog.roblox.com",
    "Inventory": "https://inventory.roblox.com",
    "Friends": "https://friends.roblox.com",
    "Avatar": "https://avatar.roblox.com",
    "Economy": "https://economy.roblox.com",
    "Groups": "https://groups.roblox.com",
    "Notifications": "https://notifications.roblox.com",
    "Develop": "https://develop.roblox.com",
    "Forum": "https://forum.roblox.com",
    "Trading": "https://trades.roblox.com",
    "Presence": "https://presence.roblox.com",
    "Thumbnails": "https://thumbnails.roblox.com",
    "AssetDelivery": "https://assetdelivery.roblox.com",
    "Badges": "https://badges.roblox.com",
    "Points": "https://points.roblox.com",
    "TextFilter": "https://textfilter.roblox.com",
    "Messaging": "https://messaging.roblox.com"
}

# Store averages
response_times = {service: [] for service in roblox_services}

# Function to check services
def check_services():
    log_lines = []
    for service, url in roblox_services.items():
        try:
            response = requests.get(url, timeout=5)
            ms = int(response.elapsed.total_seconds()*1000)
            response_times[service].append(ms)
            avg = int(sum(response_times[service])/len(response_times[service]))
            if response.status_code == 200:
                status = "UP"
                color = "green" if ms < 500 else "yellow"
            else:
                status = f"ERROR {response.status_code}"
                color = "red"
            display_text = f"{service}: {status} | {ms}ms | avg {avg}ms"
        except requests.exceptions.RequestException as e:
            status = "DOWN"
            color = "red"
            display_text = f"{service}: {status} | {e}"
        # Update GUI
        service_labels[service].config(text=display_text, fg=color)
        # Log short reason if down
        if color == "red":
            log_lines.append(f"{service}: {status} | {e if 'e' in locals() else 'HTTP error'}")
    # Write log file
    with open("roblox_status_log.txt", "w") as f:
        if log_lines:
            f.write("\n".join(log_lines))
        else:
            f.write("All services UP\n")
    # Schedule next check
    root.after(10000, lambda: threading.Thread(target=check_services).start())  # refresh every 10s

# Create Tkinter window
root = tk.Tk()
root.title("Roblox Status Monitor")
root.geometry("700x700")

tk.Label(root, text="🔹 Roblox Services Status 🔹", font=("Arial", 18)).pack(pady=10)

# Scrollable frame for services
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)
canvas = tk.Canvas(frame)
scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Labels for each service
service_labels = {}
for service in roblox_services:
    lbl = tk.Label(scrollable_frame, text=f"{service}: Checking...", font=("Arial", 12))
    lbl.pack(anchor="w", pady=2)
    service_labels[service] = lbl

# Start the monitoring in a separate thread
threading.Thread(target=check_services).start()

root.mainloop()
